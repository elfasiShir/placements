var NumberofCertifications = 1;
var NumberofExperiences = 1;
function addCertificationRow() {
  document.querySelector("#certification-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="multiple-detail-container wide-input">
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-certificate1">Certification Name</label>
          <input type="text" required id="input-certificate1" class="user-detail-field"
            placeholder="Machine Learning" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-certupload1">Upload certificate</label>
          <input type="file" required id="input-certupload1" class="user-detail-field" accept="application/pdf"
            placeholder="Upload 10th certificate" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title hide" >.</label>
                  <h4 class="edit-button remove-add-button" onclick="removeRow(this)">Remove</h4>

        </div>
        </div>
      
    `
  );
}
function addProjectRow() {
  document.querySelector("#certification-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="multiple-detail-container wide-input">
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-certificate1">Certification Name</label>
          <input type="text" required id="input-certificate1" class="user-detail-field"
            placeholder="Machine Learning" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-certupload1">Upload certificate</label>
          <input type="file" required id="input-certupload1" class="user-detail-field" accept="application/pdf"
            placeholder="Upload 10th certificate" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title hide" >.</label>
                  <h4 class="edit-button remove-add-button" onclick="removeRow(this)">Remove</h4>

        </div>
        </div>
      
    `
  );
}

function removeRow(input) {
  input.parentNode.parentNode.remove();
}
