const contactForm = document.querySelector('#contact_form');
contactForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(contactForm)

    fetch('http://127.0.0.1:5000/api/booking', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => {
            console.error('ERROR', error);
            alert('錯誤');
        });
});