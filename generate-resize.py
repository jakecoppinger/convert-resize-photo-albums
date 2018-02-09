#!/usr/bin/env python3
import json

libraryData = json.load(open('library.json'))

quality = libraryData['quality']

sizes = libraryData['sizes'] 

convertedDir = libraryData['converted_dir']
processedDir = libraryData['processed_dir']


commands = [
    "#!/usr/bin/env bash",
    "set -e"
]

commands.append('echo "Starting..."')


for size in sizes:
    cycleName = str(size)
    outputFolder = processedDir + '/' + str(size)
    # commands.append('cp -r "./' + convertedDir + '" "' + outputFolder + '"')
    commands.append('rsync -a -v --ignore-existing "./' + convertedDir + '" "' + outputFolder + '"')
    commands.append('echo "Done copying ' + cycleName + '"')

    resizeConversion = 'magick mogrify -resize ' + str(size) + 'x' + str(size) + ' ' + outputFolder + '/**/*.jpg -quality ' + str(quality)
    commands.append('echo "Resizing..."')
    commands.append(resizeConversion)

    commands.append('echo "Done resizing ' + cycleName + '."')
    commands.append("\n")

commands.append("echo 'Done.'")

print("\n".join(commands))