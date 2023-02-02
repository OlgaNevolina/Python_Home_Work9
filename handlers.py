from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from creat import *


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}! Вас приветствует Бот Ботыч! Если хотите посчитать, нажмите {'/help'}")
    


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Напишите нужное действие: sum, mult, def, dev и числа через пробел' )

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    num1 = float(items[1])
    num2 = float(items[2])
    update.message.reply_text(f'{num1} + {num2} = {num1+num2}')

def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    num1 = float(items[1])
    num2 = float(items[2])
    update.message.reply_text(f'{num1} * {num2} = {num1*num2}')

def def_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    num1 = float(items[1])
    num2 = float(items[2])
    update.message.reply_text(f'{num1} - {num2} = {num1-num2}')

def dev_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    num1 = float(items[1])
    num2 = float(items[2])
    if num2 != 0:
        update.message.reply_text(f'{num1} / {num2} = {num1/num2}')
    else:
        update.message.reply_text(f"Делить на ноль нельзя! Напишите данные заново {'/help'}")    





