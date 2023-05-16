function checkUserExists() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/login_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: email,
            password: password
        })
    })
        .then(response => {
            if (response.ok) {
                // User exists
                window.location.href = '/home_jv';
            } else {
                // User does not exist
                alert('Invalid credentials');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
