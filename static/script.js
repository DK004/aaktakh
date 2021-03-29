const apiKey_voice = "1f44c827c9794ceeb4f5d708fe7c6cd4";


let card = document.getElementsByClassName('card');
// for(i=0;i<card.length;i++){
//   console.log(card[i].innerText);
// }

let khabare = document.getElementById("khabare");
let read = document.getElementById("read");
let stopbtn = document.getElementById("stop");

function readAll(){
    read.style.display = 'none';
    stopbtn.style.display = 'flex';
    console.log("in the function")
    // for(i=0;i<1;i++){
    VoiceRSS.speech({
        key: "1f44c827c9794ceeb4f5d708fe7c6cd4",
        src: khabare.innerText,
        hl: 'en-in',
        v: 'Ajit',
        r: 3, 
        c: 'mp3',
        f: '44khz_16bit_stereo',
        ssml: false
    });
// }
}







function stopReading(){
  location.reload();
}