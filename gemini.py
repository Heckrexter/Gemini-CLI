import google.generativeai as genai
from key import GOOGLE_API_KEY

# text formatting
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Hello there!")
print(response.text)
print("(PS if you wish to exit at any time please type 'exit')")
while True:
    prompt = input(red+underline+bold+"\n\nUser"+end+red+bold+":-\n"+end)
    if prompt == "exit":
        break
    response = model.generate_content(prompt)
    print(blue+underline+bold+"\n\nGemini"+end+blue+bold+":-\n"+response.text+end)