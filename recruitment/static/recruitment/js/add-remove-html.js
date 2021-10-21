var NumberofCertifications = 1;
var NumberofExperiences = 1;
function addCertificationRow() {
  document.querySelector("#certification-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="three-detail-container wide-input">
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-certificate1">Certification Name</label>
          <input type="text" required id="input-certificate1" class="user-detail-field"
            placeholder="Machine Learning" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title" for="input-issuing-authority">Issuing Authority</label>
          <input type="text" required id="input-issuing-authority" class="user-detail-field"
            placeholder="Coursera" />
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
function addInternshipRow() {
  document.querySelector("#internship-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="field-container personal-information non-resizable-field">
    <div class="three-detail-container wide-input">
    <div class="detail-label-and-field">
      <label class="user-detail-title" for="input-role">Role</label>
      <input type="text" required id="input-role" class="user-detail-field" placeholder="Machine Learning" />
    </div>
    <div class="detail-label-and-field">
      <label class="user-detail-title" for="input-company">Company</label>
      <input type="text" required id="input-company" class="user-detail-field" placeholder="Coursera" />
    </div>
    <div class="detail-label-and-field">
      <label class="user-detail-title" for="input-duration">Duration</label>
      <input type="text" required id="input-duration" class="user-detail-field" placeholder="6 months" />
    </div>
    <div class="detail-label-and-field">
      <label class="user-detail-title hide">.</label>
      <h4 class="edit-button remove-add-button" onclick="removepppRow(this)">Remove</h4>
    </div>
  </div>

  <div class="detail-label-and-field non-resizable-field">
    <label class="user-detail-title" for="input-certupload1">Description</label>
    <textarea type="text" id="input-internships" class="user-detail-field user-detail-text"
      placeholder="Describe Company, Role, Responsibitily"></textarea>
  </div></div>
    `
  );
}
function addProjectRow() {
  document.querySelector("#project-container").insertAdjacentHTML(
    "afterbegin", `
    <div class="field-container personal-information non-resizable-field">
    <div class="three-detail-container wide-input">

      <div class="detail-label-and-field non-resizable-field">
        <label class="user-detail-title" for="input-project-title">Project title</label>
        <input type="text" required id="input-project-title" class="user-detail-field"
          placeholder="Project title" />

      </div>
      <div class="detail-label-and-field non-resizable-field">
        <label class="user-detail-title" for="input-project-contribution">Project contribution</label>
        <select name="project-contribution-type" class="user-detail-field" required
          id="project-contribution-type">
          <option value="Team">Team</option>
          <option value="Individual">Individual</option>
        </select>

      </div>
      <div class="detail-label-and-field">
        <label class="user-detail-title hide">.</label>
        <h4 class="edit-button remove-add-button" onclick="removepppRow(this)">Remove</h4>
      </div>
    </div>
    <div class="detail-label-and-field non-resizable-field">
      <label class="user-detail-title" for="input-project-description">Project Description</label>
      <textarea type="text" id="input-projects" class="user-detail-field user-detail-text"
        placeholder="Tell us about your project. The basic idea, its impact, tech stack etc"></textarea>
    </div>
  </div>
    `
  );
}

function addSocialProfilesRow(){
  document.querySelector("#social-profiles-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="field-container personal-information non-resizable-field">
    <div class="three-detail-container wide-input">

      <select name="input-social-profile-links" class="user-detail-field" required id="input-social-profile-links">
        <option value="GitHub">GitHub</option>
        <option value="LinkedIn">LinkedIn</option>
        <option value="StackOverFlow">Stack Over Flow</option>
        <option value="Others">Others</option>
      </select>

      <h4 class="edit-button remove-add-button" onclick="removeRow(this)">Remove</h4>

    </div>

    <div class="detail-label-and-field">
      <input type="url" required id="social-profile-link" class="user-detail-field"
        placeholder="github profile link" />
    </div>
  </div>
    `
  );
}

function removeRow(input) {
  input.parentNode.parentNode.remove();
}

function removepppRow(input) {
  input.parentNode.parentNode.parentNode.remove();
}
