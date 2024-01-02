import telepot
from telepot.loop import MessageLoop
import google.generativeai as genai
genai.configure(api_key="APIKEY")
model = genai.GenerativeModel('gemini-pro')

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    response = model.generate_content(text)
    telepot.bot.sendMessage(chat_id, response.text)

telepot.bot = telepot.Bot('TOKEN')
MessageLoop(telepot.bot, handle).run_forever()
print('Listening ...')
