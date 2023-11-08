#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
messages_file="$workdir/../tests/test_chat_messages.json"

echo "test engine gpt-35-turbo start..."
python $workdir/chat.py --engine='gpt-35-turbo' --messages-file="$messages_file"    # if gpt-35-turbo engine is created in this resource

echo "test engine gpt-35-turbo-16k start..."
python $workdir/chat.py --engine='gpt-35-turbo-16k' --messages-file="$messages_file"    # if gpt-35-turbo-16k engine is created in this resource

