#!/usr/bin/env python3
import os
import json
import re
import sys

def pprint(o):
    print(json.dumps(o, sort_keys=True,
        indent=4, separators=(',', ': ')))

cwd = os.getcwd()

data = json.loads(sys.stdin.read())


libraryData = json.load(open('library.json'))
conversionProgram = libraryData['conversion_program']
convertedDir = libraryData['converted_dir']
albumPath = libraryData['album_path']

commands = [
    "#!/usr/bin/env bash",
    "set -e",
    ""
]

for album in data['albums']:
    outputFolder = convertedDir + album + '/'
    albumGenerated = os.path.isdir(outputFolder)
    #albumGenerated = 0 
    if not albumGenerated:
        commands.append('echo "Converting ' + album + '..."')
        inputFolder = albumPath + album + '/'
        commands.append('mkdir "' + outputFolder + '"')
        commands.append(conversionProgram + ' "' + inputFolder + '" "' + outputFolder + '"' )
        commands.append(f'pwd')
        commands.append(f'./generate-album-resize.py "{album}" | bash')
        commands.append('')
        


    else:
        commands.append('echo "Album ' + album + ' already converted, skipping."')

commands.append("echo 'Done converting.'")

print("\n".join(commands))
