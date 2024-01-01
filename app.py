from flask import Flask, render_template, request, redirect, url_for, session
import os
import logging
import sys
import threading
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/prompt')
def prompt():
    data = request.json
    print(data)
