from gtts import gTTS
import telebot
from telebot import types
from filestack import Client
import random

# Your fire-stack api
client = Client("api")
# Directory to save files, can look like :
path = "C:\\PycharmProjects\\bot\\audios\\1.mp3"
# Your Telegram Bot token
token = "token"
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
