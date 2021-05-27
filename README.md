# Prerequisites

1. [Windows](https://www.microsoft.com/en-us/software-download/windows10)
2. [YouTube Music](https://music.youtube.com/), [YouTube](https://youtube.com), or [Spotify](https://open.spotify.com/)
3. [Firefox](https://www.mozilla.org/en-US/firefox/download/thanks/)
4. [AutoIt](https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.exe)
5. [Python](https://docs.python.org/2/using/windows.html)


## Setup ##

2. Check you have Python installed, and that your system's PATH environment variable includes the path to Python (trying typing `python` in a command-prompt window). 
2. Edit the "path" property of "ping_pong.json" to point to the location of "ping_pong_win.bat" on your computer. Note that you'll need to escape the Windows directory separator, like this: `"path": "C:\\Users\\MDN\\native-messaging\\app\\ping_pong_win.bat"`.
3. Edit "ping_pong_win.bat" to refer to the location of "ping_pong.py" on your computer.
4. Add a registry key containing the path to "ping_pong.json" on your computer. See [App manifest location ](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_manifests#Manifest_location) to find details of the registry key to add.
5. Add environment variables for spotipy 
To assist in troubleshooting on Windows, there is a script called `check_config_win.py`. Running this from the command line should give you an idea of any problems.

## Try it out!

1. Install the Firefox 

Then just install the add-on as usual, by visiting about:debugging, clicking "Load Temporary Add-on", and selecting the add-on's "manifest.json".

You should see a new browser action icon in the toolbar. Open the console ("Tools/Web Developer/Browser Console" in Firefox), and click the browser action icon. You should see output like this in the console:

    Sending: ping
    Received: pong

If you don't see this output, see the [Troubleshooting guide](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_messaging#Troubleshooting) for ideas.
