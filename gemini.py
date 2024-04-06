import google.generativeai as genai
import historydb
from key import GOOGLE_API_KEY

# text formatting
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

historydb.initdb()

genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

messages = historydb.get_messages()

print("Welcome to Gemini-CLI! Type 'exit' to exit.\nType \"flush\" to clear the chat history.")
while True:
    prompt = input(red+underline+bold+"\n\nUser"+end+red+bold+":-\n"+end)
    if prompt.lower() == "exit":
        break
    if prompt.lower() == "flush":
        historydb.clear_messages()
        print(green+"Chat history cleared."+end)
        messages = []
        continue
    messages.append({
        'role': 'user',
        'parts': [prompt]
    })
    historydb.add_message('user', prompt)
    response = model.generate_content(messages)
    output = response.candidates[0].content
    historydb.add_message(output.role, output.parts[0].text)
    messages.append(output)
    print(blue+underline+bold+"\n\nGemini"+end+blue+bold+":-\n"+response.text+end)