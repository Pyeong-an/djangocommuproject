from django.db import models

# Create your models here.
class CharList(models.Model):
    charname =  models.CharField(max_length=64,verbose_name='캐릭터 이름')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    logcount = models.CharField(max_length=64,verbose_name='로그 수')
    charcon0 = models.CharField(max_length=256,verbose_name='콘 0')
    charcon1 = models.CharField(max_length=256,verbose_name='콘 1')
    charcon2 = models.CharField(max_length=256,verbose_name='콘 2')
    charcon3 = models.CharField(max_length=256,verbose_name='콘 3')
    charcon4 = models.CharField(max_length=256,verbose_name='콘 4')
    charcon5 = models.CharField(max_length=256,verbose_name='콘 5')
    charcon6 = models.CharField(max_length=256,verbose_name='콘 6')
    charcon7 = models.CharField(max_length=256,verbose_name='콘 7')
    charcon8 = models.CharField(max_length=256,verbose_name='콘 8')
    charcon9 = models.CharField(max_length=256,verbose_name='콘 9')

    def __str__(self):
        return self.charname

    class Meta:
        db_table = 'Charlist'
        verbose_name = '캐릭터 목록'
        verbose_name_plural = '캐릭터 목록'


    