// app.js

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);

    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('output').innerText = data;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
