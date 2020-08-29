from config import update_info
from telegram.ext import Updater
from handlers.register import register
 
updater = Updater(**update_info)
dp = updater.dispatcher
register(dp)

updater.start_polling()
updater.idle()