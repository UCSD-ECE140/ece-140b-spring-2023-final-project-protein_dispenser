window.addEventListener('DOMContentLoaded', (event) => {
  let editButtons = document.querySelectorAll('[id^="edit_sup_"]');
  let saveButtons = document.querySelectorAll('[id^="save_btn_"]');
  let cancelButtons = document.querySelectorAll('[id^="cancel_btn_"]');

  let dispenseButtons = document.querySelectorAll('[id^="dis_sup_"]');

  dispenseButtons.forEach(button => {
    let supplementNumber = button.id.split('_')[2]; // Get the supplement number
    let servingInput = document.querySelector(`#sup_serv_${supplementNumber}`);

    button.addEventListener('click', () => {
      // Grab the current serving size
      let servingSize = servingInput.value;

      // Send a POST request to the /dispense route
      fetch('/dispense', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          supplementNumber: supplementNumber,
          servingSize: servingSize
        })
      })
        .then(response => response.json())
        .then(data => {
          console.log(data); // Log the response data for now, you can replace this with other actions
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
  });


  editButtons.forEach(button => {
    let supplementNumber = button.getAttribute('data-supplement');
    let dialog = document.querySelector(`#edit_dialog_${supplementNumber}`);

    button.addEventListener('click', () => {
      dialog.showModal();
    });
  });

  saveButtons.forEach(button => {
    let supplementNumber = button.getAttribute('data-supplement');
    let dialog = document.querySelector(`#edit_dialog_${supplementNumber}`);
    let nameInput = document.querySelector(`#sup_name_${supplementNumber}`);
    let supplementName = document.querySelector(`.supplement_container:nth-child(${supplementNumber}) h3`);

    button.addEventListener('click', (event) => {
      event.preventDefault();
      // Update the supplement name
      supplementName.textContent = nameInput.value;
      dialog.close();
    });
  });

  cancelButtons.forEach(button => {
    let supplementNumber = button.getAttribute('data-supplement');
    let dialog = document.querySelector(`#edit_dialog_${supplementNumber}`);

    button.addEventListener('click', (event) => {
      event.preventDefault();
      dialog.close();
    });
  });

  
});
