from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('register/',views.register_view,name = 'register'),
    path('login/',views.login_view,name = 'login'),
    path('alphabet/', views.alphabet, name='alphabet'),
    path('words/', views.words, name='words'),
    path('grammar/', views.grammar, name='grammar'),
    path('alphabet_quiz/', views.alphabet_quiz, name='alphabet_quiz'),
    path('word_quiz/', views.word_quiz, name='word_quiz'),
    path('grammar_quiz/', views.grammar_quiz, name='grammar_quiz'),
    path('logout/',views.logout_view,name = 'logout'),
]