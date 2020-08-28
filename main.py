import PySimpleGUI as sg
from random import randint
'''This is the start of a program that shows a picture of a rick or 
a stick. The user selects the correct button and it prints their choice
to the console. Can you turn this into a game?'''

# images of Ricks and Sticks - stored as lists
ricks = ['images/Rick_Sanchez.png',
        'images/rickastley_new.png',
        #'images/rickastley2_new.png',
        'images/rickstein_new.png',
        'images/ricknixon_new.png',
        'images/rickymartin_new.png']
sticks = ['images/stick1.png',
        'images/stickblender_new.png',
        'images/popstick_new.png',
        'images/stickinsect_new.png',
        'images/stick2_new.png',
        'images/stick3_new.png']
imageList = []



# get a random number from 0 to the number passed into the function
def getRandom(num):
    return randint(0,num)

def getImage():
    # randomly select either ricks list or sticks list
    if getRandom(1) == 1:
        # randomly select one of the 6 stick images
        image = sticks[getRandom(5)]
    else:
        # randomly select one of the 5 rick images
        image = ricks[getRandom(4)]
    return image

# DEFINE THE LAYOUT
layout = [
            [sg.Text('Is this a Rick or a Stick?')],
            [sg.Image(filename=getImage(), key='current_image', size=(300,400))],
            [sg.Button('Rick'), sg.Button('Stick'), sg.Button('Exit')]
]

# CREATE THE WINDOW

window = sg.Window('The Rick or Stick Game', layout)

# THE EVENT LOOP

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Rick':
        print('Rick')
        window['current_image'].update(filename=getImage(), size=(300,400))
    elif event == 'Stick':
        print('Stick')
        window['current_image'].update(filename=getImage(), size=(300,400))
window.close()
