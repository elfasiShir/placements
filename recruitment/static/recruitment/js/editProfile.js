function eduGapDetails(checkbox){
    if(checkbox.checked == true){
        document.getElementById("education-gap").style.display="flex";
    }else{
        document.getElementById("education-gap").style.display="none";
    }
}

function set_display_property(el_id, display) {
    document.getElementById(el_id).style.display = display;
}

function backlogs(){
    var check = document.getElementById("input-backlogs");
    if(check.value == "OB"){  // Outstanding backlogs
        set_display_property("out-backlogs", "flex");
        set_display_property("backlogs-cleared", "none");
    }else if(check.value == "NOB"){  // No outstanding backlogs
        set_display_property("backlogs-cleared", "flex");
        set_display_property("out-backlogs", "none");
    }else{
        set_display_property("out-backlogs", "none");
        set_display_property("backlogs-cleared", "none");
    }
}