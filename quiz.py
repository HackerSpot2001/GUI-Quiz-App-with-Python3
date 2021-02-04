#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from random import randint

width = 640
height = 480
serial = 1
quis = {
    "Which language is used to written my Code":"python",
    "Name of hero in Iron-Man Movie series":"tony stark",
    "Who is Created Facebook":"mark zuckerberg",
    "What is the capital of india":"delhi",
    "What is the full form of 'WHO'":"world health organization",
    "Which company is  owned Whatsapp messanger":"facebook",
    "Which company is  owned Instagram":"facebook",
    "What is the full form of TOR ":"the onion router",
    "Who is created Linux Operating System":"linus torvalds",
    "Who is created Windows Operating System":"bill gates",
    "Who is the Founder of Apple Company":"steve jobs",
    "which language is the skeleton of web development":"html",
    "which language is used in client side and server side web development":"javascript",
    "correct the word:- buel":"blue",
    "correct the word:- yelowl":"yellow",
    "correct the word:- apepl":"apple",
}

# questions = list(quis.keys())
# print("\t\t######\tQuiz Application\t######\t\t")
# while True:
#     random_question = questions[randint(0,len(questions)-1)]
#     print(f"\t{serial}. {random_question}")
#     ans = str(input("Ans. ")).lower()
#     if ans == quis[random_question]:
#         print("Right Answer.\n")
        
#     if ans != quis[random_question]:
#         print("Wrong Answer.\n")

#     if not str(ans):
#         print("Please enter only String")

def change_text():
    global text_var,questions
    num = randint(0,len(questions)-1)
    random_question1 = questions[num]
    text_var.set(random_question1)

def check():
    global root,quis,random_question
    ans = answer.get()
    ans = ans.lower()
    if len(ans) >=1:
        if ans == quis[random_question]:
            messagebox.showinfo("Success","Your Answer is Right.")
            answer.delete(0,END)
            change_text()
    
        if ans != quis[random_question]:
            messagebox.showerror("Failure","You are Wrong.")
            answer.delete(0,END)
    
    if len(ans) == 0:
        messagebox.showwarning("Warning","Please Do not press submit button,\n before Entering the answer.")
    

         
        

if __name__ == "__main__":
    questions = list(quis.keys())
    random_number = randint(0,len(questions)-1)
    random_question = questions[random_number]
    width = 1080
    height = 480
    root = Tk()
    root.geometry(f"{width}x{height}+200+85")
    root.minsize(width,height)
    root.maxsize(width,height)
    root.title("Quiz Application | Python Project")
    root.configure(background="#4C4B4B")
    
    text_var = StringVar()
    text_var.set(f"{random_question}")
    lbl = Label(root,textvariable=text_var,font="sans-serif 19 bold",borderwidth=6,relief=GROOVE).pack(pady=30,ipadx=10)
    answer = Entry(root,font="sans-serif 15",width=40,fg="black",borderwidth=3,relief=SOLID,bg="white")
    answer.pack(pady=6,ipady=5)
    btn1 = Button(root,text="Submit".upper(),bg="#FF4848",font="sans-serif 18 bold",fg="black",command=check).pack(pady=10)
    root.mainloop()