const myDialog = document.querySelector('#myDialog');
const deleteButton = document.querySelector('#delete');
const confirmButton = document.querySelector('#confirm');
const cancelButton = document.querySelector('#cancel');

deleteButton.addEventListener('click', () => {
  myDialog.showModal();
});

confirmButton.addEventListener('click', () => {
    window.location.href = '/Front end/index.html';
});

cancelButton.addEventListener('click', () => {
  myDialog.closeModal();
});