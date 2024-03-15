from django.db import models

# Create your models here.


from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Position(models.Model):
    id = models.AutoField(primary_key=True)  # 主键，自增
    name = models.CharField(max_length=255, verbose_name='岗位名称')  # 岗位名称, 字符串
    job_type = models.CharField(max_length=100, verbose_name='职位类型')  # 职位类型, 字符串
    work_location = models.CharField(max_length=255, verbose_name='工作地点')  # 工作地点, 字符串python manage.py makemigrations
    post_time = models.DateTimeField(verbose_name='发布时间')  # 发布时间, 日期时间
    responsibility = models.TextField(verbose_name='岗位职责')  # 岗位职责, 文本
    requirement = models.TextField(verbose_name='任职要求')  # 任职要求, 文本
    class Meta:
        verbose_name = '岗位'  # 单数形式的模型名称
        verbose_name_plural = '岗位'  # 复数形式的模型名称，如果不设置，Django会自动 在单数名称后加上's'
    def __str__(self):
        return self.name  # 返回岗位名称作为对象的字符串表示



class QuestionCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='问题标题')
    class Meta:
        verbose_name = '问题标题'  # 单数形式的模型名称
        verbose_name_plural = '问题标题'  # 复数形式的模型名称，如果不设置，Django会自动 在单数名称后加上's'

    def __str__(self):
        return self.title
class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=255, verbose_name='问题名称')
    class Meta:
        verbose_name = '问题名称'  # 单数形式的模型名称
        verbose_name_plural = '问题名称'  # 复数形式的模型名称，如果不设置，Django会自动 在单数名称后加上's'
    def __str__(self):
        return self.name
class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    text = models.TextField(verbose_name='回答')
    class Meta:
        verbose_name = '回答'  # 单数形式的模型名称
        verbose_name_plural = '回答'  # 复数形式的模型名称，如果不设置，Django会自动 在单数名称后加上's'
    def __str__(self):
        return f"Answer to {self.question.name}"