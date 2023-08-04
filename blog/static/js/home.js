// Play sci-fi sound on opening
const sfSound = document.getElementById("sfSound");

function playSoundOnPageLoad() {
    sfSound.play();
}

window.onload = playSoundOnPageLoad;
