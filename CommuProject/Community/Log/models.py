from django.db import models

# Create your models here.
class LogList(models.Model):
    charname =  models.CharField(max_length=64, verbose_name='캐릭터 이름')
    where =  models.CharField(max_length=64,verbose_name='장소')
    charcon =  models.CharField(max_length=64,verbose_name='콘')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    contents = models.TextField(verbose_name='내용')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')
    sublog_count = models.IntegerField(verbose_name='서브 로그 개수')

    def __str__(self):
        return self.charname

    class Meta:
        db_table = 'LogList'
        verbose_name = verbose_name_plural = '로그'