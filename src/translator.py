
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')

def get_translation(content: str) -> str:
    response = model.generate_content("translate " + content + " to English")
    print(response.text)
    return response.text

def get_language(content: str) -> str:

    response = model.generate_content("Please identify the language of the following sentence: " + content )
    print(response.text)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
  # empty content
  if len(content) == 0: 
     return False, ""

  # longer than one word
  if len((get_language(content)).split(" ")) != 1: 
     return False, content
  
  #language is one word
  is_english = get_language(content) == "English"
  #if English, return default content
  if is_english: 
     return True, content
  else:
    #not english, get translation
    translation = get_translation(content)
    print(translation)
    if get_language(translation) != "English":
        print(get_language(translation))
        translation = content #invalid input is returned to user

    return is_english, translation

# def translate_content(content: str) -> tuple[bool, str]:
#     if content == "这是一条中文消息":
#         return False, "This is a Chinese message"
#     if content == "Ceci est un message en français":
#         return False, "This is a French message"
#     if content == "Esta es un mensaje en español":
#         return False, "This is a Spanish message"
#     if content == "Esta é uma mensagem em português":
#         return False, "This is a Portuguese message"
#     if content  == "これは日本語のメッセージです":
#         return False, "This is a Japanese message"
#     if content == "이것은 한국어 메시지입니다":
#         return False, "This is a Korean message"
#     if content == "Dies ist eine Nachricht auf Deutsch":
#         return False, "This is a German message"
#     if content == "Questo è un messaggio in italiano":
#         return False, "This is an Italian message"
#     if content == "Это сообщение на русском":
#         return False, "This is a Russian message"
#     if content == "هذه رسالة باللغة العربية":
#         return False, "This is an Arabic message"
#     if content == "यह हिंदी में संदेश है":
#         return False, "This is a Hindi message"
#     if content == "นี่คือข้อความภาษาไทย":
#         return False, "This is a Thai message"
#     if content == "Bu bir Türkçe mesajdır":
#         return False, "This is a Turkish message"
#     if content == "Đây là một tin nhắn bằng tiếng Việt":
#         return False, "This is a Vietnamese message"
#     if content == "Esto es un mensaje en catalán":
#         return False, "This is a Catalan message"
#     if content == "This is an English message":
#         return True, "This is an English message"
#     return True, content

# print(translate_content("This is an English message"))