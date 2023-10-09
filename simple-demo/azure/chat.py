#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Note: The openai-python library support for Azure OpenAI is in preview.

import sys
import os
import json
import getopt
import openai

def usage():
    print("Usage: %s [OPTION]..." % (sys.argv[0]))
    print(" --help              Display this help and exit")
    print(" --engine            Chat Completion Engine")
    print(" --messages-file     Messages JSON file")

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], "", ["engine=", "messages-file=", "help"])

    for o, a in opts:
        if o in ("--help"):
            usage()
            sys.exit()
        elif o in ("--engine"):
            engine = a
        elif o in ("--messages-file="):
            messages_file = a
        else:
            assert False, "unhandled option"
    
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"
    openai.api_base = os.getenv("OPENAI_API_BASE")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    with open(messages_file, 'r') as f:
        messages = json.loads(f.read())
        
    response = openai.ChatCompletion.create(
        engine=engine,
        messages=messages
    )
    print(response['choices'][0]['message']['content'])