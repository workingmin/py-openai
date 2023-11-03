#!/usr/bin/env python3

import openai
import os
import sys
import logging

logging.basicConfig(filename='upload_files.log', level=logging.DEBUG)

if __name__ == '__main__':
    openai.api_type = 'open_ai'
    openai.api_version = None
    if os.getenv('OPENAI_API_BASE') is not None:
        openai.api_base = os.getenv('OPENAI_API_BASE') # default: 'https://api.openai.com/v1'
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <training.jsonl> <validation.jsonl>")
        sys.exit(1)
    
    training_file = sys.argv[1]
    validation_file = sys.argv[2]
    
    training_response = openai.File.create(
        file=open(training_file, "rb"), purpose="fine-tune"
    )
    training_file_id = training_response["id"]
    logging.info("Training file ID: {}".format(training_file_id))
    
    validation_response = openai.File.create(
        file=open(validation_file, "rb"), purpose="fine-tune"
    )
    validation_file_id = validation_response["id"]
    logging.info("Validation file ID: {}".format(validation_file_id))
    