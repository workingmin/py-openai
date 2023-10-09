#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)

echo "generate image based on a english prompt..."
python $workdir/image.py --prompt="two dogs playing chess, oil painting" --size="512x512"

echo "generate image based on a chinese prompt..."
python $workdir/image.py --prompt="美少女" --size="512x512"