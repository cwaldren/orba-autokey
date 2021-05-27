let port = browser.runtime.connect({name:"spotify"});

window.setInterval(function(){
    let title = document.body.querySelector('[data-testid="nowplaying-track-link"]').text;
    let artist = document.body.querySelector('[data-testid="nowplaying-artist"]').text;
    port.postMessage({title: title, artist: artist});
}, 1000);

