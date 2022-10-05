from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler
from telegram.ext.filters import MessageFilter
from telegram import Update

def start(update: Update, context: CallbackContext):
    context.bot.send_message(
    chat_id=update.effective_chat.id,
    text="Salom!"
)

updater = Updater(token='5463237071:AAFcOhP3U4T5KfGAJM1ldJuZ8UZriL8e1uE', use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
message_handler = MessageHandler()

dispatcher.add_handler(start_handler)

updater.start_polling()