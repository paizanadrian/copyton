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
        <link rel="stylesheet" type="text/css" href="css/styles.css">
        <script src="https://kit.fontawesome.com/dfa46fd6a4.js" crossorigin="anonymous"></script>
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
        <script src="js/buton.js"></script>
    </body>
    </html>
    """
    return html_content


# Interfața Streamlit
st.title("Generare HTML copy to clipboard din Excel")
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
