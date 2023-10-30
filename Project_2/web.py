import streamlit as st 
from SpeechTranslation import translate
from speech import Transcribe

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

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
    if st.button('Translate'):
        translation = translate(dict_lang[language], title)
        st.write(f'Your translation from English to {language} is: ', translation)

elif option== 'An audio file':
    uploaded_file = st.file_uploader("Upload an english audio file")
    if uploaded_file is not None:
        # To read file as bytes:
        audio_file = uploaded_file.getvalue()
        if st.button('Translate'):
            transcription = Transcribe(audio_file)
            speech_translation = translate(dict_lang[language], transcription)
            st.write(f'Your translation from English to {language} is: ', speech_translation)

else:
    st.write("Nothing was selected")

