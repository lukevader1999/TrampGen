document.getElementById('generiereListeBtn').addEventListener('click', () => {
    fetch('/generate_kuer')
        .then(response => response.json())
        .then(data => {
            const listeHtml = data.liste.map(item => `<li>${item}</li>`).join('');
            document.getElementById('liste').innerHTML = `<ul>${listeHtml}</ul>`;
        })
        .catch(error => console.error('Fehler:', error));
});