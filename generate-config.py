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
sizes = libraryConfig['sizes']

albumNames = [folder for folder in os.listdir(path) if folder[0] != '.']
newData = {}
newData['albums'] = {}
newData['sizes'] = sizes

for album in albumNames:
    albumPath = path + '/' + album
    albumFiles = os.listdir(albumPath)

    rawFilenames = [file for file in albumFiles if validDNG(file)]
    basenames = [fname.split('.')[0] for fname in rawFilenames]
    filenames = [fname + hardcodedExtension for fname in basenames]

    albumObj = {}
    albumObj['raw_filenames'] = rawFilenames
    albumObj['filenames'] = filenames

    if infoFilename in albumFiles:
        info = yaml.load(open(albumPath + '/' + infoFilename))
        if 'cover' in info:
            info['cover'] += '.jpg'
        albumObj['info'] = info
        
    newData['albums'][album] = albumObj
    
prettyPrint(newData)


