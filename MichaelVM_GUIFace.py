from tkinter import * #Imports for GUI and random number generator
from random import randint

master = Tk()  #New TK instance
master.title("GUI Outlab - Michael Valentino-Manno") #Title that shows up on window

window = Canvas(master, width = 300, height = 300) #Create canvas size 300 by 300
window.pack() #Pack is a layout manager 

window.create_rectangle(0, 0, 300, 300, fill = "green") #Makes backgound green
mouth = window.create_line(125, 195, 175, 195) #Draws mouth, and saves it as a variable
eye1 = window.create_oval(100, 110, 140, 150) #Draws the left eye and saves it as a variable
eye2 = window.create_oval(160, 110, 200, 150) #Draws the right eye and saves it as a variable
window.create_oval(75, 85, 225, 235) #Draws head 
counter = 0 #Counter used for talk

def Eyes(): #Eyes method that moves the eyes by a random int between -3 and 3 in the x and y directions
    x1 = randint(-3, 3) #Create random int 
    y1 = randint(-3, 3) #Create random int
    x2 = randint(-3, 3) #Create random int
    y2 = randint(-3, 3) #Create random int
    window.move(eye1, x1, y1) #Move the left eye by the random ints x1 and y1
    window.move(eye2, x2, y2) #Move the right eye by the random ints x2 and y2

def Talk(): #Talk method that opens the closed mouth or closes the open mouth
    global counter #Global counter used to determine if the mouth is open or closed
    global mouth #Mouth is global so it can be deleted in a different call
    global mouthOpen #mouthOpen is gloval so it can be deleted in a different call
    counter += 1 #Counter gets incramented
    if counter % 2 == 0: #If counter is even, the mouth is open
        mouth = window.create_line(125, 195, 175, 195) #Draw closed mouth
        window.delete(mouthOpen) #Delete open mouth
    if counter % 2 == 1: #If counter is odd, the mouth is closed
        mouthOpen = window.create_oval(115, 180, 190, 210) #Draw open mouth
        window.delete(mouth); #Delete closed mouth

def Quit(): #Method that exits program
    exit() #Stop execution


button1 = Button(master, text = "Eyes", command = Eyes) #Create Eyes button, that when pressed executes the Eyes command
window.create_window(100, 275, window = button1) #Place eyes button in the bottom left portion of canvas

button2 = Button(master, text = "Talk", command = Talk) #Creates Talk button, that when pressed executes the talk command
window.create_window(200, 275, window = button2) #Place talk button in the bottom right portion of the canvas

button3 = Button(master, text = "Quit", command = Quit) #Create Quit button that when pressed executes the Quit command
window.create_window(150, 20, window = button3) #Place quit button in the top middle of the canvas
