"""Telegram bot that sends motavational quotes"""

import os
import telebot

bot = telebot.TeleBot(os.environ.get('TOKEN'))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """"Send user the greeting message"""
    bot.reply_to(message, "Hi, buddy! Type /quote to get your piece of motivation.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """"Echo the message"""
    bot.reply_to(message, message.text);

bot.infinity_polling()
