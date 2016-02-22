#aqui es donde se registran los modelos los cuales seran mostrados en el panel de django
from django.contrib import admin
#importanto los modelos desde el archivo models.py de la clase Question
from .models import Question
from .models import Choice
#StackedInline es otra forma de mostrar los datos
#TabularInline es otra forma de mostrar los datos
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('usuario',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)