# Generated by Django 5.0.1 on 2024-02-27 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='岗位名称')),
                ('job_type', models.CharField(max_length=100, verbose_name='职位类型')),
                ('work_location', models.CharField(max_length=255, verbose_name='工作地点')),
                ('post_time', models.DateTimeField(verbose_name='发布时间')),
                ('responsibility', models.TextField(verbose_name='岗位职责')),
                ('requirement', models.TextField(verbose_name='任职要求')),
            ],
            options={
                'verbose_name': '岗位',
                'verbose_name_plural': '岗位',
            },
        ),
    ]
