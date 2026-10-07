from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'Pollster Administration'
admin.site.site_title = 'Pollster Admin'
admin.site.index_title = 'Manage Polls and Choices'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')
    list_filter = ('question',)
