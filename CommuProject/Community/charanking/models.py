from django.db import models

# Create your models here.
class charanking(models.Model):
    charname =  models.CharField(max_length=64,verbose_name='캐릭터 이름')
    logcount = models.IntegerField(verbose_name='로그 수')

    def __str__(self):
        return self.charname

    class Meta:
        db_table = 'Charanking'
        verbose_name = '캐릭터 순위'
        verbose_name_plural = '캐릭터 순위'


    