from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from handlers import *
from creat import *
updater = Updater('5841952121:AAHEiRXx89OYd2ZMP4wqwj-e8ZflsndmVo0')

updater.dispatcher.add_handler(CommandHandler('start', hi_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('mult', mult_command))
updater.dispatcher.add_handler(CommandHandler('def', def_command))
updater.dispatcher.add_handler(CommandHandler('dev', dev_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

print('server start')
updater.start_polling()
updater.idle()

