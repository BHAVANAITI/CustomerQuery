from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test') #create chatbot
conv = open('abc.txt', 'r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)
while True:
    request = raw_input('You: ')
    response = bot.get_response(request)
    
    print('Bot: ',response)



