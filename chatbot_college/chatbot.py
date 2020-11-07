from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask,render_template,request
from flask import Flask, flash, redirect, render_template, request, url_for

import os
chatbot = ChatBot("bot")
chatbot.set_trainer(ListTrainer)
for _file in os.listdir("chatbot data/"):
        data= open("chatbot data/"+ _file ,'r').readlines()
        chatbot.train(data)
app = Flask(__name__)

app.secret_key = 'random string'



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        if request.form['message']!="":
            msg = request.form['message']
            reply_bot1 = chatbot.get_response(msg)
            #reply_bot1="hello"
            return render_template('demo.html',reply_bot=reply_bot1,msg=msg)
        else:
            flash('You were successfully logged in')


    return render_template('demo.html')


if __name__ == "__main__":
    app.run(debug=True)


