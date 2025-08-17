from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain

question_list = [] # Create an empty list to store Question objects

# Convert each dictionary in question_data into a Question object
for ques in question_data:
    current_ques = ques['question'] # Extract the question text
    current_ans = ques['correct_answer']  # Extract the correct answer (True/False)

    # Create a Question object and add it to the list
    new_ques = Question(question= current_ques, answer=current_ans)
    question_list.append(new_ques)

# Initialize the QuizBrain with the list of questions
quiz = QuizBrain(q_list=question_list)

while quiz.still_has_question(): # Loop until there are no more questions left
    quiz.next_question()

# Final score after quiz completion
print(f"You have Completed the Quiz!!\nYour Final Score was: {quiz.score} / {quiz.question_num}")