from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Alphabet , Words , Grammar , QuizResult,  AlphabetQuiz, WordQuiz,QuizResult2,GrammarQuiz , QuizResult3
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"your password or username is already use")
            return render (request,'lessons/register.html',{
                'form' : form
            })
    else:
        form = UserCreationForm()
        return render (request,'lessons/register.html',{
            'form' : form
        })
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"your password or username is incorrect")
            return render (request,'lessons/login.html',{
                'form' : form
            })
    else:
        form = AuthenticationForm()
        return render (request,'lessons/login.html',{
            'form' : form
        })
@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    return render (request,'lessons/home.html',{
        'user' : user
    })
def alphabet(request):
    letters = Alphabet.objects.all()
    return render(request, 'lessons/alphabet.html',
      {'letters': letters})

@login_required
def alphabet_quiz(request):
    questions = AlphabetQuiz.objects.all()[:10]

    if request.method == "POST":
        total = len(questions)
        correct = 0

        for i, q in enumerate(questions, start=1):
            chosen = request.POST.get(f"q{i}")
            if chosen and chosen.strip() == q.correct_answer.strip():
                correct += 1

        # نمره از ۱۰۰
        score = int((correct / total) * 100)

        # ذخیره در دیتابیس
        QuizResult.objects.create(
            user=request.user,
            score=score,
            date_taken=timezone.now()
        )
        previous_results = QuizResult.objects.filter(user=request.user).order_by('-date_taken')

        return render(request, "lessons/quiz_result.html", {
            "score": score,
            "total": total,
            "correct": correct,
            "previous_results": previous_results
        })

    return render(request, "lessons/alphabet_quiz.html", {"questions": questions})

def words(request):
    letters = Words.objects.all()
    return render(request, 'lessons/words.html',{
        'letters' : letters
    })
@login_required
def word_quiz(request):
    questions = WordQuiz.objects.all()[:10]

    if request.method == "POST":
        total = len(questions)
        correct = 0

        for i, q in enumerate(questions, start=1):
            chosen = request.POST.get(f"q{i}")
            if chosen and chosen.strip() == q.correct_answer.strip():
                correct += 1

       
        score = int((correct / total) * 100)

        
        QuizResult2.objects.create(
            user=request.user,
            score=score,
            date_taken=timezone.now()
        )
        previous_results = QuizResult2.objects.filter(user=request.user).order_by('-date_taken')

        return render(request, "lessons/quiz_result2.html", {
            "score": score,
            "total": total,
            "correct": correct,
            "previous_results" : previous_results
        })

    return render(request, "lessons/word_quiz.html", {"questions": questions})

def grammar(request):
    letters = Grammar.objects.all()
    return render(request, 'lessons/grammar.html',{
        'letters' : letters
    })

@login_required
def grammar_quiz(request):
    questions = GrammarQuiz.objects.all()[:10]

    if request.method =="POST":
        total = len(questions)
        correct = 0

        for i, q in enumerate(questions , start=1):
            chosen = request.POST.get(f"q{i}")
            if chosen and chosen.strip() == q.correct_answer.strip():
                correct += 1
        
        score = int((correct / total) * 100)

        QuizResult3.objects.create(
            user = request.user,
            score = score,
            date_taken = timezone.now()
        )
        previous_results = QuizResult2.objects.filter(user=request.user).order_by('-date_taken')

        return render(request,"lessons/quiz_result3.html",{
            "score" : score,
            "total" : total,
            "correct" : correct,
            "previous_results" : previous_results 
        })
    return render(request,"lessons/grammar_quiz.html",{
        "questions" : questions
    })
def logout_view(request):
    logout(request)
    return redirect(login_view)
