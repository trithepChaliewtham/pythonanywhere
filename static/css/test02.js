function click(){
    return window.location.href = "index";
}
function showoutput(){
    showInform.innerHTML = "";
    output.innerHTML = "";
    let text = "";
    text += "<style>";
    text += ".color-p{color:Yellow;animation-name:getmove;position:relative;animation-delay:1s;animation-duration:4s;animation-iteration-count: infinite;z-index:2;}";
    text += ".color-p:hover{color:blue;transition:3s;}"
    text += ".background-item{padding:0.5rem;width:5%;left:40vh;top:10vh;border:2px solid black;background-color:black;animation-name:background-item-move;position:relative;animation-delay:1s;animation-duration:4s;animation-iteration-count: infinite;}";
       
    text += "@keyframes getmove{0% {left:0px;top:0px;} 25%{left:200px;top:0px;} 50%{left:200px;top:200px;} 75%{left:0px;top:200px;} 100%{left:0px;top:0px;}}";
    text += "@keyframes background-item-move{0% {top:2250px;border-radius:0;} 100%{border-radius:10%}}";
    
    text += "</style>";
    text += "<p class=color-p>Reading document</p>";
    text += "<div class=container-circle>";
    text += "<div class=background-item></div>";
    text += "</div>";
   
    conbody.style.height = "1300px";
    return output.innerHTML = text;
}
function formLogin(){
    output.innerHTML = "";
    let stringout = "";
    stringout += "<div style=margin-bottom:-2rem;cursor:pointer;>Log In from</div>";
    stringout += "<br>";
    stringout += "<form>";
    stringout += "<font size = 5 color = black>Account : </font><input type=text placeholder=ID name=username><br>";
    stringout += "<font size = 5 color = black>Password : </font><input type=password placeholder=password name=password><br>";
    stringout += "<button id = button type=submit style=cursor:pointer;> Submit";
    stringout += "</button>";
    stringout += "<script>alert(hello);</script>"
    stringout += "</form>";
    
    output.innerHTML = stringout;
}

function Signup(){
    output.innerHTML = "";
    let stringout2 = "";
    stringout2 += "Register from";
    stringout2 += "<br>";
    stringout2 += "<form>";
    stringout2 += "<font size = 5 color = black>Account : </font><input type=text placeholder=ID name=username autocomplete=off><br>";
    stringout2 += "<font size = 5 color = black>Password : </font><input type=password placeholder=password name=password><br>";
    stringout2 += "<font size = 5 color = black>Re-Password : </font><input type=password placeholder=password name=password><br>";
    stringout2 += "<button id = button type=submit style=cursor:pointer;> Submit";
    stringout2 += "</button>";
    stringout2 += "</form>";
    return output.innerHTML = stringout2;
}


function showimg(){
    showInform.innerHTML = "";
    output.innerHTML = "";
    let imgshow = "";
    let imgshow2 = "";
    let imgshow3 = "";
    let imgshow4 = "";
    let style = "<style>";
    style += ".imgshow{width:80%;heigth:60%;border-radius:4px;box-shadow: 2.5px 2px 5px red;cursor:pointer;margin-right:5rem;} .imgshow:hover{padding:0.5rem;box-shadow: 2.5px 2px 5px yellow;}";
    style += ".imgshow2{width:80%;heigth:40%;border-radius:4px;box-shadow: 2.5px 2px 5px blue;cursor:pointer;margin-top:1.5rem;margin-left:5rem;} .imgshow2:hover{padding:0.5rem;box-shadow: 2.5px 2px 5px pink;}";
    style += ".imgshow3{width:80%;heigth:40%;border-radius:4px;box-shadow: 2.5px 2px 5px blue;cursor:pointer;margin-top:1.5rem;margin-left:-5rem;} .imgshow3:hover{padding:0.5rem;box-shadow: 2.5px 2px 5px pink;}";
    style += ".imgshow4{width:80%;heigth:40%;border-radius:4px;box-shadow: 2.5px 2px 5px blue;cursor:pointer;margin-top:1.5rem;margin-left:5rem;} .imgshow4:hover{padding:0.5rem;box-shadow: 2.5px 2px 5px pink;}";
    
    style += ".a{text-decoration:none;}";
    style += ".a2{text-decoration:none;}";
    style += ".a3{text-decoration:none;}";
    style += ".a4{text-decoration:none;}";
    style += "</style>"
    imgshow += style;
    imgshow += '<img id=image01 src=static/FruitPic.jpg class=imgshow>';
    imgshow2 += '<img id=image02 src=static/1.jpg class=imgshow2>';
    imgshow3 += '<img id=image03 src=static/Aloe01.jpg class=imgshow3>';
    imgshow4 += '<img id=image04 src=static/FruitPic2.jpg class=imgshow4>';
    imgshow += imgshow2 ;
    imgshow += imgshow3 ;
    imgshow += imgshow4 ;

   
    
    
    

    let all = eval("imgshow");
    
    
    
    
    return output.innerHTML = all;

}
function changestyle1(){
    return conbody.style.height = "1500px";
}

function changestyle2(){
    return conbody.style.height = "auto";
}



document.getElementById("h2").addEventListener("click",click);

let showprice = document.getElementById("showprice");
if(showprice.addEventListener){
    showprice.addEventListener("click",showoutput);
    
}


let output = document.getElementById("outputbody");

let conbody = document.getElementById("conbody");


// when click at picture bar --> call changestyle function
let img2 = document.getElementById("img").addEventListener("click",changestyle2);

// when click show Price --> remove changestyle function



//let output2 = document.getElementById("outputbody2");
let img = document.getElementById("img").addEventListener("click",showimg);

let showInform = document.getElementById("ShowInform")


function infuc(){return alert("Something")}

