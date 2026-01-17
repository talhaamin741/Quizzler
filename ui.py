from tkinter import *

from quiz_brain import QuizBrain

img1="./images/true.png"
img2="./images/false.png"
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label=Label(text=f"Score:{self.quiz.score}",fg="white",font=("Times New Roman",20,"bold"),bg=THEME_COLOR)
        self.score_label.grid(row=0,column=0,columnspan=2)
        self.screen=Canvas(height=250,width=300,bg="white")
        self.question_text=self.screen.create_text(130,120,text="Question:",width=240,font=("Arial",15,"italic"),fill=THEME_COLOR)
        self.screen.grid(row=2,column=0,columnspan=2,pady=50)
        crr_img = PhotoImage(file=img1)
        wr_img = PhotoImage(file=img2)
        self.correct = Button(image=crr_img,highlightthickness=0,command=self.right_pressed)
        self.correct.grid(row=3, column=0,rowspan=2)
        self.wrong = Button(image=wr_img,highlightthickness=0,command=self.wrong_pressed)
        self.wrong.grid(row=3, column=1,rowspan=2)
        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.screen.configure(bg="white")
        if self.quiz.still_has_questions():
            new_text=self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.screen.itemconfig(self.question_text,text=new_text)
        else:
            self.screen.itemconfig(self.question_text,text="Congratulations!\nYou have completed the Quiz")
            self.wrong.config(state="disabled")
            self.correct.config(state="disabled")
    def right_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.get_response(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.get_response(is_right)

    def get_response(self,result):
        if result==True:
            self.screen.config(bg="green")
        else:
            self.screen.config(bg="red")
        self.window.after(1000,self.get_next_question)

