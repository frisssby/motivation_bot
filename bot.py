"""Telegram bot that sends motavational quotes"""

import os
import requests
import telebot

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """"Send user the greeting message"""
    bot.reply_to(message, "Hi, buddy! Type /quote to get your piece of motivation.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """"Get the quote and send it to user"""
    response = requests.get("https://nodejs-quoteapp.herokuapp.com/quote")
    if response:
        bot.send_message(message.chat.id, response.json().get("quote"))
    else:
        bot.send_message(message.chat.id, "Something went wrong. Please, try again later.")
        
bot.infinity_polling()
