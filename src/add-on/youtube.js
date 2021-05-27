let myPort = browser.runtime.connect({name:"document-title-port"});


window.setInterval(myCallback2, 1000);

var payload2 = ""
function myCallback2()
{
    let title = document.title.replace(" - YouTube", "").replace(/ *\([^)]*\) */g, "")
    if (payload2 !== title) {
        console.log("forwarding '" +title + "' to background worker")
        myPort.postMessage(title);
        payload2 = title
    }
}
