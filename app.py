import streamlit as st
import pandas as pd


# Funcția pentru a genera codul HTML
def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="ro-RO">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Copiaza in Clipboard</title>

    <!-- Texte pe acelasi rand -->
        <!-- Include fisierul CSS -->
        <script src="https://kit.fontawesome.com/dfa46fd6a4.js" crossorigin="anonymous"></script>
    <style>
        .copy-button {
            font-size: 24px;
            cursor: pointer;
            color: #3272e2;  /* Adaugă aici culoarea pe care o dorești */
            margin-left: 5px;  /* Adaugă o margine la stânga butonului */
        }
        .check-button {
            font-size: 24px;
            cursor: pointer;
            color: green;  /* Adaugă aici culoarea pe care o dorești */
            margin-left: 5px;  /* Adaugă o margine la stânga butonului */
        }
        .container {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-left: 20px;
            margin-bottom: 10px;
            margin-top: 10px;
            margin-right: 20px;
        }
        .text-button-group {  /* Grup pentru text și buton */
            display: flex;
            align-items: center;
        }
        .text-placeholder {         /* Pentru butoane fixate in dreapta */
            width: 500px;
            overflow: hidden;
        }
        .copied-text {
            font-weight: bold;
            background-color: #61f635;  /* Culoarea de fundal a textului "COPIAT!" */
        }
        .bold-text {
            font-weight: bold;  /* Setează textul ca bold */
            margin-right: 5px;  /* Adaugă o margine la dreapta */
        }
        .titlu {
            margin-left: 20px;
            margin-bottom: 20px;
        }
        </style>
            </head>
            <body>
        
                <!-- Titlul paginii ... -->
                <div class="titlu">
                    <h1>Copy to Clipboard</h1>
                </div>	
    """
    # Adăugarea fiecărui rând din dataframe în HTML
    for index, row in data.iterrows():
        html_content += f"""
        <div class="container">
            <span class="bold-text">{row['text']}: </span><span id="text-display-{index + 1}">{row['link']}</span>
            <i id="copy-button-{index + 1}" class="fa-regular fa-copy copy-button"></i>
        </div>
        <input type="text" value="Textul initial" id="myInput-{index + 1}" style="display: none;">
        """

    html_content += """
        <script>
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

        
        </script>
        </body>
        </html>
    """
    return html_content


# Setari Streamlit
st.set_page_config(
    page_title="Copy to clipboard",
    page_icon=":tada:",  # Poți folosi un emoji sau calea către un fișier imagine
    layout="wide",  # Aceasta setează modul wide
    # initial_sidebar_state="auto"  # Poți seta și starea inițială a barei laterale: "auto", "expanded", "collapsed"
)
# Interfața Streamlit
st.title("Generare HTML copy to clipboard din Excel (max. 1000 de rânduri)")
st.subheader("Fișierul Excel trebuie să conțină coloanele 'text' și 'link'.")

# Încărcarea fișierului Excel
uploaded_file = st.file_uploader("Alege un fișier Excel", type=["xlsx"])

if uploaded_file:
    # Citirea datelor din Excel
    df = pd.read_excel(uploaded_file)

    # Afișarea numelor coloanelor pentru verificare
    st.write("Numele coloanelor citite din fișierul Excel:", df.columns.tolist())

    # Asigură-te că numele coloanelor sunt corecte
    if 'text' in df.columns and 'link' in df.columns:
        # Generarea codului HTML
        html_result = generate_html(df)

        # Afișarea rezultatului
        st.markdown("### Codul HTML generat:")
        st.code(html_result, language='html')

        # Salvarea fișierului HTML
        st.download_button(
            label="Descarcă HTML",
            data=html_result,
            file_name='output.html',
            mime='text/html'
        )
    else:
        st.error("Fișierul Excel trebuie să conțină coloanele 'text' și 'link'.")
