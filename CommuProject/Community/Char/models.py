from django.db import models

# Create your models here.
class CharList(models.Model):
    charname =  models.CharField(max_length=64,verbose_name='캐릭터 이름')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    logcount = models.CharField(max_length=64,verbose_name='로그 수')
    charcon = models.CharField(max_length=256,verbose_name='콘')

    def __str__(self):
        return self.charname

    class Meta:
        db_table = 'Charlist'
        verbose_name = '캐릭터 목록'
        verbose_name_plural = '캐릭터 목록'


    