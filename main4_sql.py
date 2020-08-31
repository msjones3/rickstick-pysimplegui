import PySimpleGUI as sg
from random import randint
import sqlite3
'''Saving the players file to a database rather than a text file.
This is probably overkill for this application. Normally
You would have more than just one field. '''

# connect to database (if it doesn't exist then create it)
db = sqlite3.connect("players.db")
db.cursor().executescript("""
  
  CREATE TABLE IF NOT EXISTS players(
    nickname TEXT NOT NULL
  );""")

db.commit()

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
            [sg.Button('Rick'), sg.Button('Stick')],
            [sg.Button('view players'), sg.Button('Exit')]
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
                # User has won. Store their name only if they have entered or not cancelled
                winner = sg.popup_get_text('You won!','please enter your name')
                if not winner or winner == "":
                    sg.popup("Thanks for playing")
                    break
                sg.popup(f'congratulations, {winner}. You are the new winner.')
                # add the name to the database
                db.cursor().execute("INSERT INTO players(nickname) VALUES (?);", (winner,))
                db.commit()
                break
            print(f'new score {score}')
            window['score'].update(score)
            image, answer = getNew()
            window['current_image'].update(filename=image, size=(300,400))
        else:
            print('Incorrect. No Change to score')
            window['current_image'].update(filename=image, size=(300,400))
    if event =='view players':
        # get list of players - We need to return every player in the table
        results = db.cursor().execute("SELECT nickname from players").fetchall()
        # store all names into a variable called players
        players = []
        # players will be the 0th item in each tuple
        for result in results:
            players.append(result[0])
        sg.sprint(*players, title="Past Players", size=(30,20))
db.close()
window.close()
