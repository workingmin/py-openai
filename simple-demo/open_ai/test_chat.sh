#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
messages_file="$workdir/../tests/test_chat_messages.json"

echo "test model gpt-3.5-turbo start..."
python $workdir/chat.py --model='gpt-3.5-turbo' --messages-file="$messages_file"

echo "test model gpt-3.5-turbo-16k start..."
python $workdir/chat.py --model='gpt-3.5-turbo-16k' --messages-file="$messages_file"

echo "test model gpt-4 start..."
python $workdir/chat.py --model='gpt-4' --messages-file="$messages_file"
