function checkUserExists() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/login_check', {
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
                // User exists, redirect to the desired page
                window.location.href = '/home_jv.html';
            } else {
                // User does not exist or invalid credentials
                alert('Invalid credentials');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
