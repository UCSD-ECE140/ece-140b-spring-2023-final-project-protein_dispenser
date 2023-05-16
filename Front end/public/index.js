const signUpDialog = document.getElementById('sign_up_dialog');
const signUpDialogButton = document.getElementById('sign_up_dialog_button');
const cancelButton = document.getElementById('cancel');
const signInButton = document.getElementById('sign_in_button');

const nameForm = document.getElementById('sign_in_email').value;
const passForm = document.getElementById('sign_in_password').value;

signUpDialogButton.addEventListener('click', () => {
  signUpDialog.showModal();
});

cancelButton.addEventListener('click', () => {
  signUpDialog.close();
});

signInButton.addEventListener('click', () => {
  // console.log(nameForm.length)
  //   if (nameForm.length>0 && passForm.length>0) {
      location.href = "/home_jv.html";
    // }
});