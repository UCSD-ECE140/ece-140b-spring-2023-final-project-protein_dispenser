const form = document.querySelector('form');

const supplementButtons = document.querySelectorAll('.toggle-btn');

supplementButtons.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('selected');
    });
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const selectedServingSize = document.querySelector('#serving').value;

    try {
        const response = await fetch('/api/set-serving', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ServingSize: selectedServingSize })
        });

        if (!response.ok) {
            throw new Error('Failed to set serving size');
        }

        alert(`Serving size set to ${selectedServingSize} g`);
    } catch (error) {
        alert(error.message);
    }
});
