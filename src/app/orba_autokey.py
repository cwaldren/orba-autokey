#!/usr/bin/env python

import sys
import json
import struct
import subprocess
import os
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
    return encodedLength, encodedContent

def reply(msg):
    length, content = encodeMessage(msg)
    sys.stdout.buffer.write(length)
    sys.stdout.buffer.write(content)
    sys.stdout.buffer.flush()

# What follows is somewhat inelegant python. Sorry.

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

    results = spotify.search(q=f'track:{query}', type='track')
    if len(results) and len(results['tracks']) and len(results['tracks']['items']) and len(results['tracks']['items'][0]):
        pass
    else:
        reply(f"no items for {query}")
        continue

    id = results['tracks']['items'][0]['id']
    analysis = spotify.audio_analysis(id)['track']
    key, mode = analysis['key'], analysis['mode']
    if key != lastKey or mode != lastMode:
        lastKey, lastMode = key, mode
        reply(f'"{query}", {keys[key]} {modes[mode]}')
        subprocess.check_call([os.getenv("AUTOIT_EXE"), "orba_autokey.au3", str(lastKey), str(lastMode)])
