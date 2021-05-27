**This project is not endorsed or sponsored by Artiphon, Inc in any way.**

## What?

This software enhances your improv music-making experience when using an [Orba](https://artiphon.com/pages/artiphon-shop) connected to a Windows PC over USB, by automatically configuring Orba's key based on a currently playing song.

When playing a song, you often need to change the key programmed into the Orba in order for your improv to sound good. This means determining the correct key, opening the Orba app, and then modifying the key through the app's user-interface.

Enter AutoKey.

Whenever a new song comes on, AutoKey will determine the key signature of the song using Spotify's Analysis API, and then reconfigure your Orba using a series of mouse movements and keystrokes.

The result is a much improved experience when playing and searching for your favorite songs, as you no longer need to worry about the Orba's key being incorrect (mostly - Spotify may not have the key, or it may be inaccurate.)

## Prerequisites

Setting up AutoKey is pretty involved at the moment, but shouldn't be out of reach
if you're familiar with installing software, using text editors, and modifying registry keys.

1. [Windows](https://www.microsoft.com/en-us/software-download/windows10)
2. [YouTube Music](https://music.youtube.com/), [YouTube](https://youtube.com), or [Spotify](https://open.spotify.com/)
3. [Firefox](https://www.mozilla.org/en-US/firefox/download/thanks/)
4. [AutoIt](https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe)
5. [Python](https://docs.python.org/3/using/windows.html) 
6. [Spotify Developer Account](https://developer.spotify.com)

## Setup 

0. Clone this repo or download the zip (green "Code" button to the top-right)
1. Check you have Python 3 installed, and that your system's PATH environment variable includes the path to Python (trying typing `python` in a command-prompt window). 
    - Add dependency: `python -m pip install spotipy` ([get pip](https://pip.pypa.io/en/stable/installing/))

2. Edit the "path" property of "app/orba_autokey.json" to point to the location of "app/orba_autokey.bat" on your computer. Note that you'll need to escape the Windows directory separator, like this: `"path": "C:\\Users\\whatever\\path\\to\\orba-autokey\\src\\app\\orba_autokey.bat"`.
3. Edit "orba_autokey.bat" to refer to the location of "orba_autokey.py" on your computer.
4. Add a registry key containing the path to "orba_autokey.json" on your computer. See [App manifest location](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_manifests#Manifest_location) to find details of the registry key to add.
5. Add environment variables for your Spotify credentials (needed to determine key of a song)
    1. Visit Spotify developer [dashboard](https://developer.spotify.com/dashboard/applications)
    2. Create a new Spotify application, and take note of the `Client ID` and `Client Secret`
    3. Open PowerShell
    4. `$Env:SPOTIPY_CLIENT_ID = "your_client_id"`
    5. `$Env:SPOTIPY_CLIENT_SECRET = "your_client_secret"`
        1. NOTE: spoti**py** is _not_ a typo.
    6. Log out of Windows and back in again

6. In PowerShell, run `python check_config_win.py` (helper script that comes with the Firefox extension template that this project is based on).
    - It should show `Looks good! Give it a try from Firefox.`.
    - If not, the registry key is incorrect or one of the other paths is incorrect - go back to step #2. 
7. Open the Orba app! Almost there!
8. Open `src/app/orba_autokey.au3` and follow the instructions to calibrate the app

## Try it out!

1. Install the Firefox extension
    1. Visit `about:debugging`
    2. Click `This Firefox`
    3. Click `Load Temporary Add-on...`
    4. Select `src\add-on\manifest.json`

2. You should see a new browser action icon in the toolbar
3. Visit one of the supported music streaming sites
4. Play a song
5. Watch your Orba auto tune itself to the correct key
6. If nothing happens, it may be because there is no key information for this song. Try another.
7. If still not working, check errors in a few places:
    1. On `about:debugging`, click `Inspect` on the extension
    2. `Menu > Web Developer > Browser Console`
    3. On the music player page, `Right Click > Inspect > Console`

## Gotchas

If you have multiple music services open, each will be sending data to the app and you'll have some really annoying key changes. 
For now, only use with one streaming service open at once. 

The YouTube support is pretty rudimentary; it just forwards the page title to the app. There's no support for grabbing the artist, so it'll be sending whatever you type in the search box, and then also when you click on a video. 
