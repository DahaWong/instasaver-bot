from datetime import time
def clear(context):
  context.user_data['today'].clear()
  context.user_data['today']['count'] = 0

def run_job(jobs):
  jobs.run_daily(clear, time=time(16,0))