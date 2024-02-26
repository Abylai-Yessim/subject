from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass

@admin.register(WordTranslation)
class WordTranslationAdmin(admin.ModelAdmin):
    pass

@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    list_display = ('language',)
    
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass

@admin.register(LessonTranslation)
class LessonTranslationAdmin(admin.ModelAdmin):
    pass

@admin.register(LessonLesson)
class LessonLessonAdmin(admin.ModelAdmin):
    pass