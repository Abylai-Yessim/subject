from django.shortcuts import render, get_object_or_404
from .models import *
# from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

# Create your views here.

menu = [
    {'title': 'Trilingo'},
]

def home(request):
    data = {
   
        'title': 'Главная страница',
    }
    return render(request, 'myapp/home.html', context=data)

def search_results(request):
    query = request.GET.get('query')
    return render(request, 'myapp/home.html', {'query': query})

def three(request):
    lessons = LessonLesson.objects.all()
    data = {
        'title': 'Главная страница',
        'lessons': lessons,
    }
    return render(request, 'myapp/three.html', context=data)


def subject(request):
    selected_language_name = request.GET.get('lang', '')
    selected_letter = request.GET.get('letter', '')

    languages = Language.objects.all()

    if selected_language_name:
        try:
            selected_language = Language.objects.get(name=selected_language_name)
            alphabet = get_alphabet(selected_language)
            if selected_letter:
                words = Word.objects.prefetch_related('wordtranslation_set').filter(
                    wordtranslation__language__name=selected_language_name,
                    chapter__istartswith=selected_letter
                )
            else:
                words = Word.objects.prefetch_related('wordtranslation_set').filter(
                    wordtranslation__language__name=selected_language_name
                )
        except Language.DoesNotExist:
            selected_language = ''
            alphabet = []
            words = Word.objects.prefetch_related('wordtranslation_set').all()
    else:
        selected_language = ''
        alphabet = []
        words = Word.objects.prefetch_related('wordtranslation_set').all()

    return render(request, 'myapp/subject.html', {'languages': languages, 'words': words, 'selected_language': selected_language, 'alphabet': alphabet})

def get_alphabet(language):
    try:
        alphabet_obj = Alphabet.objects.get(language=language)
        alphabet = alphabet_obj.letters.split(',') if alphabet_obj else []
    except Alphabet.DoesNotExist:
        alphabet = []

    return alphabet



def search_subject(request):
    search_query = request.GET.get('sub_query')
    if search_query:
        pos = WordTranslation.objects.filter(Q(word__chapter__icontains=search_query) | Q(topic__icontains=search_query))
    else:
        pos = WordTranslation.objects.all()

    return render(request, 'myapp/subject.html', {'words': pos, 'query': search_query})




def four_subject(request):
    selected_language_name = request.GET.get('lang', '')

    languages = Language.objects.all()

    if selected_language_name:
        try:
            selected_language = Language.objects.get(name=selected_language_name)
            alphabet = get_alphabet(selected_language)
            lessons = Lesson.objects.prefetch_related('lessontranslation_set').filter(lessontranslation__language__name=selected_language_name)
        except Language.DoesNotExist:
            selected_language = ''
            alphabet = []
            lessons = Lesson.objects.prefetch_related('lessontranslation_set').all()
    else:
        selected_language = ''
        alphabet = []
        lessons = Lesson.objects.prefetch_related('lessontranslation_set').all()

    return render(request, 'myapp/four.html', {'languages': languages, 'lessons': lessons, 'selected_language': selected_language, 'alphabet': alphabet})
