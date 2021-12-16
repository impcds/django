from django.contrib import admin
from .models import Question, Choice


class ListandoQuestion(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date', )
    list_display_links = ('id', 'question_text', )


class ListandoChoice(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    list_display_links = ('id', 'choice_text')


admin.site.register(Question, ListandoQuestion)
admin.site.register(Choice, ListandoChoice)
