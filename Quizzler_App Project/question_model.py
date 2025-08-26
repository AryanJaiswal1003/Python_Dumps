class Question:

    def __init__(self, q_text, q_answer):
        """
            Represents a single quiz question.
            :param q_text: The text of the question
            :param q_answer: The correct answer (usually "True" or "False")
        """
        self.text = q_text      # The question itself
        self.answer = q_answer  # The correct answer
