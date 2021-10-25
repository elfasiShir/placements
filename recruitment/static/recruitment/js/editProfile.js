function eduGapDetails(checkbox){
    if(checkbox.checked == true){
        document.getElementById("educationGap").style.display="flex";
    }else{
        document.getElementById("educationGap").style.display="none";
    }
}

function set_display_property(el_id, display) {
    document.getElementById(el_id).style.display = display;
}

function backlogs(){
    var check = document.getElementById("input-backlogs");
    if(check.value == "OutstandingBacklogs"){
        set_display_property("outBacklogs", "flex");
        set_display_property("backlogs-cleared", "none");
    }else if(check.value == "NoOutstandingBacklogs"){
        set_display_property("backlogs-cleared", "flex");
        set_display_property("outBacklogs", "none");
    }
    else{
        set_display_property("outBacklogs", "none");
        set_display_property("backlogs-cleared", "none");
    }
}