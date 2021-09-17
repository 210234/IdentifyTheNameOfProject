from tkinter import *
import random
from tkinter import messagebox


# Colors that are insert in game
colors = ['Yellow','Red','Green','Blue','Black','White','Orange','Grey','Pink','Purple']

# Initial Score
score = 0

# Initial time 60 seconds
time = 60


# Defining startGame function
def startGame(self):

    if time==60:

        # Insert the countdown timer
        countdown()

    # Run the function to chose the next color
    nextcolor()


# Defining  nextcolor function
def nextcolor():

    global score
    global time

    # When a game is in play state
    if time > 0:

        # Making the text entry box active
        e.focus_set()

        # To convert all thw words into lower case so that if gamer write in upper case ans wont became wrong
        if e.get().lower() == colors[1].lower():

            score += 1

        # Clearing the entry the box
        e.delete(0, END)

        # For displaying the given colors randomly
        random.shuffle(colors)

        # changing the colour to type, by changing the
        # text _and_ the colour to a random colour value
        colour.config(fg= str(colors[1]) , text = str(colors[0]))

        # updating the score.
        scoreLabel.config(text = "Score: " + str(score))


# Defining countdown function
def countdown():

    global time

    # To show the score after finishing the time
    if time == 0:
        messagebox.showinfo("Time Left", "Time is over Your score is" + str(score))


    # When a game is in play
    if time > 0 :

        # decrement the time
        time -= 1

        # updating  the time left label
        timeLabel.config(text = "Time left: "+ str(time))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)


#Driver Code
if __name__=='__main__':

    root = Tk()

    photo = PhotoImage(file = "logo.png")
    background_label=Label(root,image=photo)
    background_label.place(x=0,y=0,relwidth=0,relheight=0)
    l = Label(image=photo).pack()

    # Inserting the title
    root.title('Identify The Name Of Color')

    # Setting the geometry of the window
    root.geometry('450x450')

    # Putting an instruction label
    instructions = Label(root, text = 'Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself!',
                         font = ('Helvetica', 12),fg="blue",bg="pink")
    instructions.pack()

    # Making a Score label
    scoreLabel = Label(root, text = 'Score :'+str(score), font=('Helvetica' , 12),fg="blue",bg="pink")
    scoreLabel.pack()

    # Making a Time Label
    timeLabel = Label(root, text = 'Time Left : '+str(time), font=('Helvetica' , 12),fg="blue",bg="pink")
    timeLabel.pack()

    # Making a colour label
    colour = Label(root, font=('Helevetica',25))
    colour.pack()



    # Entry box for input from user
    e= Entry(root)


    e.focus_set()
    root.bind('<Return>',startGame)

    e.pack()
    startbutton = Button(root, text="start!", width = 10, fg = "red", bg = "pink", bd = 0,padx = 20,command = nextcolor)
    startbutton.pack()

    # To display the name of developer
    developer = Label(text="This game was developed by \n Rikesh maharjan!", fg="black",bg="sky blue")
    developer.pack()

    # Start te Gui
    root.mainloop()

