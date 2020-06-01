from gtts import gTTS
import telebot
from telebot import types
from filestack import Client
import random

client = Client("A0LbJ1YlXQFWtoK4G9QBjz")
path = "C:\\Users\\WINDOWS 10\\PycharmProjects\\memebot\\images\\1.mp3"
token = "1157303469:AAG9iUMm_meciVW8Vwiqb1ZdAgepWOyQowQ"
bot = telebot.TeleBot(token)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        query.query = query.query.replace("\n", " ")
        audiotext = query.query
        tts = gTTS(audiotext, lang="ru")
        tts.save(path)
        filelink = client.upload(filepath=path)
        print(filelink.url)
        ans = types.InlineQueryResultVoice(
            id=str(random.randint(1, 64 * 8)), voice_url=filelink.url, title="nothing"
        )
        bot.answer_inline_query(query.id, [ans], cache_time=5)
    except Exception as e:
        print(e)


bot.polling()
