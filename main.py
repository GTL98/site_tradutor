# --- Importar as bibliotecas --- #
import pyperclip
import streamlit as st
from deep_translator import GoogleTranslator

# --- Configação da página --- #
st.set_page_config(page_title='Tradutor', layout='centered')

# --- Título na página --- #
st.title('Tradutor')

# --- Colocar o campo de texto --- #
texto = st.text_area('Texto para tradução', height=400)

# --- Tratar o texto --- #
texto = ' '.join(texto.split('\n'))

# --- Colocar o botão --- #
c_1, c_2, c_3, c_4, c_5 = st.columns(5)
with c_3:
    traduzir = st.button('Traduzir')
    if traduzir:
        # --- Traduzir o texto --- #
        traducao = GoogleTranslator(source='en', target='pt').translate(text=texto)

        # --- Copiar o texto --- #
        pyperclip.copy(traducao)
