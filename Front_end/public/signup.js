function submitForm() {
    const firstname = document.getElementById('firstname').value;
    const lastname = document.getElementById('lastname').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    formData.append('info', firstname + " " + lastname);

    fetch('/register', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            window.location.href = '/login';
        } else {
            alert('Registration failed');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}
