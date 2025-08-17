# Quiz Game (True/False)

This is a simple **True/False Quiz Game** built in Python using Object-Oriented Programming (OOP).

---

## 📂 Project Structure
- `main.py` → Entry point of the program. Loads questions and runs the quiz.
- `question_model.py` → Defines the `Question` class, which stores the text and answer of each question.
- `quiz_brain.py` → Defines the `QuizBrain` class, which manages question flow, scoring, and user interaction.
- `data.py` → Contains a list of questions in dictionary format (`question_data`).

---

## How It Works
1. Questions are loaded from `data.py`.
2. Each question is turned into a `Question` object.
3. The `QuizBrain` class handles:
   - Asking questions
   - Getting user input
   - Checking answers
   - Keeping track of score
4. The game continues until all questions are answered.
5. At the end, your **final score** is displayed.

---

## Learning Concepts Covered

1. Classes & Objects
2. Constructors (__init__)
3. Lists & Loops
4. User Input Handling
5. Basic OOP Principles