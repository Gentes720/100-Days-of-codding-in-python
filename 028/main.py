from tkinter import *
import time, math
 # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "SET?!")
    title_label.config(text= "Timer", foreground= "#9bdeac")
    check_mark.config(text= "◔")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text= "Break", foreground= RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text= "Break", foreground= PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text= "Work", foreground= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"

    if int(count_sec) < 10:
        canvas.itemconfig(timer_text, text =  f"0{count_sec}")

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
         global timer
         timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 8 == 2:
            check_mark.config(text= "◔")
        elif reps % 8 == 4:
            check_mark.config(text= "◗")
        elif reps % 8 == 6:  
            check_mark.config(text= "◕")
        elif reps % 8 == 0:
            check_mark.config(text= "●")   
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro◔")
window.config(padx= 150, pady= 100, background= YELLOW)

title_label = Label(text= "Timer", foreground= "#9bdeac",background= YELLOW, font= (FONT_NAME, 50))
title_label.grid(column= 1, row=0)

 
canvas = Canvas(width= 200, height= 224, background= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(100, 112, image= tomato_img)
timer_text =  canvas.create_text(100, 143 , text = "SET?!", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)

start_button = Button(text= "Start", command= start_timer)
start_button.grid(column=0, row= 2)

reset_button = Button(text= "Reset", command= reset_timer)
reset_button.grid(column= 2, row = 2)

check_mark = Label(text= "◔", font= (FONT_NAME, 50), background= YELLOW, foreground= GREEN )
check_mark.grid(column=1, row= 3)


window.mainloop()