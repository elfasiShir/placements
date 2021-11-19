import {
  toDateTimeString
} from './utils.js';

function addDiv(checkbox, divId) {
  if (checkbox.checked == true) {
    divId.style.display = "block";
  } else {
    divId.style.display = "none";
  }
}

function storeToDeadline() {
  let date = document.getElementById('input-application-deadline').value;
  let time = document.getElementById('input-application-deadline-time').value;
  document.getElementById('deadline').value = toDateTimeString(date, time);
}

document.getElementById('input-application-deadline').addEventListener('change', () => {
  storeToDeadline();
})

document.getElementById('input-application-deadline-time').addEventListener('change', () => {
  storeToDeadline();
})

document.getElementById('branches_allowed_checkboxes').addEventListener('click', () => {
  let branches_allowed = Array.from(document.querySelectorAll('[branch]:checked')).map((el) => el.getAttribute('branch'));
  document.getElementById("branches_allowed_input").value = branches_allowed.join();
})