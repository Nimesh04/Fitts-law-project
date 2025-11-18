from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
# root = Tk()
# frm = ttk.Frame(root, padding=500)
# frm.grid()

# four circle diameters and four distances from the position
# Circle diameters : 4, 6, 8, 10
# Distances from the position: 2, 6, 10, 14


# Function to randomize the list for the circle
def functionList():
    taskList = taskList = [
    (4, 2, -1), (4, 2, 1),
    (4, 6, -1), (4, 6, 1),
    (4, 10, -1), (4, 10, 1),
    (4, 14, -1), (4, 14, 1),
    (6, 2, -1), (6, 2, 1),
    (6, 6, -1), (6, 6, 1),
    (6, 10, -1), (6, 10, 1),
    (6, 14, -1), (6, 14, 1),
    (8, 2, -1), (8, 2, 1),
    (8, 6, -1), (8, 6, 1),
    (8, 10, -1), (8, 10, 1),
    (8, 14, -1), (8, 14, 1),
    (10, 2, -1), (10, 2, 1),
    (10, 6, -1), (10, 6, 1),
    (10, 10, -1), (10, 10, 1),
    (10, 14, -1), (10, 14, 1)
]
    return taskList

def randomizeList():
    tasks = functionList()
    random.shuffle(tasks)
    return tasks

# function to display the consent for the user
def consent():
    heading = "Participant Consent Form"
    body = "You are invited to take part in a research study. Participation is voluntary, and you may withdraw at any time without penalty. All information collected will remain confidential and used solely for research purposes. By selecting “I Agree,” you confirm that you are at least 18 years of age, have read this statement, and voluntarily consent to participate in the study."
    return print(f"{heading} {body}")

print(randomizeList())
# ttk.Button(frm, command=consent).grid(column=1, row=0)
# root.mainloop()

root = Tk()
root.title("Fitt's Law Project: Data Collection")
#root.state('zoomed')
root.geometry("1800x1000")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

startPage = tk.Frame(container, bg="lightblue")
experimentPage = tk.Frame(container, bg="lightgreen")

for frame in (startPage, experimentPage):
    frame.place(relwidth=1, relheight=1)

canvas = tk.Canvas(experimentPage, bg="white")
canvas.pack(fill="both", expand=True)

def drawCircle(x, y, r, color="skyblue"):
    return canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")

def check_click(event):
    x, y = event.x, event.y
    # Circle equation
    if (x - CX)**2 + (y - CY)**2 <= RADIUS**2:
        print("Circle clicked!")

def goToExperimentPage():
    experimentPage.tkraise()

############################## PAGE 1 ##############################

header = tk.Label (
    startPage,
    text="Participant Consent Form",
    font=("Arial", 40)
)
header.place(relx=0.5, y=80, anchor="center")

body = tk.Label (
    startPage,
    text="You are invited to take part in a research study. Participation is voluntary, and you may withdraw at any time without penalty. All information collected will remain confidential and used solely for research purposes. By selecting “I Agree,” you confirm that you are at least 18 years of age, have read this statement, and voluntarily consent to participate in the study.",
    wraplength = 1200,
    font=("Arial", 18)
)
body.place(relx=0.5, y=200, anchor="center")

button = tk.Button (
    startPage,
    text = "I Agree",
    font=("Arial", 18),
    command = goToExperimentPage
)
button.place(relx=0.5, y=300, anchor="center")

############################## PAGE 2 ##############################

centerButton = drawCircle(900, 500, 20)
targetButton = drawCircle(400, 500, 100)

############################## FOOTER ##############################

startPage.tkraise() 
root.mainloop()