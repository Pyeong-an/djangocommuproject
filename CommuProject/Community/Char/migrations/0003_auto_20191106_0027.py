# Generated by Django 2.2.7 on 2019-11-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Char', '0002_auto_20191105_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charlist',
            name='charcon0',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon1',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon2',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon3',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon4',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon5',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon6',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon7',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon8',
        ),
        migrations.RemoveField(
            model_name='charlist',
            name='charcon9',
        ),
        migrations.AddField(
            model_name='charlist',
            name='charcon',
            field=models.CharField(default=1234, max_length=256, verbose_name='콘'),
            preserve_default=False,
        ),
    ]
