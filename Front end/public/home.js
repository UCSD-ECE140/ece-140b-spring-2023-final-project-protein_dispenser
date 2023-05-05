const form = document.querySelector('form');

const supplementButtons = document.querySelectorAll('.toggle-btn');

supplementButtons.forEach(button => {
    button.addEventListener('click', () => {
        button.classList.toggle('selected');
    });
});

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const selectedProteinAmount = document.querySelector('#protein-amount').value;

    try {
        const response = await fetch('/api/set-protein-amount', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ proteinAmount: selectedProteinAmount })
        });

        if (!response.ok) {
            throw new Error('Failed to set protein amount');
        }

        alert(`Protein amount set to ${selectedProteinAmount} g`);
    } catch (error) {
        alert(error.message);
    }
});
