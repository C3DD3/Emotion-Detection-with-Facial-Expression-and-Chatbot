import google.generativeai as genai
import json
from app import intro  

API_KEY = ''
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def get_gemini_response(userInput):
    instruction = intro()  # intro fonksiyonunu çağırarak instruction'ı güncelliyorum
    response = chat.send_message(userInput + instruction)
    result = response.text
    return result
