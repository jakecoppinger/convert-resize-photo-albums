#!/usr/bin/env python3
import json, os, re
from pprint import pprint
from subprocess import call
import yaml

def prettyPrint(o):
    print(json.dumps(o, sort_keys=True,
        indent=4, separators=(',', ': ')))

def validDNG(filename):
    return filename.split('.')[-1].lower() in ['cr2', 'dng']

infoFilename = 'info.yaml'
hardcodedExtension = '.jpg'

libraryConfig = json.load(open('library.json'))
path = libraryConfig['album_path']


albumNames = [folder for folder in os.listdir(path) if folder[0] != '.']
newData = {}
newData['albums'] = {}

newData['sizes'] = libraryConfig['sizes']
newData['album_order'] = libraryConfig['album_order']
newData['fallback_size'] = libraryConfig['fallback_size']

for album in albumNames:
    albumPath = path + '/' + album
    albumFiles = os.listdir(albumPath)

    rawFilenames = [file for file in albumFiles if validDNG(file)]
    basenames = [fname.split('.')[0] for fname in rawFilenames]
    # filenames = [fname + hardcodedExtension for fname in basenames]

    albumObj = {}
    albumObj['raw_filenames'] = rawFilenames
    albumObj['basenames'] = basenames

    if infoFilename in albumFiles:
        albumObj['info'] = yaml.load(open(albumPath + '/' + infoFilename))
    
    # if not ('hidden' in albumObj['info'] and albumObj['info']['hidden'] == True):
    newData['albums'][album] = albumObj
    
prettyPrint(newData)


