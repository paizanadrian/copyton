        for (let i = 1; i <= 100; i++) {
            let copyButton = document.getElementById('copy-button-' + i);
            let myInput = document.getElementById('myInput-' + i);
            let textDisplay = document.getElementById('text-display-' + i);

            copyButton.addEventListener('click', function() {
                let originalText = textDisplay.innerText;
                myInput.value = originalText;
                myInput.style.display = 'block';
                myInput.select();
                document.execCommand('copy');
                myInput.style.display = 'none';

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
            });
        }
  