import os
import logging
import json
from flask import Flask, render_template, request
from openai import OpenAI
from pathlib import Path
from google_service import GoogleService






#globals
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/token')
def token():
   try:
         if(not Path('token.json').exists()):
             service = GoogleService()
             service._authenticate()
             
         access  = json.load(Path('token.json').open('r'))
         
         return access["token"]
         
   except Exception as e:
        print(f'An error occurred: {e}')
        return None

@app.get('/googleDocs')
def googleDocs():
    service = GoogleService()
    result = service.get_google_docs()
    if result:
        return result
    else:
        return '{"error": "An error occurred"}'

@app.post('/doc')
def doc():
    data = request.json
    print(data)
    doc_id = data['id']
    service = GoogleService()
    result = service.get_file(doc_id)
    if result:
        return result
    else:
        return '{"error": "An error occurred"}'
    
@app.post('/save')
def save():
    data = request.json
    print(data)
    doc_id = data['id']
    content = data['content']
    service = GoogleService()
    result = service.save_file(doc_id, content)
    if result:
        return result
    else:
        return '{"error": "An error occurred"}'

@app.post('/prompt')
def prompt():
    data = request.json
    print(data)
    model = data['model']
    prom = data['prompt']
    match model:
        case 'dall-e':
           conversation = dalle_conversation(prom)
        case _:
            conversation = chatGPT_conversation(model, prom)

    return conversation

def dalle_conversation(prom):
    img_params = {
        "model": "dall-e-3",
        "prompt": prom.strip(),
        "size": "1024x1024",
        "n": 1
        }
    res = client.images.generate(**img_params)
    return res.model_dump()

def chatGPT_conversation(model, prom):
    #set gpt-4 to preview
    if(model == 'gpt-4'):
        model = 'gpt-4-1106-preview'
    completion = client.chat.completions.create(
        model=model,
        messages=[
                    {"role": "system", "content": "You are a professinal children's book proofreader, trying to maintain the author's voice as much as possible while also suggesting slight improvements in story telling and cleaning up any overt grammar and spelling mistake that don't interfere with character or narrator dialog."},
                    {"role": "user", "content": prom.strip()}
                ]
    )
    return completion.model_dump()

  