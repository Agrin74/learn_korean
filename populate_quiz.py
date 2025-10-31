import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_korean.settings')
django.setup()

from lessons.models import AlphabetQuiz

questions = [
    {"question_text": "What sound does ㄱ make?", "option1": "n", "option2": "m", "option3": "k", "option4": "s", "correct_answer": "k"},
    {"question_text": "How do you pronounce ㄴ?", "option1": "n", "option2": "r", "option3": "h", "option4": "b", "correct_answer": "n"},
    {"question_text": "What is the sound of ㄷ?", "option1": "t/d", "option2": "k", "option3": "s", "option4": "p", "correct_answer": "t/d"},
    {"question_text": "Which letter represents 'm'?", "option1": "ㅁ", "option2": "ㅂ", "option3": "ㄹ", "option4": "ㄴ", "correct_answer": "ㅁ"},
    {"question_text": "What is the sound of ㅂ?", "option1": "t", "option2": "p/b", "option3": "s", "option4": "ch", "correct_answer": "p/b"},
    {"question_text": "Which character sounds like 's'?", "option1": "ㅈ", "option2": "ㅅ", "option3": "ㅎ", "option4": "ㅊ", "correct_answer": "ㅅ"},
    {"question_text": "What is the sound of ㅇ at the end of a syllable?", "option1": "silent", "option2": "ng", "option3": "k", "option4": "t", "correct_answer": "ng"},
    {"question_text": "Which one represents 'h'?", "option1": "ㅎ", "option2": "ㅊ", "option3": "ㅋ", "option4": "ㅌ", "correct_answer": "ㅎ"},
    {"question_text": "How do you pronounce ㅊ?", "option1": "ch", "option2": "s", "option3": "j", "option4": "r", "correct_answer": "ch"},
    {"question_text": "What is the sound of ㅈ?", "option1": "ch", "option2": "j", "option3": "k", "option4": "p", "correct_answer": "j"},
]

for q in questions:
    AlphabetQuiz.objects.get_or_create(**q)

print("✅ Quiz questions added successfully!")
