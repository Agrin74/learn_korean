from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Alphabet(models.Model):
    korean_letter = models.CharField(max_length=10, verbose_name="korean word")
    meaning_fa = models.CharField(max_length=100, verbose_name="persian word")
    meaning_en = models.CharField(max_length=100, verbose_name="english word")


    def __str__(self):
        return self.korean_letter

class AlphabetQuiz(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"

class Words(models.Model):
    korean_letter = models.CharField(max_length=10, verbose_name="korean word")
    meaning_fa = models.CharField(max_length=100, verbose_name="persian word")
    meaning_en = models.CharField(max_length=100, verbose_name="english word")


    def __str__(self):
        return self.korean_letter

class WordQuiz(models.Model):
    question_text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

class QuizResult2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"

class Grammar(models.Model):
    korean_letter = models.CharField(max_length=10, verbose_name="korean word")
    meaning_fa = models.CharField(max_length=100, verbose_name="persian word")
    meaning_en = models.CharField(max_length=100, verbose_name="english word")


    def __str__(self):
        return self.korean_letter

class GrammarQuiz(models.Model):
    question_text = models.CharField(max_length= 255)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

class QuizResult3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"