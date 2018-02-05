#!/usr/bin/env bash

config=$(./generate-config.py)

convert=$(echo "${config}" | ./generate-convert.py)

# Run conversion
echo "${convert}" | bash

# Run resize
./generate-resize.py | bash

echo "Done."



