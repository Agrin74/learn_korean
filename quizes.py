import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_korean.settings')
django.setup()

from lessons.models import GrammarQuiz 

questions = [
    {
        "question_text": "What does the verb ending '이다' mean in Korean?",
        "option1": "to have",
        "option2": "to be",
        "option3": "to go",
        "option4": "to want",
        "correct_answer": "to be"
    },
    {
        "question_text": "Which word means 'to want' in Korean?",
        "option1": "가다",
        "option2": "먹다",
        "option3": "원하다",
        "option4": "있다",
        "correct_answer": "원하다"
    },
    {
        "question_text": "How do you say 'can do' or 'able to' in Korean?",
        "option1": "-(으)ㄹ 수 있다",
        "option2": "-고 있다",
        "option3": "-지 않다",
        "option4": "-아서",
        "correct_answer": "-(으)ㄹ 수 있다"
    },
    {
        "question_text": "Which ending is used for past tense in Korean?",
        "option1": "-았/었-",
        "option2": "-겠-",
        "option3": "-(으)ㄹ 것이다",
        "option4": "-고 있다",
        "correct_answer": "-았/었-"
    },
    {
        "question_text": "Which ending expresses future tense in Korean?",
        "option1": "-았/었-",
        "option2": "-겠-",
        "option3": "-고 있다",
        "option4": "-지 않다",
        "correct_answer": "-겠-"
    },
    {
        "question_text": "What does '-고 싶다' mean?",
        "option1": "don’t want to",
        "option2": "want to",
        "option3": "can do",
        "option4": "must do",
        "correct_answer": "want to"
    },
    {
        "question_text": "What is the negative form of a verb in Korean?",
        "option1": "-지 않다",
        "option2": "-고 있다",
        "option3": "-아서",
        "option4": "-려고 하다",
        "correct_answer": "-지 않다"
    },
    {
        "question_text": "Which structure is used to say 'must do' or 'should do'?",
        "option1": "-아/어야 하다",
        "option2": "-(으)ㄹ 수 있다",
        "option3": "-지 않다",
        "option4": "-아서",
        "correct_answer": "-아/어야 하다"
    },
    {
        "question_text": "How do you say 'because' or 'so' in Korean grammar?",
        "option1": "-아서/어서",
        "option2": "-고 있다",
        "option3": "-지만",
        "option4": "-면",
        "correct_answer": "-아서/어서"
    },
    {
        "question_text": "Which particle is used for comparison (like 'than')?",
        "option1": "보다",
        "option2": "에서",
        "option3": "까지",
        "option4": "에게",
        "correct_answer": "보다"
    },
]

for q in questions:
    GrammarQuiz.objects.get_or_create(**q)

print("✅ Grammar quiz questions added successfully!")
