import telebot
import openai

openai.api_key = "api"
bot = telebot.TeleBot("api")

@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, text="Hello")

@bot.message_handler(content_types=['text'])
def message(message):

    prompt = message.text

    model = "text-davinci-003"
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

    generated_text = response.choices[0].text
    bot.send_message(message.chat.id,generated_text)

bot.infinity_polling()
