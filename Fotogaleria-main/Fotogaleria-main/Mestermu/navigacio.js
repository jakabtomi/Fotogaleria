
document.addEventListener('keydown', function(event) {
    if (event.keyCode === 37) {
   
        lightbox.prev();
    } else if (event.keyCode === 39) {
      
        lightbox.next();
    }
});
