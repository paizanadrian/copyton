for (let i = 1; i <= 1000; i++) {
    let copyButton = document.getElementById('copy-button-' + i);
    let myInput = document.getElementById('myInput-' + i);
    let textDisplay = document.getElementById('text-display-' + i);

    copyButton.addEventListener('click', async function() {
        let originalText = textDisplay.innerText;
        myInput.value = originalText;
        myInput.style.display = 'block';
        myInput.select();

        try {
            await navigator.clipboard.writeText(originalText);

            // Schimbă textul, adaugă stilul de text bold și culoarea de fundal
            textDisplay.innerText = 'COPIAT!';
            textDisplay.className = "copied-text";

            // Schimbă iconița butonului și aplică noua clasă
            copyButton.className = "fa-solid fa-check check-button";

            // Revenire la textul original după 1 secundă și eliminarea stilului
            setTimeout(function() {
                textDisplay.innerText = originalText;
                textDisplay.className = "";
            }, 1000); // 1000 de milisecunde = 1 secundă

            // Revenire la iconița originală după 1 secundă
            setTimeout(function() {
                copyButton.className = "fa-regular fa-copy copy-button";
            }, 1000); // 1000 de milisecunde = 1 secundă
        } catch (err) {
            console.error('Eroare la copierea textului: ', err);
        } finally {
            myInput.style.display = 'none';
        }
    });
}
