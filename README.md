# 🏫 Learn Korean - Django Web App 🇰🇷

An interactive web-based Korean learning platform built with **Django**.  
It helps users learn the Korean alphabet (Hangul), vocabulary, and grammar through lessons, quizzes, and pronunciation features.  
Users can register, log in, take quizzes, and track their past scores.

---

## 🌟 Features

✅ **User Authentication**
- Register and log in securely using Django’s built-in authentication.
- Personalized dashboard that greets the logged-in user.

✅ **Learning Sections**
- **Alphabet Section:** Learn each Hangul character with pronunciation support.
- **Words Section:** Study basic Korean vocabulary with English and Persian translations.
- **Grammar Section:** Explore essential grammar concepts.

✅ **Interactive Quizzes**
- Three types of quizzes:
  - Alphabet Quiz  
  - Word Quiz  
  - Grammar Quiz  
- Each quiz consists of 10 random questions.
- Results are scored out of 100 and automatically stored in the database.

✅ **Audio Pronunciation**
- Each Korean word/character can be read aloud using the browser’s Speech Synthesis API (`speechSynthesis`).

✅ **Auto Question Loader**
- Questions are automatically added to the admin panel using Python scripts (`import django` method).

✅ **Score History**
- After every quiz, the user can view all previous quiz scores.

✅ **Responsive Design**
- Clean and simple user interface compatible with desktop and mobile devices.

---

## 🧩 Tech Stack

- **Backend:** Django (Python 3.x)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default)
- **Authentication:** Django Auth System
- **Speech Engine:** Web Speech API

---
## 📂 Project Structure
learn_korean/
│
├── lessons/
│ ├── models.py # Database models for alphabet, words, grammar, quizzes, results
│ ├── views.py # Logic for user interaction, quizzes, login, logout, etc.
│ ├── templates/
│ │ ├── lessons/
│ │ │ ├── home.html
│ │ │ ├── alphabet.html
│ │ │ ├── words.html
│ │ │ ├── grammar.html
│ │ │ ├── alphabet_quiz.html
│ │ │ ├── word_quiz.html
│ │ │ ├── grammar_quiz.html
│ │ │ ├── quiz_result.html
│ │ │ ├── quiz_result2.html
│ │ │ ├── quiz_result3.html
│ │ │ └── register.html / login.html
│ ├── static/
│ │ └── style.css
│ └── scripts/
│ ├── add_alphabet_quiz.py
│ ├── add_word_quiz.py
│ └── add_grammar_quiz.py
│
├── manage.py
├── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/learn-korean.git
cd learn-korean
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---

🧠 Usage

Home Page: Welcomes the logged-in user.

Alphabet/Words/Grammar: Explore and listen to Korean pronunciations.

Quizzes: Test your knowledge and view your previous scores.

Logout Button: Small red-bordered button on the top-right corner for easy logout.

---

👨‍💻 Author

Developed by: َAgrin Babaie
GitHub: https://github.com/Agrin74

## 📂 Project Structure

