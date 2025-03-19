#This file is if you want to host your bot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!\n\nInvite the Demo Bot with this link:\nhttps://discord.com/api/oauth2/authorize?client_id=979560474104463381&permissions=8&scope=bot"
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    server = Thread(target=run)
    server.start()