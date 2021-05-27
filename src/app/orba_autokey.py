#!/usr/bin/env python

import sys
import json
import struct
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



# Python 3.x version
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

lastKey = ""
lastMode = ""
lastTitle = "whatever"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


while True:
    title = getMessage()
    if title == lastTitle:
        continue

    lastTitle = title
    results = spotify.search(q='track:' + title, type='track')
    if len(results) == 0:
        sendMessage(encodeMessage("no results for " + title))
        continue
    if len(results['tracks']) == 0:
        sendMessage(encodeMessage("no tracks for " + title))
        continue
    if len(results['tracks']['items']) == 0:
        sendMessage(encodeMessage("no items for " + title))
        continue

    id = results['tracks']['items'][0]['id']
    analysis = spotify.audio_analysis(id)["track"]
    key = analysis["key"]
    mode = analysis["mode"] 
    if key != lastKey or mode != lastMode:
        lastKey = key
        lastMode = mode
        sendMessage(encodeMessage("spotify returned key " + str(key) + ", " +str(mode)))
        subprocess.check_call([r"C:\Program Files (x86)\AutoIt3\AutoIt3.exe", r"C:\Users\Casey\Documents\OrbaRust\src\app\orba_autokey.au3", str(lastKey), str(lastMode)])
   
   
    
