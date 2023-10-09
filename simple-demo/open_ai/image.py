#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import getopt
import openai

def usage():
    print("Usage: %s [OPTION]..." % (sys.argv[0]))
    print(" --help      Display this help and exit")
    print(" --prompt    Create new image based on a prompt")
    print(" --size      Image Size, default \"512x512\"")

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], "", ["prompt=", "size=", "help"])

    for o, a in opts:
        if o in ("--help"):
            usage()
            sys.exit()
        elif o in ("--prompt"):
            prompt = a
        elif o in ("--size="):
            size = a
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

    if prompt is None:
        print("prompt is not specified")
        sys.exit(1)

    if size is None:
        size = "512x512"

    image_resp = openai.Image.create(prompt=prompt, n=1, size=size)
    print(image_resp['data'][0]['url'])