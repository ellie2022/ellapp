from django.contrib import admin
from .models import Question
from .models import Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)