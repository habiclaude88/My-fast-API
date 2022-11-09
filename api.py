from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')

@storage.get('/')
def index():
    return "My name is HABICLAUDE, This is my API"

@storage.get('/today')
def today():
    return str(datetime.now())

@storage.get('/mynames')
def names(First_name: bool = False, last_name: bool = False, full_name: bool = True):
    full_names = ""
    if First_name:
        full_names += 'Jean Claude'
    if last_name:
        full_names += 'HABIMANA'
    if full_name:
        full_names = 'Hello my name is Jean Claude HABIMANA'
    return full_names


