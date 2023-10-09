#!/usr/bin/env python3

import os
import json
import openai
from flask import Flask, jsonify, render_template, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='console.log')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image', methods = ['POST'])
def image():
    data = json.loads(request.get_data(as_text=True))
    prompt = data.get('prompt')
    
    openai.api_type = 'open_ai'
    openai.api_version = None
    openai.api_base = os.getenv('OPENAI_API_BASE') 
    openai.api_key = os.getenv('OPENAI_API_KEY')
    try:
        resp = openai.Image.create(prompt=prompt, n=1, size="512x512")
        image_url = resp['data'][0]['url']
        app.logger.error("prompt: {}, create image url: {}".format(prompt, image_url))
        return jsonify({
            "url": image_url
        })
    except openai.error.OpenAIError as e:
        app.logger.error(json.dumps(e.error))
        return jsonify({
            "error": json.dumps(e.error)
        })
        
        