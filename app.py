from turtle import ScrolledCanvas
from flask import Flask, render_template
import random

app = Flask(__name__)

#Scores
user_score = 0
com_score = 0

def computerChoice():
    print('Inside computerChoice Function')
    options = ['rock','paper','scissor']
    com_choice = random.choice(options)
    print('Computer Choice: ', com_choice)
    return com_choice

def WhoIsWinner(user_choice):
    print('Inside WhoIsWinner Function')
    global user_score
    global com_score
    result = ""
    com_choice = computerChoice()
    user_choice = user_choice.upper()
    com_choice = com_choice.upper()
    color=""
    print('com_choice: ',com_choice,'\nuser_choice: ', user_choice)
    if user_choice==com_choice:
        result = "Tie"
        color="yellow"
    elif user_choice=='ROCK' and com_choice=='SCISSOR':
        result = "You WON aganist computer!!"
        user_score +=1
        color="green"
    elif user_choice=='PAPER' and com_choice=='ROCK':
        result = "You WON aganist computer!!"
        user_score +=1
        color="green"
    elif user_choice=='SCISSOR' and com_choice=='PAPER':
        result = "You WON aganist computer!!"
        user_score +=1
        color="green"
    else:
        result = "You LOST to computer"
        com_score +=1
        color="red"
    final_result_details = {
        'result':result,
        'com_choice':com_choice,
        'user_choice':user_choice,
        'user_score': user_score,
        'com_score': com_score,
        'color':color
    }
    print('final_result_details: ', final_result_details)
    return final_result_details

@app.route('/')
def home():
    return render_template('home.html',user_score=user_score,com_score=com_score)

@app.route('/userPicked/<userchoice>')
def result(userchoice):
    print('User Choice: ', userchoice)
    result = WhoIsWinner(userchoice)
    return render_template('resultPage.html', result = result)

@app.route('/playAgain')
def playAgain():
    return render_template('home.html',user_score=user_score,com_score=com_score)

@app.route('/startOver')
def startOver():
    global user_score
    global com_score
    user_score=0
    com_score=0
    return render_template('home.html',user_score=user_score,com_score=com_score)
