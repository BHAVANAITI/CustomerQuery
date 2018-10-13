from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot('Test') #create chatbot
conv = open('ads.txt', 'r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")



