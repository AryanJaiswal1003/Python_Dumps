import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0        # Keeps track of which question we are on
        self.score = 0                  # Player's score
        self.question_list = q_list     # List of Question objects
        self.current_question = None    # Stores the current Question object

    def still_has_questions(self):
        """
           Returns True if there are more questions left, otherwise returns False.
       """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
            Retrieves the next question from the list, increments the question counter, and returns the question text
                (decoded from HTML entities).
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text) # Decode HTML entities like &quot; or &#039; (useful for API questions)

        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer:bool):
        """
            Checks the user's answer against the correct answer. Increases the score if the answer is correct.
                Returns True if correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False