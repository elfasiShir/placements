function eduGapDetails(checkbox){
    if(checkbox.checked == true){
        document.getElementById("educationGap").style.display="flex";
    }else{
        document.getElementById("educationGap").style.display="none";
    }
}

function backlogs(){
    var check = document.getElementById("input-backlogs");
    if(check.value == "OutstandingBacklogs"){
        document.getElementById("outBacklogs").style.display="flex";
    }else{
        document.getElementById("outBacklogs").style.display="none";
    }
}