let port = browser.runtime.connect({name:"youtube-music"});

window.setInterval(function(){
    let title = document.getElementsByClassName("title style-scope ytmusic-player-bar")[0].title;
    let artist = document.getElementsByClassName("byline style-scope ytmusic-player-bar complex-string")[0].title.split(" • ")[0];
    port.postMessage({title: title, artist: artist});
}, 1000);

