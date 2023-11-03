#!/usr/bin/env python3

import openai
import os
import sys

if __name__ == '__main__':
    openai.api_type = 'open_ai'
    openai.api_version = None
    if os.getenv('OPENAI_API_BASE') is not None:
        openai.api_base = os.getenv('OPENAI_API_BASE') # default: 'https://api.openai.com/v1'
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <job-id>")
        sys.exit(1)
    
    job_id = sys.argv[1]
    response = openai.FineTuningJob.retrieve(job_id)
    fine_tuned_model_id = response["fine_tuned_model"]

    if fine_tuned_model_id is None: 
        raise RuntimeError("Fine-tuned model ID not found. Your job has likely not been completed yet.")

    print("Fine-tuned model ID:", fine_tuned_model_id)