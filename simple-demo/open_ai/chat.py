#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import getopt
import openai

def usage():
    print("Usage: %s [OPTION]..." % (sys.argv[0]))
    print(" --help              Display this help and exit")
    print(" --model             Chat Completion Model")
    print(" --messages-file     Messages JSON file")

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], "", ["model=", "messages-file=", "help"])

    for o, a in opts:
        if o in ("--help"):
            usage()
            sys.exit()
        elif o in ("--model"):
            model = a
        elif o in ("--messages-file="):
            messages_file = a
        else:
            assert False, "unhandled option"

    openai.api_type = 'open_ai'
    openai.api_version = None
    if os.getenv('OPENAI_API_BASE') is not None:
        openai.api_base = os.getenv('OPENAI_API_BASE') # default: 'https://api.openai.com/v1'
    openai.api_key = os.getenv('OPENAI_API_KEY')

    if  openai.api_key is None:
        print("OpenAI API key not specified")
        sys.exit(1)

    if messages_file is None:
        print("messages file not specified")
        sys.exit(1)
    
    with open(messages_file, 'r') as f:
        messages = json.loads(f.read())

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    print(f'{response["choices"][0]["message"]["content"]}')
