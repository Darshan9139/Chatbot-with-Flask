from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
import os



'''chatbot = ChatBot("bot",logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter="chatterbot.storage.SQLStorageAdapter")
chatbot.set_trainer(ListTrainer)
for _file in os.listdir("chatbot data/"):
        data= open("chatbot data/"+ _file ,'r').readlines()
        chatbot.train(data)'''
chatbot = ChatBot('Chatbot for SITCOE', logic_adapters=[
                                            {
                                                'import_path': 'chatterbot.logic.BestMatch'
                                            },

                                            {
                                                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                                'threshold': 0.65,
                                                'default_response': 'I am Sorry, but I do not understand.'
                                            }
                                        ]
              )
chatbot.set_trainer(ListTrainer)
for _file in os.listdir("chatbot data/"):
        data= open("chatbot data/"+ _file ,'r').readlines()
        chatbot.train(data)
