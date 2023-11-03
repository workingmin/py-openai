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

    print("Job ID:", response["id"])
    print("Status:", response["status"])
    print("Trained Tokens:", response["trained_tokens"])
    
    response = openai.FineTuningJob.list_events(id=job_id, limit=50)

    events = response["data"]
    events.reverse()

    for event in events:
        print(event["message"])