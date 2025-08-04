from deep_translator import GoogleTranslator


def language_translate(text:str,target_language:str='hi',source_language:str='en')->str:

    translated = GoogleTranslator(source=source_language, target=target_language).translate(text)

    return translated

if __name__=='__main__':
    text='I Love India'

    transcript=language_translate(text)
    print(type([transcript]))


