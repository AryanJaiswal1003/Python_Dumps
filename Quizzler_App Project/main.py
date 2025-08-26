from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# -------------------- Build Question Bank --------------------
question_bank = []
for question in question_data:
    question_text = question["question"]                    # extract question text
    question_answer = question["correct_answer"]            # extract correct answer
    new_question = Question(question_text, question_answer) # create Question object
    question_bank.append(new_question)                      # add to bank

# -------------------- Start Quiz --------------------
quiz = QuizBrain(question_bank) # pass all questions into QuizBrain
quiz_ui = QuizInterface(quiz)   # start the GUI with QuizBrain