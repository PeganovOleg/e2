import threading
import time

from send_email import send_email_with_text

TASKS = []
NUMBER_OF_TASKS = 10 
EMAIL_FROM = 'azure_1d60a1018e3994a754d0c57248c0cfe0@azure.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'azure_1d60a1018e3994a754d0c57248c0cfe0@azure.com'
EMAIL_HOST_PASSWORD = 'M9284336198m'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


def worker(text,text2):
    send_email_with_text(text, EMAIL_FROM, text2)
    

def add_email_to_emails(text,text2,timer):
    TASKS.append({"text": text,"text2": text2, "timer": timer})
    t = threading.Timer(timer, worker, args=(text, text2, ))
    t.start()

def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:] 
