from django.contrib import admin
from .models import Alphabet,Words,Grammar,AlphabetQuiz,WordQuiz,GrammarQuiz

@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    list_display = ('korean_letter', 'meaning_fa', 'meaning_en')
    search_fields = ('korean_letter', 'meaning_fa', 'meaning_en')


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('korean_letter', 'meaning_fa', 'meaning_en')
    search_fields = ('korean_letter', 'meaning_fa', 'meaning_en')

@admin.register(Grammar)
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('korean_letter', 'meaning_fa', 'meaning_en')
    search_fields = ('korean_letter', 'meaning_fa', 'meaning_en')


admin.site.register(AlphabetQuiz)
admin.site.register(WordQuiz)
admin.site.register(GrammarQuiz)