from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # QuizBrain instance that handles the logic

        # -------------------- Window Setup --------------------
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # -------------------- Score Label --------------------
        self.score_label = Label(
            text=f"Score: 0",
            font=("Times New Roman", 12, "bold"),
            bg=THEME_COLOR,
            foreground="white"
        )
        self.score_label.grid(row=0, column=1)

        # -------------------- Question Canvas --------------------
        self.canvas = Canvas(width=350, height=300, bg="white", highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        # Text placeholder on canvas (updated later with actual questions)
        self.question_text = self.canvas.create_text(
            175, 150, # center
            text="Some Question Text",
            width=300, # wrap text if it's long
            font=("Times New Roman", 20, "italic"),
            fill="black"
        )

        # -------------------- Buttons --------------------
        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.wrong_button.grid(row=3, column=1)

        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.right_button.grid(row=3, column=0)

        self.get_next_question() # Load the first question

        self.window.mainloop()

    # -------------------- Functions --------------------
    def get_next_question(self):
        """Fetch the next question or end the quiz if none left."""
        self.canvas.config(bg="white")  # reset background color

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            # End of quiz
            self.canvas.itemconfig(self.question_text, text="You've Reached the End of the Quiz!!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        """User clicked 'True' → check answer and give feedback."""
        self.give_feedback(is_right=self.quiz.check_answer("True"))


    def false_pressed(self):
        """User clicked 'False' → check answer and give feedback."""
        self.give_feedback(is_right=self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
            Show green/red feedback based on correctness. Then automatically move to next question after 1 second.
        """
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        # delay next question by 1 second
        self.window.after(1000, self.get_next_question)