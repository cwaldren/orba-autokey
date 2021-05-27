#!/usr/bin/env python

import sys
import json
import struct
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def reply(msg):
    sendMessage(encodeMessage(msg))

# What follows is inelegant python. Sorry.

# Holds previously determined key of song
lastKey = ""
# Holds previously determined mode of song
lastMode = ""
# Holds previous query from the extension
lastQuery = ""

# Used to pretty-print the results back to the extension; only useful for debugging right now.
keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
modes = ["Minor", "Major"]

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

while True:
    query = getMessage()
    if query == lastQuery:
        continue
    lastQuery = query

    results = spotify.search(q='track:' + query, type='track')
    if len(results) == 0:
        reply("no results for " + query)
        continue
    if len(results['tracks']) == 0:
        reply("no tracks for " + query)
        continue
    if len(results['tracks']['items']) == 0:
        reply("no items for " + query)
        continue

    id = results['tracks']['items'][0]['id']
    analysis = spotify.audio_analysis(id)["track"]
    key = analysis["key"]
    mode = analysis["mode"] 
    if key != lastKey or mode != lastMode:
        lastKey = key
        lastMode = mode
        reply("\"" + query + "\", " + keys[key] +" " + modes[mode])
        subprocess.check_call([r"C:\Program Files (x86)\AutoIt3\AutoIt3.exe", r"C:\Users\Casey\Documents\OrbaRust\src\app\orba_autokey.au3", str(lastKey), str(lastMode)])
   
   
    
