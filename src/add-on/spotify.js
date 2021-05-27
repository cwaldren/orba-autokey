
let myPort = browser.runtime.connect({name:"document-title-port"});


window.setInterval(myCallback3, 1000);

var payload3 = ""

function myCallback3()
{
    let title = document.body.querySelector('[data-testid="nowplaying-track-link"]').text
    let extra = document.body.querySelector('[data-testid="nowplaying-artist"]').text
    let combined = title + ", " + extra
    if (combined != payload3) {
        console.log("forwarding '" + combined + "' to background worker")
        myPort.postMessage(combined);
        payload3 = combined
    }
}
