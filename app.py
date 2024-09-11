import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

# Function to get language code from language name
def get_language_code(language_name):
    for lang_name, lang_code in GOOGLE_LANGUAGES_TO_CODES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Custom CSS for styling the app
st.markdown("""
    <style>
    body {
        background-color: #f0f0f5;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 16px !important;
    }
    h1, h2, h3, p {
        text-align: center;
        color: #4B0082;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
        border: none;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("🌐 Language Translator using Seq2Seq Model")
st.write("Translate text between languages using a dynamic, user-friendly interface.")

# Input text
source_text = st.text_area("📝 Enter the text you want to translate:", "")

# Input source language (fixed selection)
source_lang = st.selectbox("Select source language", list(GOOGLE_LANGUAGES_TO_CODES.keys()))

# Target language input (searchable by name)
target_language_search = st.text_input("🔍 Enter target language name (e.g., French, Spanish, German):")

# Translate button
if st.button("🌍 Translate"):
    target_lang_code = get_language_code(target_language_search)

    if target_lang_code is None:
        st.write(f"⚠ Error: '{target_language_search}' is not a valid language name. Please try again.")
    else:
        # Using deep-translator for translation
        translator = GoogleTranslator(source=source_lang, target=target_lang_code)
        translated_text = translator.translate(source_text)
        st.success(f"Translated Text: {translated_text}")

# Show supported languages with better design
if st.checkbox("Show supported languages"):
    st.write("Supported Languages:")
    st.write(", ".join([lang_name.capitalize() for lang_name in GOOGLE_LANGUAGES_TO_CODES.keys()]))

# Footer styling
st.markdown("""
    <div style="text-align: center; padding-top: 20px; font-size: 14px; color: #808080;">
        Created by <a href="https://github.com/DeninjoseE" target="_blank">DENIN JOSE</a> | Powered by Streamlit & Google Translate API
    </div>
    """, unsafe_allow_html=True)