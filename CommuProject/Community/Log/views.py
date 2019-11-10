from django.shortcuts import render, redirect
from .models import LogList
from Char.models import CharList
from sub_log.models import SubLogList
from charanking.models import charanking

from datetime import datetime

import random

# Create your views here.
#가챠 시스템 구현
def dice(request):
    return render(request,'gatya.html')
def gatya(request):

    mang = random.randrange(1,201)
    if mang<=1:
        img ='/static/img/t3982819189.png'
        speak ='<i>"이걸로 괜찮아요? 정말요?"<br>"네~ 물론이죠~"<br>"풉"<br>"첫번째가 웃었어!?"</i>'
        effect ='<b><big>매력 능력치 +30</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    elif mang>1 and mang<=3:
        img = '/static/img/t187489119771.png'
        speak ='<i>"상냥한 사람."<br>"당신과 함께하다간 저도 그렇게 되겠죠."<br>"그러니까, 이별이에요."</i>'
        effect ='<b><big>의지 능력치 +30</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    elif mang>2 and mang<=7:
        img = '/static/img/t9325817786767.jpg'
        speak ='<i>몹시 느긋한 수영으로 보이지만<br>사실은 상어로부터 도망치고 있다</i>'
        effect ='<b><big>민첩 능력치 +30</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    elif mang>7 and mang<=17:
        img = '/static/img/t12418186593.jpg'
        speak ='<i>.......</i>'
        effect ='<b><big>근력 능력치 +5</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    elif mang>17 and mang<=27:
        img = '/static/img/t18293685629.jpg'
        speak ='<i>즐거우신가요~?</i>'
        effect ='<b><big>의지 능력치 +5</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    elif mang>27 and mang<=32:
        img = '/static/img/t121891281928.jpg'
        speak ='<i>진짜! 잠깐 사이에 그리셨다니까요?!</i>'
        effect ='<b><big>매력 능력치 +5</big></b>'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})
    else:
        img = 0
        speak ='<i>"괜찮아요?"<i>'
        effect ='아무 일도 일어나지 않았습니다'
        data = {'img':img,'speak':speak,'effect':effect}
        return render(request,'gatyaVSSR.html',{'data':data})



#Bool return
def Password_not_in_CharList(password):
    """
    Password가 CharList에 존재하는지 확인
    없을 경우 True가 반환된다
    """
    if not CharList.objects.filter(password=password):
        return True
    else:
        return False
def Mainlog_not_in_SubLogList(MainLog_id):
    """
    Mainlog가 SubLogList에 존재하는지 확인
    없을 경우 True가 반환된다
    """
    if not SubLogList.objects.filter(mainlog=MainLog_id):
        return True
    else:
        return False
def Sublog_not_in_SubLogList(SubLog_id):
    """
    Mainlog가 SubLogList에 존재하는지 확인
    없을 경우 True가 반환된다
    """
    if not SubLogList.objects.filter(id=SubLog_id):
        return True
    else:
        return False
def modify_password_not_match(request,lg,sublog):
    """
    수정할 때 암호가 맞는지 확인하는 함수
    틀릴 경우 True이다.
    """
    password = request.POST.get('password',None)
    if password != sublog.password:
        return True
    else:
        return False

#오류 났을 때 이동되는 사이트
def Warning_site(request):
    return render(request, 'wrong_char.html')

#로그 수 + -
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

#신규 로그 생성 함수
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

#메인로그 저장 함수
def mainlog_save(log,char,where,contents):  
    """
    메인 로그 저장 함수
    """
    log_substitute(log,char,where,contents) #로그에 각 값 대입하는 함수
    log.sublog_count = 0
    log.save()
    return
#서브로그 저장 함수
def sublog_save(sublog,lgid,char,where,contents):
    """
    서브 로그 저장 함수
    """
    log_substitute(sublog,char,where,contents) #로그와 마찬가지로 서브로그 첫번째 값에 대입
    sublog.mainlog = lgid #메인로그 넣어줌
    sublog.save()
    return
#로그 수정 함수
def modify_save(log,password,where,request):
    log.password = password
    log.where = where
    log.contents = contents_replace(request)
    log.charcon = CharList.objects.get(password=password).charcon
    log.save()
    return
#콘텐츠 바꾸는 함수
def contents_replace(request):
    """
    폰트, 이미지 태그 치환 함수
    """
    contents = request.POST.get('contents',None)
    contents = contents.replace('{{', '<font color="green"     >')
    contents = contents.replace('}}', '</font     >')
    contents = contents.replace('[[', '<font color="red"     >')
    contents = contents.replace(']]', '</font    >')
    contents = contents.replace('((', '<font color="blue"     >')
    contents = contents.replace('))', '</font   >')
    contents = contents.replace('+++', '<     img src="')
    contents = contents.replace('---', '"></img     >"')
    contents = contents.replace('<<', '<br><br>&nbsp;<a href="/home/log/')
    contents = contents.replace('>>', '#rep"      style="text-decoration:none;padding:5px;color: rgb(136, 100, 245);border-radius: 8px;border: 1px solid #E0E0F8;"><b>로그 이동</b></a><br><br>')

    return contents
def contents_re_replace(contents):
    """
    폰트, 이미지 태그 재치환 함수
    """
    contents = contents.replace('<font color="green"     >','{{')
    contents = contents.replace('</font     >','}}')
    contents = contents.replace( '<font color="red"     >', '[[')
    contents = contents.replace('</font    >', ']]')
    contents = contents.replace('<font color="blue"     >','((')
    contents = contents.replace( '</font   >','))')
    contents = contents.replace('<     img src="','+++')
    contents = contents.replace( '"></img     >"','---')
    contents = contents.replace( '<br><br>&nbsp;<a href="/home/log/','<<')
    contents = contents.replace( '#rep"      style="text-decoration:none;padding:5px;color: rgb(136, 100, 245);border-radius: 8px;border: 1px solid #E0E0F8;"><b>로그 이동</b></a><br><br>','>>')

    return contents
#메인페이지로 이동
def move_mainpage():
    """
    메인 페이지로 리다이렉트할 때 쓰는 함수
    """
    return redirect('/home/main/')
#상세페이지로 이동(메인로그 id를 통해)
def move_detailpage(lg):
    """
    로그 개별 상세 페이지로 이동하는 함수
    """
    return redirect('/home/log/'+str(lg) +'#rep',)
#최접 불러오는 거
def latest_char():
    """
    최근 접속자 목록을 넘겨주는 함수
    """
    subloglist = SubLogList.objects.all().order_by('-id')[:10]#보드의 정렬
    latest = []
    latest_charname = []
    for latest_sublog in subloglist:
        if latest_sublog.charname not in latest_charname:
            

            write_time = datetime.today().minute - latest_sublog.write_dttm.minute
            if write_time < 0 and (datetime.today().hour -latest_sublog.write_dttm.hour ==1 and  datetime.today().day == latest_sublog.write_dttm.day and datetime.today().month == latest_sublog.write_dttm.month and datetime.today().year == latest_sublog.write_dttm.year):
                write_time += 60
            if write_time <= 5 and write_time>=0 : #차가 5분 이하일 경우
                latest.append(latest_sublog.charname+" "+str(write_time)+"분")
                latest_charname.append(latest_sublog.charname)


    return latest  
#session latest 값에 따라 최접 불러올지 그냥 리턴할지 결정하는 함수
def latest_char_db(choijeob):
    if choijeob=='on':#최접불러오기 설정이 되어 있을 때 최근 접속자 데이터 불러오기 
        return latest_char()
    else:
        return None

#session에 password와 where 저장하는 함수
def session_save_WP(where,password,request):
    """
    session에 비밀번호, 웨어 저장하는 함수
    """
    request.session['password'] = password
    request.session['where'] = where
    return
#메인_포스트
def main_POST(request):
    """
    메인 페이지에서 POST 데이터를 받았을 때의 함수
    """
    password = request.POST.get('password',None)
    where = request.POST.get('where',None)
    session_save_WP(where,password,request)
    if Password_not_in_CharList(password):
        return Warning_site(request)
    else: #비밀번호가 맞았을 때
        
        #contents를 받아오는 것을 저장과 따로 하는 이유는 저장 전에 중복 로그인지 테스트하기 위해서
        contents = contents_replace(request)

        jungbok_test_log = LogList.objects.filter(password=password)#조금이라도 트래픽을 줄이기 위해 함수로 합치지 않았다!
        for log in jungbok_test_log:
            if contents == log.contents:
                return Warning_site(request)

        log = LogList() #빈 로그 오브젝트 생성
        sublog = SubLogList() #빈 서브로그 오브젝트 생성

        char = CharList.objects.get(password=password) #캐릭터 리스트에서 패스워드와 맞는 캐릭터 불러옴

        log_plus(char) #로그 카운터 증가 함수  

        mainlog_save(log,char,where,contents) #메인로그 저장 함수
        sublog_save(sublog,log.id,char,where,contents) #서브로그 저장 함수

        return move_mainpage() #작성후 메인페이지 이동
def detail_POST(request,lg):
    """
    로그 상세 페이지에서 포스트 전송을 받았을 때 구동되는 함수
    """
    password = request.POST.get('password',None)
    where = request.POST.get('where',None)
    session_save_WP(where,password,request)
    if Password_not_in_CharList(password):
        return Warning_site(request)
    else:
        sublog = SubLogList() #빈 서브로그 생성
        sublog_count_plus(lg) #메인로그의 서브로그카운터 증가시키는 함수
        
        char = CharList.objects.get(password=password) #캐릭터 리스트에서 패스워드와 맞는 캐릭터 불러옴
        
        contents = contents_replace(request)

        jungbok_test_log = SubLogList.objects.filter(mainlog=lg)#트래픽을 줄이기위해 일부러 함수로 빼지 않았다!
        for log in jungbok_test_log:
            if contents == log.contents:
                return Warning_site(request)

        log_plus(char)
        sublog_save(sublog,lg,char,where,contents)

        if request.session.get('main_type',None) == 'old':
            return move_mainpage()

        return move_detailpage(lg)


#다음 페이지가 존재하는지 확인하는 함수
def nextpage_False(loglist,t):  
    """
    다음 페이지가 있는지 확인하는 함수
    """
    try:
        loglist[t]
    except IndexError:
        return 'F'
    return 'T'
#펴기모드에서 쓰이는 데이터 불러오는 함수
def loglist_old(loglist):
    """
    세션에 저장된 것이 펴기 모드일 때 데이터 불러오는 함수
    """
    subloglist_list = [] #서브로그리스트의 리스트를 딕셔너리로 넘겨주기 위해 배열 선언
    for i in loglist[0:10]:#로그리스트에 들어 있는 '메인로그'들을 하나씩 가져온다
        subloglist = SubLogList.objects.filter(mainlog=i.id).order_by('id')#메인로그의 id값으로 서브로그 목록을 찾아내어 리스트로 끌고 온다
        subloglist_list.append(subloglist)#subloglist_list에 append
    return subloglist_list


def main_GET_data(request,page):
    """
    메인 페이지, 일반적으로 접속했을 때 넘겨 주어야 할 데이터를 수집, 리턴하는 함수
    """
    password = request.session.get('password',"")
    where = request.session.get('where',"")

    loglist = LogList.objects.all().order_by('-id')[(page-1)*10:page*10+1]#보드의 정렬
    nextpage = nextpage_False(loglist,10)

    choijeob = request.session.get('latest',None)#최근 접속자 온오프 변수
    latest = latest_char_db(choijeob)
    
    main_type = request.session.get('main_type',None)#old인지 확인하기 위해 메인 타입을 불러온다
    if main_type == 'old':#메인타입이 올드일 경우
        subloglist_list = loglist_old(loglist)
        
        return {'logs':subloglist_list, 'latest':latest,'page':[page-1,page,page+1], 'next':nextpage,'main_type':main_type, 'choijeob':choijeob, 'where':where,'password':password}

    return {'logs':loglist[0:10], 'latest':latest,'page':[page-1,page,page+1], 'next':nextpage,'main_tpye':main_type, 'choijeob':choijeob, 'where':where,'password':password}
def detail_GET_data(request,lg):
    """
    디테일 데이터 리턴하는 함수
    """
    subloglist = SubLogList.objects.filter(mainlog=lg).order_by('id')
    password = request.session.get('password',"")
    where = request.session.get('where',"")
    return {'logs': subloglist,'password':password,'where':where}


def sublog_count_plus(lg):
    """
    메인로그의 sublog_count를 하나 추가하는 함수
    """
    mainlg = LogList.objects.get(id=lg)
    mainlg.sublog_count += 1
    mainlg.save()
    return
#메인 페이지
def main_page(request,page=1):
    """
    / , /home/ , /home/main/ , /home/main/<int:page> 일때 실행되는 함수
    """
    if request.method == 'POST':#메인 페이지에서 포스트 요청을 받았을 때
        return main_POST(request)
    else:
        data = main_GET_data(request,page)
        return render(request, 'main_page.html',{'data' : data})
def choose_paging(request):
    """
    main_page.html에서 원하는 페이지를 검색할 때 실행되는 함수
    일반적으로 GET type으로 <int:page>가 전송된다
    """
    page = request.GET.get('page',None)
    return redirect('/home/main/'+page)
#상세 페이지
def log_detail(request, lg):
    """
    /home/log/<int:lg> 일때 실행되는 함수
    """
    if Mainlog_not_in_SubLogList(lg):
        return Warning_site(request)

    if request.method == 'POST':
        return detail_POST(request,lg)
    else:
        data = detail_GET_data(request,lg)
        return render(request, 'log_detail.html',{'data': data})
#수정 페이지
def log_confirm(request,lg):
    """
    로그를 수정하려고 할 때, 비밀번호 확인하는 함수
    """
    if Sublog_not_in_SubLogList(lg):#잘못된 로그 주소로 접속했을 때 오류를 띄운다
        return Warning_site(request)

    if request.method == "POST":
        
        sublog = SubLogList.objects.get(id=lg)
        
        if modify_password_not_match(request,lg,sublog):#비밀번호가 틀릴때    
            return Warning_site
        else:
            sublog.contents = contents_re_replace(sublog.contents)#치환했던 콘텐츠를 되돌려 사용자가 알아보기 쉽도록한다
            where = request.session.get('where',"")
            password = request.session.get('password',"")
            data = {'log':sublog,'where':where,'password':password}
            return render(request, 'log_modify.html', {'data':data})
    else:

        sublog = SubLogList.objects.get(id=lg)
        return render (request, 'password_confirm.html',{'log':sublog})
def log_modify(request,lg):
    """
    수정 자체를 진행한 후 디테일 페이지로 이동하는 함수
    """
    if Sublog_not_in_SubLogList(lg):#잘못된 로그 주소로 접속했을 때 오류를 띄운다
        return Warning_site(request)

    if request.method == "POST":
        sublog = SubLogList.objects.get(id=lg)#고칠 서브로그를 불러와서 수정!!
        password = request.POST.get('password',None)
        where = request.POST.get('where',None)
        if Password_not_in_CharList(password):
            return Warning_site(reqeust) #비밀번호가 틀렸을 때

        #메인로그도 고쳐야하는지 판별하기 위해 메인로그도 불러온다
        if sublog == SubLogList.objects.filter(mainlog=sublog.mainlog).order_by('id')[0]:
            #서브로그리스트를 차례대로 정렬한 것의 제일 첫번째와 서브로그가 일치하는 경우 메인로그도 고쳐야 한다
            
            log = LogList.objects.get(id=sublog.mainlog)
            modify_save(log,password,where,request)

        modify_save(sublog,password,where,request)
        #수정후 저장을 마치고
        if request.session.get('main_type') == 'old':
            return move_mainpage()
        return move_detailpage(sublog.mainlog)

    else:
        return Warning_site(request)
#삭제 페이지
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

            return move_mainpage()
            

    else:
        return render (request, 'delete_confirm.html',{'log':sublog})

def char_ranking(request):

    ranking = charanking.objects.all().order_by('-logcount')
    return render(request, 'char_ranking.html',{"rank":ranking})
def search_choose_paging(request):
    """
    검색화면에서 원하는 페이지 검색할 때 실행되는 함수
    일반적으로 GET type으로 <int:page>가 전송된다?
    """
    page = request.GET.get('page',None)
    search_word = request.GET.get('search_word',None)
    return redirect('/home/search/'+page+'?search_word='+search_word)

def log_search(request,page=1):
    search_word = request.GET.get('search_word',None)
    search_list = search_word.split(" ")
    all_subloglist = SubLogList.objects.all().order_by('-id')
    ori_search_result = []
    log_id = ""
    first_charname = search_list[0]
    for sublog in all_subloglist:
            
        if sublog.mainlog != log_id and sublog.charname == first_charname:
            ori_search_result.append(sublog.mainlog)
            log_id = sublog.mainlog
            #이전 메인로그와 현재 메인로그가 같지 않을 때만 charname으로 필터링한 mainlog 결과를 search_result에 push
    #for문의 결과로 charname로 검색한 sublog의 mainlog들이 나옴
    del all_subloglist
    search_result = []
    
    for charname in search_list[1:]:
        for mainlg in ori_search_result:
            search_in_mainlog = SubLogList.objects.filter(mainlog=mainlg)#메인로그에 있는 sublog를 다불러온다
            for sublog in search_in_mainlog:#그 불러온 서브로그 중에 charname이 존재하는게 있을 경우
                if sublog.charname==charname:
                    search_result.append(mainlg)#메인로그를 search_result에 푸시한다
                    break#그리고 브레이크
        for var in ori_search_result[0:]:
            if var not in search_result:#search result에 없는 경우 모두 삭제
                ori_search_result.remove(var)
        
        search_result.clear()
    loglist = []
    first_log = last_log = 0
    if (page-1)*10 > len(ori_search_result):#검색 결과 페이지가 존재할 수 없을 때
        return Warning_site
    else :
        first_log = (page-1)*10
    if page*10 > len(ori_search_result): 
        last_log=len(ori_search_result)
    else:
        last_log = page*10

    for mainlg in ori_search_result[first_log:last_log]:#범위 밖이라고 오류날것 같은데?
        log = LogList.objects.get(id=mainlg)
        loglist.append(log)

    nextpage = nextpage_False(ori_search_result,last_log)
    main_type = request.session.get('main_type',None)
    choijeob = request.session.get('latest',None)
    latest = latest_char_db(choijeob)
    where = request.session.get('where',None)
    password = request.session.get('password',None)


    if main_type == 'old':#메인타입이 올드일 경우
        subloglist_list = loglist_old(loglist)
        data = {'logs':subloglist_list, 'latest':latest,'page':[page-1,page,page+1], 'search_word':search_word, 'next':nextpage, 'main_type':main_type, 'choijeob':choijeob, 'where':where,'password':password }

    else:
        data = {'logs':loglist, 'latest':latest,'page':[page-1,page,page+1], 'search_word':search_word, 'next':nextpage, 'main_type':main_type, 'choijeob':choijeob, 'where':where,'password':password }


    return render(request, 'search_page.html',{'data' : data})
#구버전 세션 저장용
def change_version(request,vers):
    """
    main_page.html에서 원하는 페이지를 검색할 때 실행되는 함수
    일반적으로 GET type으로 <int:page>가 전송된다
    """
    if vers == 0:
        request.session['main_type'] = 'young'
    elif vers == 1:
        request.session['main_type'] = 'old'
    elif vers == 2:
        request.session['latest'] = 'on'
    elif vers==3:
        request.session['latest'] = 'off'
        
    elif vers == 4:
        request.session['world'] = 'on'
    elif vers==5:
        request.session['world'] = 'off'
    return redirect('/home/main/')

def save_log(request,page=1):
    """
    현재 페이지에 표시된 로그들을 저장하는 함수
    """
    main_type = request.session.get('main_type',"")
    if main_type != 'old':
        return Warning_site(request)#old 버전, 펴기 모드에서만 지원 가능하게 설정
    else:
        data = main_GET_data(request,page)
        return render(request, 'save_log.html',{'data' : data})

def save_detail_log(request, lg):
    """
    /home/log/<int:lg> 일때 실행되는 함수
    """
    if Mainlog_not_in_SubLogList(lg):
        return Warning_site(request)
    else:
        data = detail_GET_data(request,lg)
        return render(request, 'save_detail_log.html',{'data': data})


def world(request,page=1):
    """
    weight 페이지로 이동하는 함수
    """
    world_page = 'weight' + str(page) +'.html'
    world = request.session.get('world','on')
    return render(request,world_page,{'data':world})