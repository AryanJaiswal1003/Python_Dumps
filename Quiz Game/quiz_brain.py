class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0 # Keep track of the current question number
        self.question_list = q_list # Store all the questions passed into the quiz
        self.score = 0 # Keep track of the user’s score

    def still_has_question(self): # Returns True if there are still questions left in the list
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]  # Get the current question object
        self.question_num += 1
        user_answer = input(f"Q{self.question_num}: {current_question.text} (True / False): ").lower() # Ask the user for input (True/False)

        # Check if the user’s answer is correct
        self.check_answer(user_ans=user_answer, correct_ans=current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            print("You Answered the Question Correctly!!")
            self.score += 1
        else:
            print("You're Answer is Wrong!!")

        # Show correct answer and current score
        print(f"The Correct Answer for this Question was: {correct_ans}")
        print(f"Your Score is: {self.score} / {self.question_num}\n")