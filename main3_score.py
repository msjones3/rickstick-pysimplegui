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
score = 0
# setting a global variable to answer
answer = ''

# get a random number from 0 to the number passed into the function
def getRandom(num):
    return randint(0,num)

def getNew():
    # randomly select either ricks list or sticks list
    if getRandom(1) == 1:
        # randomly select one of the 6 stick images
        image = sticks[getRandom(5)]
        answer = 'Stick'
    else:
        # randomly select one of the 5 rick images
        image = ricks[getRandom(4)]
        answer = 'Rick'
    return (image, answer)
image, answer = getNew()
# DEFINE THE LAYOUT
layout = [
            [sg.Text('Is this a Rick or a Stick?')],
            [sg.Text('Score: '), sg.Text(score, key='score')],
            [sg.Image(filename=image, key='current_image', size=(300,400))],
            [sg.Button('Rick'), sg.Button('Stick'), sg.Button('Exit')]
]

# CREATE THE WINDOW

window = sg.Window('The Rick or Stick Game', layout)

# THE EVENT LOOP

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Rick' or event == 'Stick':
        print(answer)
        if event == answer:
            score += 1
            if score >= 5:
                # User has won. Store their name.
                winner = sg.popup_get_text('You won!','please enter your name')
                sg.popup(f'congratulations, {winner}. You are the new winner.')
                # close the file
                break
            print(f'new score {score}')
            window['score'].update(score)
            image, answer = getNew()
            window['current_image'].update(filename=image, size=(300,400))
        else:
            print('Incorrect. No Change to score')
            window['current_image'].update(filename=getImage(), size=(300,400))

window.close()
