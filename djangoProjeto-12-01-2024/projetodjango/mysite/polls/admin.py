# from django.contrib import admin

# from .models import Question

# admin.site.register(Question)
from django.contrib import admin
from .models import Choice, Question

# Stacked = deixa uma opção embaixo da outra 
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

# Check if the Question model is already registered
if not admin.site.is_registered(Question):
    admin.site.register(Question, QuestionAdmin)
