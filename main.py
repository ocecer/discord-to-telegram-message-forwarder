from telebot import TeleBot
from discord.ext import commands
from discord import Intents
from decouple import config

# Basics
TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
DISCORD_BOT_TOKEN = config("DISCORD_BOT_TOKEN")
TO_CHANNEL_ = config("TO_CHANNEL")
BLACKLIST_WORDS_ = config("BLACKLIST_WORDS")
CHANGE_FOR_ = config("CHANGE_FOR")

botTG = TeleBot(TELEGRAM_BOT_TOKEN)
# TO_CHANNEL = TO_CHANNEL_
TO_CHANNEL = [int(i) for i in TO_CHANNEL_.split(";")]
if len(BLACKLIST_WORDS_) == 0:
    BLACKLIST_WORDS = []
else:
    BLACKLIST_WORDS = [str(i) for i in BLACKLIST_WORDS_.split(";")]
if len(CHANGE_FOR_) == 0:
    CHANGE_FOR = []
else:
    CHANGE_FOR = [str(i) for i in CHANGE_FOR_.split(";")]

# intents = Intents.default()
intents = Intents.all()
botDS = commands.Bot(command_prefix='>', intents=intents)


@botDS.event
async def on_message(message):
    author = message.author.name

    if len(BLACKLIST_WORDS) > 0:
        userMessage = str(message.content)
        userMessage = checkMgs(BLACKLIST_WORDS, CHANGE_FOR, userMessage)
        message.content = userMessage

    try:
        repos = message.content + ' ' + message.attachments[0].url
    except:
        repos = message.content
    for i in TO_CHANNEL:
        botTG.send_message(str(i), repos)
        # sleep(.5)
    # await print(message.author.name + ' ' + message.content)


def checkMgs(blacklist, changeFor, userMessage):
    if len(changeFor) == 0:
        for word in blacklist:
            if word in userMessage:
                userMessage = userMessage.replace(word, "")
    elif len(blacklist) > 1 and len(changeFor) == 1:
        for word in blacklist:
            if word in userMessage:
                userMessage = userMessage.replace(word, changeFor[0])
    else:
        for i in range(len(blacklist)):
            word = blacklist[i]
            if word in userMessage:
                userMessage = userMessage.replace(word, changeFor[i])

    return userMessage


botDS.run(DISCORD_BOT_TOKEN)
botTG.infinity_polling()
