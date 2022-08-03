let music;
let previous_music_element;

function play_music(ele) {
    // todo: check if music is playing
    if (music != undefined){
        if (music.paused == false){
            stop_music(previous_music_element);
        }
    }

    let music_path = ele.id;
    music = new Audio(music_path);
    music.play();
    let play_icon = ele.children[0];
    play_icon.className = "fa fa-pause fa-5x";

    ele.setAttribute('onClick','stop_music(this)');
    previous_music_element = ele
}

function stop_music(ele){
    music.pause();
    music.currentTime = 0;
    let pause_icon = ele.children[0];
    pause_icon.className = "fa fa-play fa-5x";

    ele.setAttribute('onClick','play_music(this)');
    previous_music_element = ele;
}