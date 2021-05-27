let myPort = browser.runtime.connect({name:"document-title-port"});


window.setInterval(myCallback, 1000);

var payload = ""

function myCallback()
{
    let title = document.getElementsByClassName("title style-scope ytmusic-player-bar")[0].title
    let extra = document.getElementsByClassName("byline style-scope ytmusic-player-bar complex-string")[0].title.split(" • ")
    let combined = title + ", " + extra[0]
    if (combined != payload) {
        console.log("forwarding '" + combined + "' to background worker")
        myPort.postMessage(combined);
        payload = combined
    }
}
