#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
messages_file="$workdir/../tests/test_chat_messages.json"

echo "test engine gpt-35-turbo start..."
python $workdir/chat.py --engine='gpt-35-turbo' --messages-file="$messages_file"

echo "test engine gpt-35-turbo-16k start..."
python $workdir/chat.py --engine='gpt-35-turbo-16k' --messages-file="$messages_file"
