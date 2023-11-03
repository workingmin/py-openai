#!/usr/bin/env python3

import openai
import os
import sys
import logging

logging.basicConfig(filename='finetuning_job.log', level=logging.DEBUG)

if __name__ == '__main__':
    openai.api_type = 'open_ai'
    openai.api_version = None
    if os.getenv('OPENAI_API_BASE') is not None:
        openai.api_base = os.getenv('OPENAI_API_BASE') # default: 'https://api.openai.com/v1'
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <training-file-id> <validation-file-id>")
        sys.exit(1)
    
    training_file_id = sys.argv[1]
    validation_file_id = sys.argv[2]
    response = openai.FineTuningJob.create(
        training_file=training_file_id,
        validation_file=validation_file_id,
        model="gpt-3.5-turbo",
        suffix="recipe-ner",
    )
    job_id = response["id"]

    logging.info("Job ID: {}".format(response["id"]))
    logging.info("Status: {}".format(response["status"]))
    