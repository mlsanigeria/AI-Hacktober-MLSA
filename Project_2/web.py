import streamlit as st
st.set_page_config(page_title="Naija Speech Translation App", page_icon="🔊")

from SpeechTranslation import translate
# from speech import Transcribe
from speech_rest import Transcribe

from moviepy.editor import *
from tempfile import NamedTemporaryFile

# st.header("Speech Translation")
st.markdown("# 🔊 Speech Translation")
st.markdown("### (From English to Yoruba, Igbo or Hausa)")

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
    title = st.text_area('English Text', 'Enter your english text here?')
    if st.button('Translate'):
        with st.spinner(f"Translating text..."):
            translation = translate(dict_lang[language], title)

        st.write(f'Your translation from English to {language} is: ')
        # st.markdown(f"#### {translation}")
        # st.code(f"{translation}", language="markdown")
        # st.text(translation)
        title = st.text_area(label='Output', value=translation, height=200, label_visibility='hidden')

elif option== 'An audio file':
    uploaded_file = st.file_uploader("Upload an english audio file",
                            type=['mp3', 'wav', 'aac', 'ogg', 'wma', 'aiff', 'opus', 'm4a', 'amr'])
    if uploaded_file is not None:
        # To read file as bytes:
        audio_file = uploaded_file.getvalue()
        if st.button('Translate'):
            audio_params = {
                "codec": "pcm_s16le",
                "fps": 16000,  # Set the desired sampling rate: 16000 Hz
                # "fps": 8000,  # Alternatively, set the sampling rate to 8000 Hz
                "nchannels": 1,  # Mono audio
                "bitrate": "16k"  # Set the desired bitrate
            }

            with st.spinner(f"Translating audio..."):
                with NamedTemporaryFile(suffix="wav") as temp:

                    temp.write(audio_file)
                    audioclip = AudioFileClip(temp.name)
                    audioclip.write_audiofile("audio.wav", codec=audio_params["codec"], fps=audio_params["fps"],
                                                nbytes=2,bitrate=audio_params["bitrate"])
                    
                    transcription = Transcribe("audio.wav")
                    speech_translation = translate(dict_lang[language], transcription)

            st.write(f'Your translation from English to {language} is: ')
            # st.markdown(f"#### {translation}")
            # st.code(f"{translation}", language="markdown")
            # st.text(translation)
            title = st.text_area(label='Output', value=speech_translation, height=200, label_visibility='hidden')

else:
    st.write("Nothing was selected")

st.divider()
st.markdown("##### Built by contributors to the [AI-Hacktober-MLSA](https://github.com/mlsanigeria/AI-Hacktober-MLSA) repository as part of an ML/AI Hacktoberfest Challenge.")
st.write("Copyright © Microsoft Learn Student Ambassadors, Nigeria 2023")
