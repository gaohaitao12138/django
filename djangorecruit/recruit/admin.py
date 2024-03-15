from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Person, Position, QuestionCategory, Question, Answer

admin.site.register(Person)
admin.site.register(Position)
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Answer)