function clear1(){
    document.getElementById("answer-result").textContent=""
    document.getElementById("history-value").textContent=""
}
function backspace(){
    const output=document.getElementById("answer-result");
    output.textContent=output.textContent.slice(0,-1);
}
function setscreenvalue(value){
    const output=document.getElementById("answer-result");
    const currentvalue=output.textContent;
    if(
        (
            ["+","-","*","/"].includes(value)&& currentvalue===""
        )
        ||
        (["+","-","*","/"].includes(value)&& ["+","-","*","/"].includes(currentvalue.slice(-1)))
    )
    {
        return;
    }
    output.textContent+=value;
}
function calculate_result(){
    const output=document.getElementById("answer-result");
    const history=document.getElementById("history-value");
    const expression=output.textContent.trim();
    if(expression===""){
        output.textContent="Please enter an expression";
        return;
    }
else{
    const result=eval(expression)
    history.textContent=expression
    output.textContent=result;
}
}
