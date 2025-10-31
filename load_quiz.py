import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_korean.settings')
django.setup()

from lessons.models import WordQuiz

questions = [
    {
        "question_text": "What does the Korean word '음식' (eumsik) mean?",
        "option1": "Clothes",
        "option2": "Food",
        "option3": "Chair",
        "option4": "Book",
        "correct_answer": "Food",
    },
    {
        "question_text": "What does '집' (jip) mean?",
        "option1": "Mountain",
        "option2": "Sea",
        "option3": "House",
        "option4": "Bag",
        "correct_answer": "House",
    },
    {
        "question_text": "What is the meaning of '옷' (ot)?",
        "option1": "Shoe",
        "option2": "Clothes",
        "option3": "Gift",
        "option4": "Food",
        "correct_answer": "Clothes",
    },
    {
        "question_text": "What does '신발' (sinbal) mean?",
        "option1": "Hat",
        "option2": "Shoes",
        "option3": "Food",
        "option4": "Chair",
        "correct_answer": "Shoes",
    },
    {
        "question_text": "What is '선물' (seonmul)?",
        "option1": "Gift",
        "option2": "Bank",
        "option3": "Bag",
        "option4": "Food",
        "correct_answer": "Gift",
    },
    {
        "question_text": "What does '은행' (eunhaeng) mean?",
        "option1": "Restaurant",
        "option2": "Bank",
        "option3": "Mountain",
        "option4": "Sea",
        "correct_answer": "Bank",
    },
    {
        "question_text": "What does '산' (san) mean?",
        "option1": "Sea",
        "option2": "Movie",
        "option3": "Mountain",
        "option4": "Photo",
        "correct_answer": "Mountain",
    },
    {
        "question_text": "What is the English meaning of '사진' (sajin)?",
        "option1": "Picture",
        "option2": "Chair",
        "option3": "Table",
        "option4": "Movie",
        "correct_answer": "Picture",
    },
    {
        "question_text": "What does '영화관' (yeonghwagwan) mean?",
        "option1": "Cinema",
        "option2": "Sea",
        "option3": "House",
        "option4": "Food",
        "correct_answer": "Cinema",
    },
    {
        "question_text": "What does '여행' (yeohaeng) mean?",
        "option1": "Travel",
        "option2": "Study",
        "option3": "Work",
        "option4": "Gift",
        "correct_answer": "Travel",
    },
]

for q in questions:
    WordQuiz.objects.get_or_create(**q)

print("✅ Word quiz questions added successfully!")
