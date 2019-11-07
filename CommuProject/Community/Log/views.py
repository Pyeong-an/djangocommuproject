from django.shortcuts import render, redirect
from .models import LogList
from Char.models import CharList
from sub_log.models import SubLogList
from charanking.models import charanking
# Create your views here.

def log_plus(char):
    """
    로그 카운터를 하나 증가시키고 저장하는 함수
    """
    charank = charanking.objects.get(charname=char.charname)
    charank.logcount +=1
    charank.save()
    return
def log_minus(char):
    """
    로그 카운터를 하나 감소시키고 저장하는 함수
    """
    charank = charanking.objects.get(charname=char.charname)
    charank.logcount -=1
    charank.save()
    return
def log_substitute(log,char,where,contents):
    """
    로그에 값을 대입하는 함수
    """
    log.charname = char.charname
    log.where = where
    log.contents = contents
    log.charcon = char.charcon
    log.password = char.password
    
    return

def contents_replace(contents):
    """
    폰트, 이미지 태그 치환 함수
    """
    
    contents = contents.replace('{{', '<font color="green">')
    contents = contents.replace('}}', '</font>')
    contents = contents.replace('[[', '<font color="red">')
    contents = contents.replace(']]', '</font>')
    contents = contents.replace('((', '<font color="blue">')
    contents = contents.replace('))', '</font>')
    contents = contents.replace('+++', '<img src="')
    contents = contents.replace('---', '"></img>"')

    return contents

def main_POST(request):
    """
    메인페이지에서 포스트를 받았을 때의 함수
    """
    password = request.POST.get('password',None)

    if not CharList.objects.filter(password=password):
        return render(request, 'wrong_char.html') #비밀번호가 틀렸을 때
    else: #비밀번호가 맞았을 때
        log = LogList() #빈 로그 오브젝트 생성
        sublog = SubLogList() #빈 서브로그 오브젝트 생성
        where = request.POST.get('where',None) #받아오지 않은 포스트값을 받아옴
        contents = request.POST.get('contents',None)
        contents = contents_replace(contents)
        char = CharList.objects.get(password=password) #캐릭터 리스트에서 패스워드와 맞는 캐릭터 불러옴
            
        log_plus(char) #로그 카운터 증가 함수   

        log_substitute(log,char,where,contents) #로그에 각 값 대입하는 함수
        log.sublog_count = 1
        log.save()

        log_substitute(sublog,char,where,contents) #로그와 마찬가지로 서브로그 첫번째 값에 대입
        sublog.mainlog = log.id #메인로그 넣어줌
        sublog.save()
            

        return render(request, 'redirectpage.html') #작성후 메인페이지 이동


#메인 페이지
def main_page(request):
    if request.method == 'POST':#메인 페이지에서 포스트 요청을 받았을 때
        return main_POST(request)
    else:
        loglist = LogList.objects.all().order_by('-id')[:10]#보드의 정렬
        subloglist = SubLogList.objects.all().order_by('-id')[:5]#보드의 정렬
        latest = []
        for latest_charname in subloglist:
            latest.append(latest_charname)
        data = {'logs':loglist, 'latest':latest, 'page':[0,1,2]}

        return render(request, 'main_page.html',{'data' : data})

def paging(request,page):
    if request.method=='POST':
        return main_POST(request)
    else:
        first = ( ( page-1 ) * 10)
        last = page*10
        loglist = LogList.objects.all().order_by('-id')[first:last]#보드의 정렬
        subloglist = SubLogList.objects.all().order_by('-id')[:5]#보드의 정렬
        latest = []
        for latest_charname in subloglist:
            latest.append(latest_charname)
        data = {'logs':loglist, 'latest':latest, 'page':[page-1,page,page+1]}

        return render(request, 'main_page.html',{'data' : data})

def choose_paging(request):
    page = request.GET.get('page',None)
    return redirect('/home/main/'+page)
    

#상세를 눌렀을 때 로그 개별 창이 나오게 한다
def log_detail(request, lg):
    if not SubLogList.objects.filter(mainlog=lg):
        return render(request, 'wrong_char.html')
    subloglist = SubLogList.objects.filter(mainlog=lg).order_by('id')

    if request.method == 'POST':#로그디테일 페이지에서 포스트요청
        password = request.POST.get('password',None)#포스트요청에서 비밀번호를 받아옴

        if not CharList.objects.filter(password=password):
            return render(request, 'wrong_char.html') #비밀번호가 틀렸을 때
        else:#비밀번호가 맞았을 때 이번엔 서브로그만 추가해야함!
            sublog = SubLogList() #빈 서브로그 생성

            mainlg = LogList.objects.get(id=lg)
            mainlg.sublog_count += 1
            mainlg.save()

            char = CharList.objects.get(password=password) #캐릭터 리스트에서 패스워드와 맞는 캐릭터 불러옴
            where = request.POST.get('where',None) #받아오지 않은 포스트값을 받아옴
            contents = request.POST.get('contents',None)
            contents = contents_replace(contents)

            log_plus(char)
            
            log_substitute(sublog,char,where,contents) #로그와 마찬가지로 서브로그 첫번째 값에 대입
            sublog.mainlog = lg #메인로그 넣어줌
            sublog.save()

            
            
            return render(request, 'log_detail.html',{'logs':subloglist})

    else:
    
        return render(request, 'log_detail.html',{'logs': subloglist})


def log_confirm(request,lg):
    if not SubLogList.objects.filter(id=lg):
        return render(request, 'wrong_char.html')
    sublog = SubLogList.objects.get(id=lg)
    if request.method == "POST":
        password = request.POST.get('password',None)
        if password != sublog.password:#비밀번호가 틀릴때
            return render(request, 'wrong_char.html')
        else:
            return render(request, 'log_modify.html', {'log':sublog})
    else:
        return render (request, 'password_confirm.html',{'log':sublog})

def log_modify(request,lg):
    if not SubLogList.objects.filter(id=lg):
        return render(request, 'wrong_char.html')
    if request.method == "POST":
        sublog = SubLogList.objects.get(id=lg)#고칠 서브로그를 불러와서 수정!!
        password = request.POST.get('password',None)
        if not CharList.objects.filter(password=password):
            return render(request, 'wrong_char.html') #비밀번호가 틀렸을 때

        
        #메인로그도 고쳐야하는지 판별하기 위해 메인로그도 불러온다
        if sublog == SubLogList.objects.filter(mainlog=sublog.mainlog).order_by('id')[0]:
            #서브로그리스트를 차례대로 정렬한 것의 제일 첫번째와 서브로그가 일치하는 경우 메인로그도 고쳐야 한다
            
            log = LogList.objects.get(id=sublog.mainlog)
            log.password = password
            log.where = request.POST.get('where',None)
            log.contents = request.POST.get('contents',None)
            log.contents = contents_replace(log.contents)
            log.charcon = CharList.objects.get(password=password).charcon
            log.save()

        sublog.password = password
        sublog.where = request.POST.get('where',None)
        sublog.contents = request.POST.get('contents',None)
        sublog.contents = contents_replace(sublog.contents)
        sublog.charcon = CharList.objects.get(password=password).charcon
        sublog.save()
        #수정후 저장을 마치고
        subloglist = SubLogList.objects.filter(mainlog=sublog.mainlog).order_by('id')
        return render(request, 'log_detail.html',{'logs':subloglist})

    else:
        return render(request, 'wrong_char.html')

def log_delete(request,lg):
    if not SubLogList.objects.filter(id=lg):
        return render(request, 'wrong_char.html')
    sublog = SubLogList.objects.get(id=lg)
    if request.method == "POST":
        password = request.POST.get('password',None)
        if password != sublog.password:#비밀번호가 틀릴때
            return render(request, 'wrong_char.html')
        else:
            if sublog == SubLogList.objects.filter(mainlog=sublog.mainlog).order_by('id')[0]:
                #서브로그리스트를 차례대로 정렬한 것의 제일 첫번째와 서브로그가 일치하는 경우 메인로그도 삭제 해야 한다
                log = LogList.objects.get(id=sublog.mainlog)
                log.delete()
                #그 경우 남아 있는 서브로그도 일괄 삭제한다
                subloglist = SubLogList.objects.filter(mainlog=sublog.mainlog).order_by('id')
                for subl in subloglist:
                    char = CharList.objects.get(password=subl.password)
                    log_minus(char)
                    subl.delete()

            else:
                mainlg = LogList.objects.get(id=sublog.mainlog)
                mainlg.sublog_count -= 1
                mainlg.save()
                
                char = CharList.objects.get(password=sublog.password)
                log_minus(char)
                sublog.delete()


            loglist = LogList.objects.all().order_by('-id')[:10]#보드의 정렬
            data = {'logs':loglist}

            return render(request, 'main_page.html',{'data' : data})
            

    else:
        return render (request, 'delete_confirm.html',{'log':sublog})

def char_ranking(request):

    ranking = charanking.objects.all().order_by('-logcount')
    return render(request, 'char_ranking.html',{"rank":ranking})

