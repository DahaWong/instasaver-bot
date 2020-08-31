from config import update_info
from telegram.ext import Updater
from handlers.register import register
from utils.clear_today import run_job
 
updater = Updater(**update_info)
register(updater.dispatcher)
run_job(updater.job_queue)

updater.start_polling()
updater.idle()