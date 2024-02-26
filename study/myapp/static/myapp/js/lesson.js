// function playAudio(id) {
//   var audio = document.getElementById(id);
//   audio.play();
// }

var currentlyPlaying = null;

function playAudio(id) {
    var audio = document.getElementById(id);

    if (currentlyPlaying && currentlyPlaying !== audio) {

        currentlyPlaying.pause();

        var prevButton = document.querySelector('[data-audio="' + currentlyPlaying.id + '"]');
        if (prevButton) {
            prevButton.disabled = false;
        }
    }

    audio.play();
    currentlyPlaying = audio;

    var button = document.querySelector('[data-audio="' + id + '"]');
    if (button) {
        button.disabled = true;
    }
}
