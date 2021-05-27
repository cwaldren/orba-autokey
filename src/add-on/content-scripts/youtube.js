let port = browser.runtime.connect({name:"youtube"});

window.setInterval(function(){
    let title = document.title.replace(" - YouTube", "").replace(/ *\([^)]*\) */g, "")    
    if (title != "YouTube") {
        port.postMessage({title: title});
    }
}, 1000);

