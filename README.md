convert-resize-photo-albums
===========================

This is a very custom setup for batch processing and resizing images for a
personal photo website - I've made this code public so you may find it helpful.

Essentially this will:
- generate a config based on the paths in `library.json`, including the files to
  process
- convert the RAW files (specified in the config) to full size JPEGs
- resize the JPEGs to a number of different formats, specified in `library.json`.

# generate-config.py

Outputs config, used by Flask server, generate-convert.py and generate-resize.py

# generate-convert.py

Generate bash script to convert the raw files to JPEGs

# generate-resize.py

Generate the bash script to resize the images

# main.sh

Do all the above!
