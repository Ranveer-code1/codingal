function validate(){
    var a =document.getElementById("email");
    var b =document.getElementById("msg");
    msg.textContent="";
    if(!email.value.includes("@")){
        msg.textContent="Please enter a valid email id";
        email.style.border="1px solid green";
        return false;
    }
    return true;
    }
    var ranveer=document.getElementById("a").innerHTML;
    alert("This form is highly confidentia, DO NOT SHARE"+ranveer);