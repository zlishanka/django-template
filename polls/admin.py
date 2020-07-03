from django.contrib import admin

# Register your models here.
from .models import Choice, Question
#admin.site.register(Choice) 
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)