import gradio as gr
from extract_youtube_link import extract_youtube_IDs
from extract_trascript import extract_transcript
import pandas as pd
from typing import List
from languages import LANGUAGES
from language_translator import language_translate

text=gr.Textbox(value='Enter the topic',
           lines=2,
           placeholder='tutorials on Python')
def interface_fn(topic:str,source_lang:str,target_lang:str) ->str:
    try:
        language_code = LANGUAGES[source_lang]
        transcript=extract_transcript(topic, [language_code])
        translate=language_translate(text=transcript[0],target_language=target_lang)
        if not transcript:
            return "No YouTube links found for this topic."
        
        return translate
    except Exception as e:
        return f'Error: {str(e)}'


source_lang_dropdown = gr.Dropdown(
    choices=list(LANGUAGES.keys()),
    value="English",
    label="Select Transcript Language"
)

from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='en')

# Get the supported language mapping
language_dict = translator.get_supported_languages(as_dict=True)

target_language_dropdown=gr.Dropdown(choices=list(language_dict.keys()),
                            value="English",
                            label="Select target Language")

text_input = gr.Textbox(label="Enter a Topic", lines=2, placeholder="e.g. LangChain Tutorial")

demo=gr.Interface(
    fn=interface_fn,
    inputs=[text_input,source_lang_dropdown,target_language_dropdown],
    outputs=gr.Textbox(
        lines=15,
        placeholder=True
        
    )
)

demo.launch(share=True)
