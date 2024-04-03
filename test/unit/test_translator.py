from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    print(translated_content)
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("The weather is good today") 
    assert is_english == True 
    assert translated_content == "The weather is good today"
                                            

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("248629efjh(^$#*@)")
    assert is_english == False
    assert translated_content == "248629efjh(^$#*@)"