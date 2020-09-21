function clicks(){

    return window.open("https://www.google.com");

}
let home = document.getElementById("Home");
home.addEventListener("click",clicks);

let textin = document.getElementById("textin");
let find = document.getElementById("find");
let output = document.getElementById("output");

function shows(){
    let textout = "<p>";
    textout += String(textin.value);
    textout += "</p>"
    return output.innerHTML = textout;

}
find.addEventListener("click",shows);