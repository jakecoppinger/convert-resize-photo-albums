#!/usr/bin/env python3
import json
import sys

assert(len(sys.argv) == 2)
albumName = sys.argv[1:][0]

libraryData = json.load(open('library.json'))

quality = libraryData['quality']

sizes = libraryData['sizes'] 

convertedAlbumDir = libraryData['converted_dir'] + albumName + '/'
processedDir = libraryData['processed_dir']


commands = [
    "#!/usr/bin/env bash",
    "set -e"
]

commands.append(f'echo "Resizing album [{albumName}]..."')

commands.append('echo "Copying and resizing for each size..."')

for size in sizes:
    cycleName = str(size)
    outputFolder = processedDir + '/' + str(size) + '/' + albumName + '/'
    # commands.append('cp -r "./' + convertedDir + '" "' + outputFolder + '"')

    commands.append(f'echo -n "{cycleName}..."')
    commands.append('rsync -a --ignore-existing "./' + convertedAlbumDir + '" "' + outputFolder + '"')
    resizeConversion = f'magick mogrify -resize {size}x{size} "{outputFolder}"*.jpg -quality {quality}'
    commands.append(resizeConversion)
    commands.append("\n")

commands.append(f'echo ""')
commands.append(f'echo "Done resizing album [{albumName}]."')

print("\n".join(commands))
