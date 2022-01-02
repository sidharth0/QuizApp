THEME_COLOR = "#375362"
import tkinter as tk
from quiz_brain import QuizBrain
from tkinter import messagebox
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.scoreLabel = tk.Label(self.window, text="Score:0", bg=THEME_COLOR, fg='white')
        self.scoreLabel.grid(row=0, column=1, sticky='ew')

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg="white")
        self.questionText = self.canvas.create_text(150, 125, text="Question Area", fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)
        trueImg = tk.PhotoImage(file="./images/true.png")
        falseImg = tk.PhotoImage(file="./images/false.png")
        self.trueBut = tk.Button(self.window, image=trueImg, highlightthickness=0, command=self.answer_true)
        self.trueBut.grid(row=2, column=0, pady=10, sticky='w')
        self.falseBut = tk.Button(self.window, image=falseImg, highlightthickness=0, command=self.answer_false)
        self.falseBut.grid(row=2, column=1, pady=10, sticky='e')
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.questionText, text=q_text)

    def answer_true(self):
        self.submit_ans("True")

    def answer_false(self):
        self.submit_ans("True")

    def submit_ans(self, ans):
        if self.quiz.check_answer(ans):
            self.scoreLabel.config(text=f"Score:{self.quiz.score}")
            messagebox.showinfo(title="Answer", message="Your answer is correct.")
        else:
            messagebox.showinfo(title="Answer", message="Your answer is wrong.")
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            check = messagebox.showinfo(title="Quiz Completed",
                                        message=f"Your score in the Quiz : {self.quiz.score}/10 ")
            self.window.destroy()
