from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
RIGHT = "#99C68E"
WRONG = "#FF8674"
FONT = ("Arial", 14, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.question = "None"

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.question_canvas.create_text(150, 125, text=self.question, width=250, font=FONT)
        self.question_canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        true_btn_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_btn_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        false_btn_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_btn_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.question_canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="End of the Quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        answer_right = self.quiz.check_answer("True")
        self.feedback_and_score(answer_right)
        self.window.after(1000, self.display_next_question)

    def false_pressed(self):
        answer_right = self.quiz.check_answer("False")
        self.feedback_and_score(answer_right)
        self.window.after(1000, self.display_next_question)

    def feedback_and_score(self, answer_right):
        if answer_right:
            self.question_canvas.config(bg=RIGHT)
        else:
            self.question_canvas.config(bg=WRONG)

