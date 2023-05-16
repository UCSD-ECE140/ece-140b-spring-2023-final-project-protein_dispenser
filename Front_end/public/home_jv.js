window.addEventListener('DOMContentLoaded', (event) => {
  let editButtons = document.querySelectorAll('[id^="edit_sup_"]');
  let saveButtons = document.querySelectorAll('[id^="save_btn_"]');
  let cancelButtons = document.querySelectorAll('[id^="cancel_btn_"]');

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
