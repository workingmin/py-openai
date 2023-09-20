#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import openai

if __name__ == '__main__':
    if os.getenv('OPENAI_API_TYPE') is not None:
        openai.api_type = os.getenv('OPENAI_API_TYPE') # default: 'open_ai'
    if os.getenv('OPENAI_API_BASE') is not None:
        openai.api_base = os.getenv('OPENAI_API_BASE') # default: 'https://api.openai.com/v1'
    if os.getenv('OPENAI_API_VERSION') is not None:
        openai.api_version = os.getenv('OPENAI_API_VERSION')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    if  openai.api_key is None:
        print("OpenAI API key not specified")
        sys.exit()
    
    openai_object = openai.Model.list()
    models = [ model.id for model in openai_object.data ]
    print(models)
