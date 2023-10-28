import streamlit as st 
import pandas as pd
from io import StringIO
from SpeechTranslation import translate


option = st.selectbox(
    'What would you like to translate?',
    ('A text', 'An audio file'))

language = st.selectbox(
    'What language do you want to translate to?',
    ('Yoruba', 'Igbo', 'Hausa'))

dict_lang = {"Yoruba": "yo",
               "Igbo": "ig",
               "Hausa": "ha"}

if option=='A text':
    title = st.text_input('English Text', 'Enter your english text here?')
    translation = translate(dict_lang[language], title)
    st.write('Your translation from English to {language} is: ', translation)

elif option== 'An audio file':
    uploaded_file = st.file_uploader("Upload an audio file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        if st.button('Translate'):
            speech_translation = translate(dict_lang[language], bytes_data)
            st.write('Your translation from English to {language} is: ', speech_translation)

else:
    st.write("Nothing was selected")
