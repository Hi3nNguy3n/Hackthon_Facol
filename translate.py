from deep_translator import GoogleTranslator

def vi_en(user_input):

    en = GoogleTranslator(source='auto', target='en').translate(user_input)
    return en

def en_vi(user_input):

    vi = GoogleTranslator(source='auto', target='vi').translate(user_input)
    return vi

