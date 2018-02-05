#!/usr/bin/env python3
import json

libraryData = json.load(open('library.json'))

quality = libraryData['quality']

sizes = libraryData['sizes'] 

convertedDir = libraryData['converted_dir']
processedDir = libraryData['processed_dir']


commands = [
    "#!/usr/bin/env bash",
    "set -ex"
]

commands.append('echo "Starting..."')


for size in sizes:
    cycleName = str(size)
    outputFolder = processedDir + '/' + str(size)
    commands.append('cp -r "./' + convertedDir + '" "' + outputFolder + '"')
    commands.append('echo "Done copying ' + cycleName + '"')

    resizeConversion = 'magick mogrify -resize ' + str(size) + 'x' + str(size) + ' ' + outputFolder + '/**/*.jpg -quality ' + str(quality)
    commands.append(resizeConversion)

    commands.append('echo "Done converting ' + cycleName + '."')

commands.append("echo 'Done.'")

print("\n\n".join(commands))