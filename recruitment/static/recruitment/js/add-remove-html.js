var NumberofCertifications = 1;
var NumberofExperiences = 1;
function addCertificationRow() {
  document.querySelector("#certification-container").insertAdjacentHTML(
    "afterbegin",
    `
    <div class="multiple-detail-container wide-input">
      
        <div class="detail-label-and-field">
          <label class="detail-title" for="input-certificate1">Certification Name</label>
          <input type="text" required id="input-certificate1" class="detail-field"
            placeholder="Machine Learning" />
        </div>
        <div class="detail-label-and-field">
          <label class="detail-title" for="input-issuing-authority">Issuing Authority</label>
          <input type="text" required id="input-issuing-authority" class="detail-field"
            placeholder="Coursera" />
        </div>
        <div class="detail-label-and-field">
          <label class="detail-title" for="input-certupload1">Upload certificate</label>
          <input type="file" required id="input-certupload1" class="detail-field" accept="application/pdf"
            placeholder="Upload 10th certificate" />
        </div>
        <div class="detail-label-and-field">
          <label class="user-detail-title hide" >.</label>
          <button type="button" class="edit-button remove-add-button" onclick="removeRow(this)">-</button>
        </div>
        </div>
    `
  );
}

function scrolltoelement(element) {
  window.scrollTo({
    top: element.offsetTop,
    behavior: "smooth",
  });
}


function addRound() {
  document.querySelector("#forms-parent").insertAdjacentHTML(
    "beforeend",
    `      <form action="" method="post" class=" flex-col add-round-form" >
        <select class="detail-field is-last-round"   data-target=".selective-round-view-container">
          <option value="notLastRound" data-show=".not-last-round-option">Not last round</option>
          <option value="lastRound" data-show=".last-round-option">Is last round</option>
        </select>

<div class="selective-round-view-container">
          <div class="flex-col not-last-round-option hide">

       
        <h2>Round 1 </h2>
        <div class="flex-row">
          <div class="flex-col">
            <label class="detail-title required" for="input-round-name">Round Name</label>
            <input type="text" name="input-round-name" class="detail-field" id="input-round-name" required placeholder="Technical round">
            
          </div>
          
          <div class="flex-col ">
             <label class="detail-title " for="input-round-venue">Venue</label>
             <input type="text"  id="input-round-venue" class="detail-field" 
               placeholder="Academic block room 19" />
             
          </div>
          <div class="flex-col ">
             <label class="detail-title " for="input-round-link">Link</label>
             <input type="url"  id="input-round-link" class="detail-field" 
               placeholder="" />
             
          </div>
           

        </div>
        <div class="flex-row">
          <div class="flex-col " style="width: 100%;">
             <label class="detail-title  " for="input-round-procedure">Procedure</label>
             <textarea  id="input-round-procedure" class="detail-field user-detail-text" 
               placeholder="" ></textarea>
             
          </div>
        </div>
        
        
        
        <div class="flex-col">
          <label class="detail-title required " for="input-round-from-day">Reporting time</label>
          <div class="flex-row">
              <input type="date"  id="input-round-from-day" class="detail-field" 
              placeholder="" />
              <input type="time"  id="input-round-from-time" class="detail-field" 
              placeholder="10:00 AM" value="23:59:00" />           
          </div>
        </div>
        
        
        <label class="detail-title " for="input-round-query">For Any Queries</label>
        <div class="flex-row">
            
            <div class="flex-col">
              <label class="detail-title " for="input-round-contact">Contact No.</label>
              <input type="tel" name="input-round-contact" class="detail-field" id="input-round-contact" >
              
            </div>
            <div class="flex-col">
              <label class="detail-title " for="input-round-email">Email</label>
              <input type="email" name="input-round-email" class="detail-field" id="input-round-email" >
              
            </div>
          </div>
        

      

        </div>
         <div class="flex-col last-round-option hide">
           <div class="flex-col">
             <label for="upload-offer-letter" class="detail-label">Upload Offer Letter for Selected Students</label>
             <input type="file" name="" id="upload-offer-letter" class="detail-field" accept="application/pdf" placeholder="upload offer letter">
            </div>
            <div class="flex-col">
              <label class="detail-title required" for="input-congrats-message">Congratulations Message for Selected Students</label>
        <textarea  id="input-congrats-message" class="detail-field user-detail-text"
        placeholder="type your message here"></textarea>
            </div>


        </div>

</div>
        


       
        <div class="flex-row flex-spbw ">
  <div >
    <a href="#add-students-modal" rel="modal:open"> <h4 class="edit-button remove-add-button" >Add Students</h4></a>
   
  </div>
  <div >
  <h4 class="edit-button remove-add-button" onclick="removepppRow(this)">remove Round</h4>
  
  <input type="submit" class="edit-button remove-add-button" value="Save Round">
</div>
        </div>
        <hr/>
      </form>`)
    let elemarr = document.getElementsByClassName("add-round-form");
  let elem = elemarr[elemarr.length - 1];
  
   $(document).find('.is-last-round').last().trigger('change');
   scrolltoelement(elem);

    }



function addInternshipRow() {
  document.querySelector("#internship-container").insertAdjacentHTML(
    "afterbegin",
    `<div class="field-container personal-information non-resizable-field">
    <div class="three-detail-container wide-input">
    <div class="detail-label-and-field">
      <label class="detail-title" for="input-area-of-internship">Area of Internship</label>
      <input type="text" required id="input-area-of-internship" class="detail-field" placeholder="Machine Learning" />
    </div>
    <div class="detail-label-and-field">
      <label class="detail-title" for="input-company">Company</label>
      <input type="text" required id="input-company" class="detail-field" placeholder="Coursera" />
    </div>
    <div class="detail-label-and-field">
      <label class="detail-title" for="input-duration">Duration</label>
      <input type="text" required id="input-duration" class="detail-field" placeholder="6 months" />
    </div>
    <div class="detail-label-and-field">
      <label class="detail-title hide">.</label>
      <h4 class="edit-button remove-add-button" onclick="removepppRow(this)">Remove</h4>
    </div>
  </div>

  <div class="detail-label-and-field non-resizable-field">
    <label class="detail-title" for="input-certupload1">Description</label>
    <textarea type="text" id="input-internships" class="detail-field user-detail-text"
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
        <label class="detail-title" for="input-project-title">Project title</label>
        <input type="text" required id="input-project-title" class="detail-field"
          placeholder="Project title" />

      </div>
      <div class="detail-label-and-field non-resizable-field">
        <label class="detail-title" for="input-project-contribution">Project contribution</label>
        <select name="project-contribution-type" class="detail-field" required
          id="project-contribution-type">
          <option value="Team">Team</option>
          <option value="Individual">Individual</option>
        </select>

      </div>
      <div class="detail-label-and-field">
        <label class="detail-title hide">.</label>
        <h4 class="edit-button remove-add-button" onclick="removepppRow(this)">Remove</h4>
      </div>
    </div>
    <div class="detail-label-and-field non-resizable-field">
      <label class="detail-title" for="input-project-description">Project Description</label>
      <textarea type="text" id="input-projects" class="detail-field user-detail-text"
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

      <select name="input-social-profile-links" class="detail-field" required id="input-social-profile-links">
        <option value="GitHub">GitHub</option>
        <option value="LinkedIn">LinkedIn</option>
        <option value="StackOverFlow">Stack Over Flow</option>
        <option value="Others">Others</option>
      </select>

      <h4 class="edit-button remove-add-button" onclick="removeRow(this)">Remove</h4>

    </div>

    <div class="detail-label-and-field">
      <input type="url" required id="social-profile-link" class="detail-field"
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
