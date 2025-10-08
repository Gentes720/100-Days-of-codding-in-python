from tkinter import*# pyright: ignore[reportWildcardImportFromLibrary]
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pandas.read_csv('/home/gentes/Documents/My 100 days pycodes/31/data/words_to_learn.csv')
except (FileNotFoundError, pandas.errors.EmptyDataError):
    original_data = pandas.read_csv('/home/gentes/Documents/My 100 days pycodes/31/data/french_words.csv')
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")


#-----functions-------#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text= "French", fill= "black")
    canvas.itemconfig(word_text, text= current_card["French"], fill= "black")
    canvas.itemconfig(bg_image, image= card_front)
    flip_timer = window.after(3000, func= flip_card)

def is_known():
    to_learn.remove(current_card)
    data =  pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index= False)

    next_card()


def flip_card():

    canvas.itemconfig(title_text, text= "English", fill= "white")
    canvas.itemconfig(word_text, text= current_card["English"], fill= "white")
    canvas.itemconfig(bg_image, image= card_back)
 #-----UI SETUP-------#
window = Tk()
window.title("MyFlashCard") 
window.config(padx= 30, pady= 30, background= BACKGROUND_COLOR)

flip_timer = window.after(3000, func= flip_card)

# front card image

canvas = Canvas(width= 800, height= 526, highlightthickness= 0, background= BACKGROUND_COLOR)
card_front = PhotoImage(file= '/home/gentes/Documents/My 100 days pycodes/31/images/card_front.png')
card_back = PhotoImage(file= '/home/gentes/Documents/My 100 days pycodes/31/images/card_back.png')

bg_image = canvas.create_image(400, 263, image= card_front)

title_text = canvas.create_text(400, 160, text= "title", font = ("Ariel", 25 , "italic"))

word_text = canvas.create_text(400, 263, text= "word", font = ("Ariel", 45 , "bold"))

canvas.grid(row= 0, column= 0, columnspan= 2)

# Buttons
croos_image = PhotoImage(file = '/home/gentes/Documents/My 100 days pycodes/31/images/wrong.png') 
right_image = PhotoImage(file = '/home/gentes/Documents/My 100 days pycodes/31/images/right.png')

cross_button = Button(image = croos_image , highlightthickness = 0, command= next_card)
cross_button.grid(row = 1, column= 0)

right_button = Button(image = right_image , highlightthickness = 0, command= is_known)
right_button.grid(row = 1, column= 1)









next_card()

window.mainloop()