from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask,render_template,request
from flask import Flask, flash, redirect, render_template, request, url_for
from pygame import mixer 

mixer.init()

import os
chatbot = ChatBot(
    'Norman', read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 

trainer = ListTrainer(chatbot)
data=[]
for _file in os.listdir("chatbot data/"):

        data = data + open("chatbot data/"+ _file).read().splitlines()
        
trainer.train(data)


app = Flask(__name__)

app.secret_key = 'random string'

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/home')
def home_page1():
    return render_template('home.html')


@app.route('/SIT Assistant')
def chatbot_web():
    return render_template('head.html')
    

@app.route('/SIT Assistant', methods=['POST'])
def chat_bot_text():
    if(request.form['message']!=""):
        msg = request.form['message']
        if(msg=="give me a clap"):
            mixer.music.load('sound/clap.mp3')
            mixer.music.play()
            reply=""
            msg=""
            pass
        elif(msg=="pikachu"):
            mixer.music.load('sound/Pika Thunder.mp3')
            mixer.music.play()
            reply=""
            msg=""
            pass
        else:    
            reply1 = chatbot.get_response(msg)
            reply = reply1.text
            #reply_bot1,temp=reply.split("$")
            pass
        return render_template('head.html',reply_bot=reply,msg=msg)
    else:
        return render_template('head.html',reply_bot='How May I Help You', msg=' ')


@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
