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
        document.getElementById("backlogs-cleared").style.display="none";
    }else if(check.value == "NoOutstandingBacklogs"){
        document.getElementById("backlogs-cleared").style.display="flex";
        document.getElementById("outBacklogs").style.display="none";
    }
    else{
        document.getElementById("outBacklogs").style.display="none";
        document.getElementById("backlogs-cleared").style.display="none";
    }
}