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
    let roll = row.childNodes[0].childNodes[1].innerText;
    let name = row.childNodes[0].childNodes[3].innerText;
    document.querySelector("#added-student-list").insertAdjacentHTML(
        "afterbegin",
        `<li><div class="flex-row student-row"> <h3 class="student-roll-number">${roll} </h3> <h3 class="student-name">${name}</h3>  <div class="student-row-button remove-add-button"onclick="removeStudent(this)">&#10005;</div></div></li>
`
    );
    row.remove();

}

function removeStudent(element) {
    let row = element.parentNode.parentNode;
    let roll = row.childNodes[0].childNodes[1].innerText;
    let name = row.childNodes[0].childNodes[3].innerText;
    document.querySelector("#student-list").insertAdjacentHTML(
        "afterbegin",
        `<li><div class="flex-row student-row"> <h3 class="student-roll-number">${roll} </h3> <h3 class="student-name">${name}</h3>  <div class="student-row-button remove-add-button"onclick="addStudent(this)">&#43;</div></div></li>
`
    );
    row.remove();

}