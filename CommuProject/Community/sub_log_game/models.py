from django.db import models

# Create your models here.
class SubLogList_game(models.Model):
    mainlog = models.CharField(max_length=64, verbose_name='상위 로그')
    charname =  models.CharField(max_length=64, verbose_name='캐릭터 이름')
    where =  models.CharField(max_length=64,verbose_name='장소')
    charcon =  models.CharField(max_length=64,verbose_name='콘')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    contents = models.TextField(verbose_name='내용')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')

    def __str__(self):
        return self.charname

    class Meta:
        db_table = "SubLogList_game"
        verbose_name = verbose_name_plural = '서브 로그_game'