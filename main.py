from ui import QuizInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
from tkinter import *
from tkinter import messagebox
level=""
amount=0
def game_level():
    global level
    if(radio_state.get()==1):
        level="easy"
    elif(radio_state.get()==2):
        level="medium"
    else:
        level="difficult"
def start_it():
    global amount
    try:
        amount=int(questions.get())
        window.destroy()
    except ValueError:
        messagebox.showinfo(title="Invalid Input", message="Please Enter a number")
#Variable to hold on to which radio button value is checked.
window=Tk()
window.title("User Choices")
window.configure(padx=100,pady=50,width=400,height=500)
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Easy", value=1, variable=radio_state, command=game_level)
radiobutton2 = Radiobutton(text="Medium", value=2, variable=radio_state, command=game_level)
radiobutton3 = Radiobutton(text="Hard", value=3, variable=radio_state, command=game_level)
radiobutton1.grid(row=0,column=0,columnspan=2)
radiobutton2.grid(row=1,column=0,columnspan=2)
radiobutton3.grid(row=2,column=0,columnspan=2)
label=Label(text="Total Questions")
label.grid(row=5,column=0,rowspan=2)
questions=Entry(width=10,highlightthickness=0)
questions.grid(row=5,column=1,rowspan=2)
apply=Button(text="Apply",command=start_it,highlightbackground="Green")
apply.grid(row=8,column=0,columnspan=2)
window.mainloop()

parameters={"amount":amount,"type":"boolean","difficulty":level}

api="https://opentdb.com/api.php?"
status=0
try:
    data=requests.get(api,parameters)
    data.raise_for_status()
    question_data=data.json()
    status=requests.status_codes
    question_bank = []
    for question in question_data["results"]:
    #for question in question_data:

        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    win=QuizInterface(quiz)

    while quiz.still_has_questions():
        quiz.next_question()

except RuntimeError:
    if status==404:
        print("Address not found")
    elif status==300:
        print("Problem in fetching")
    elif status == 200:
        print("Information Successfully Fetched")
