from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Вывод определенный полей в определенном порядке
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

# Группировка полей
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'create_date')
    fieldsets = [
        ('Инфа по вопросу', {'fields':['question_text']}),
        ('Инофрмация дополнительная', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)


