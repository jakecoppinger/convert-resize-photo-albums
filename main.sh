#!/usr/bin/env bash

config=$(./generate-config.py)

convert=$(echo "${config}" | ./generate-convert.py)

# Run conversion
echo "${convert}" | bash

# Delete old resized images
rm -r ~/repos/photo-website/static/img/*

# Run resize
./generate-resize.py | bash

# Copy config
./generate-config.py > ~/repos/photo-website/data/config.json

echo "Done."



