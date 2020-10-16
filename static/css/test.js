
let textin = document.getElementById("textin");
let find = document.getElementById("find");
let output = document.getElementById("output");

function shows(){
    let textout = "<div>";
    textout += String(textin.value);
    textout += "</div>"
    return output.innerHTML = textout;

}
function Log_out(){
    // window.location.replace("https://www.google.com");
    alert("Log Out")
    return buutton_log_out.location = "https:www.google.com";
}
find.addEventListener("click",shows);
let button_log_out = document.getElementById("button-log-out");
buutton_log_out.addEventListener("click",Log_out)