# Generated by Django 2.2.7 on 2019-11-05 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Char', '0002_auto_20191105_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('contents', models.TextField(verbose_name='내용')),
                ('write_dttm', models.DateTimeField(auto_now_add=True, verbose_name='작성 시간')),
                ('charname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Char.CharList', verbose_name='캐릭터 이름')),
            ],
            options={
                'verbose_name': '로그',
                'verbose_name_plural': '로그',
                'db_table': 'LogList',
            },
        ),
    ]
