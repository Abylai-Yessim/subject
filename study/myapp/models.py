from django.db import models
from django.conf import settings


# Модель языка
class Language(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Модель алфавита
class Alphabet(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    letters = models.TextField()  # Список букв алфавита, например, "А,Ә,Б,В,..."

    def __str__(self):
        return self.language.name


# Модель слова
class Word(models.Model):
    chapter = models.IntegerField()
    languages = models.ManyToManyField(Language, through='WordTranslation')

    def __str__(self):
        return f"Chapter {self.chapter}"

# Промежуточная модель для хранения текста слова на каждом языке
class WordTranslation(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.language}: {self.topic}"

# Модель темы
class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Модель урока
class Lesson(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, through='LessonTranslation')

    def __str__(self):
        return f"Lesson on {self.topic}"

# Промежуточная модель для хранения текста урока на каждом языке
class LessonTranslation(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.language}: {self.content}"


class LessonLesson(models.Model):
    title_kz = models.CharField(max_length=100, verbose_name='Заголовок на казахском')
    title_ru = models.CharField(max_length=100, verbose_name='Заголовок на русском')
    title_en = models.CharField(max_length=100, verbose_name='Заголовок на английском')
    sub_title_kz = models.CharField(max_length=100, verbose_name='Подзаголовок на казахском')
    sub_title_ru = models.CharField(max_length=100, verbose_name='Подзаголовок на русском')
    sub_title_en = models.CharField(max_length=100, verbose_name='Подзаголовок на английском')
    description_kz = models.TextField(verbose_name='Описание на казахском')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_en = models.TextField(verbose_name='Описание на английском')
    image = models.ImageField(upload_to='lessons', verbose_name='Изображение')
    audio_kz = models.FileField(upload_to='audio', verbose_name='Аудио на казахском')
    audio_ru = models.FileField(upload_to='audio', verbose_name='Аудио на русском')
    audio_en = models.FileField(upload_to='audio', verbose_name='Аудио на английском')

    @property
    def audio_kz_url(self):
        return settings.MEDIA_URL + str(self.audio_kz)

    @property
    def audio_ru_url(self):
        return settings.MEDIA_URL + str(self.audio_ru)

    @property
    def audio_en_url(self):
        return settings.MEDIA_URL + str(self.audio_en)

    def __str__(self):
        return self.title_kz
