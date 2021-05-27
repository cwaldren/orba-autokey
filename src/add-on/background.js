var port = browser.runtime.connectNative("orba_autokey");


var ports = []
// Listens for messages from the python app, which can be viewed
// in the browser console.
port.onMessage.addListener((response) => {
  console.log("orba-autokey: " + response);
});

let portFromContentScript;

function connected(p) {
  ports[p.sender.tab.id] = p
  // Directly forward any messages from the content script to the python app.
  p.onMessage.addListener(function(m) {
    let msg = m.title
    if ('artist' in m) {
      // Combining the track and artist with a comma seems to yield good results from the Spotify API. 
      msg = msg + ", " + m.artist
    }
    port.postMessage(msg)
  });
}

browser.runtime.onConnect.addListener(connected);

// The icon doesn't do anything yet. Perhaps use it to allow user to determine priority between tabs?
browser.browserAction.onClicked.addListener(() => {});