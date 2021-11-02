function filter(element) {
    var value = $(element).val().toLowerCase();

    $("#student-list > li").each(function () {
        if ($(this).text().toLowerCase().search(value) > -1) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

function selectedFilter(element) {
    var value = $(element).val().toLowerCase();

    $("#added-student-list > li").each(function () {
        if ($(this).text().toLowerCase().search(value) > -1) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

function addStudent(element) {
    let row = element.parentNode.parentNode;
    let roll = row.getElementsByClassName('student-roll-number')[0].innerText;
    let name = row.getElementsByClassName('student-name')[0].innerText;
    let student_id = row.getAttribute("user_id");
    document.querySelector("#added-student-list").insertAdjacentHTML(
        "afterbegin",
        `<li user_id="${student_id}"><div class="flex-row student-row"> <h3 class="student-roll-number">${roll} </h3> <h3 class="student-name">${name}</h3>  <div class="student-row-button remove-add-button"onclick="removeStudent(this)">&#10005;</div></div></li>
`
    );
    row.remove();

    let selected_student_list_html = document.querySelector("#selected-student-list-input").innerHTML;
    selected_student_list_html += `<input type="hidden" name="selected" value="${student_id}">`;
    document.querySelector("#selected-student-list-input").innerHTML = selected_student_list_html;

}

function removeStudent(element) {
    let row = element.parentNode.parentNode;
    let roll = row.getElementsByClassName('student-roll-number')[0].innerText;
    let name = row.getElementsByClassName('student-name')[0].innerText;
    let student_id = row.getAttribute("user_id");
    document.querySelector("#student-list").insertAdjacentHTML(
        "afterbegin",
        `<li user_id="${student_id}"><div class="flex-row student-row"> <h3 class="student-roll-number">${roll} </h3> <h3 class="student-name">${name}</h3>  <div class="student-row-button remove-add-button"onclick="addStudent(this)">&#43;</div></div></li>
`
    );
    row.remove();

    let student_list = document.querySelector("#selected-student-list-input");
    let student_input = student_list.querySelector(`input[value="${student_id}"]`);
    student_input.remove();
}
