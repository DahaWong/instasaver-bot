def delete(context):
    job = context.job
    context.bot.delete_message(*job.context)

def later(update, context, message, timeup=1800):
  context.job_queue.run_once(delete, timeup, context=[message.chat_id, message.message_id])
  if update.message:
    context.job_queue.run_once(delete, timeup, context=[update.message.chat_id, update.message.message_id])
  