/*
On startup, connect to the "ping_pong" app.
*/
var port = browser.runtime.connectNative("orba_autokey");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("autokey: " + response);
});



let portFromCS;

function connected(p) {
  portFromCS = p;
  portFromCS.onMessage.addListener(function(m) {
    port.postMessage(m)
  });
}

browser.runtime.onConnect.addListener(connected);

browser.browserAction.onClicked.addListener(() => {
  portFromCS.postMessage("ACTION CLICKED")
});