from tkinter import *
from tkinter import ttk
import random
root = Tk()
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