import {
  toDateTimeString
} from './utils.js';



document.getElementById('backlogCheckBox').addEventListener('change', function() {
  const backlogLimitationsDiv=document.getElementById('backlogLimitations');
  if (this.checked) {
    backlogLimitationsDiv.style.display = "block";
  } else {
    backlogLimitationsDiv.style.display = "none";
   
  }
});


document.getElementById('input-application-deadline').addEventListener('change', () => {
  storeToDeadline();
})

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

const updateBranchCheckBoxes = () => {
    let branches_allowed = Array.from(document.querySelectorAll('[branch]:checked')).map((el) => el.getAttribute('branch'));
  document.getElementById("branches_allowed_input").value = branches_allowed.join();
}

document.getElementById('branches_allowed_checkboxes').addEventListener('click', () => {
  updateBranchCheckBoxes();
})

const element = document.querySelector('#post-job-form');
element.addEventListener('submit', event => {
  storeToDeadline() ;
  updateBranchCheckBoxes();

});

