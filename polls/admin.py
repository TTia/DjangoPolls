from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    pass

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    list_per_page = 2
    search_fields = ['question_text']

'''
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Choice', {'fields': ['choice_text', 'votes']}),
    ]
'''

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)
