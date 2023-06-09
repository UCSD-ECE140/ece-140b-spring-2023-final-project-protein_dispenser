document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('sshForm').addEventListener('submit', function (event) {
        event.preventDefault();  // prevent form from submitting normally

        var password = document.getElementById('password').value;
        
        fetch('/ssh_open', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/home_jv';  // redirect to placeholder page
                } else {
                    alert('SSH connection failed.');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
});
