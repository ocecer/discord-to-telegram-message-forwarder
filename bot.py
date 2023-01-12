from check_message import *
from telebot import TeleBot
from discord.ext import commands
from discord import Intents, Client
import requests
from logging import basicConfig, WARNING

basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=WARNING)

print("Starting...")

try:
    botTG = TeleBot(TELEGRAM_BOT_TOKEN)
except Exception as e:
    print(f"ERROR - {e}")
    exit(1)

try:
    # intents = Intents.default()
    intents = Intents.all()
    botDS = commands.Bot(command_prefix='>', intents=intents)
except Exception as e:
    print(f"ERROR - {e}")
    exit(1)

baseUrl = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


@botDS.event
async def on_message(message):
    # try:
    #     serverName = message.guild.name
    # except Exception as e:
    #     print(e)

    try:
        channelName = message.channel.name
    except AttributeError:
        print(e + " Channel name can not get. Please try again.")

    userMessage = str(message.content)
    author = message.author.name

    print(author)

    if len(BLACKLIST_WORDS) > 0 or len(THROW_IF_MESSAGE_CONSIST_WORDS) > 0 or THROW_IF_MESSAGE_CONSIST_URL or THROW_IF_MESSAGE_CONSIST_MEDIA or DELETE_URL_FROM_MESSAGE:
        userMessage = checkMgs(userMessage)

    if userMessage != "THROW_THIS_MESSAGE" and (channelName in FROM):
        if len(message.mentions) > 0:
            # User Mentioned
            userMessage = replaceMentions(message.mentions, userMessage, channel=False)

        if len(message.channel_mentions) > 0:
            # Channel Mentioned
            userMessage = replaceMentions(message.channel_mentions, userMessage, channel=True)

        if len(message.attachments) > 0:
            for j in range(len(message.attachments)):
                attachmentUrl = message.attachments[j].url

                if isPhoto(attachmentUrl):
                    for i in TO:
                        url = f"{baseUrl}/sendPhoto?photo={attachmentUrl}&caption={reWriteCaption(userMessage, author)}&chat_id={i}"
                        sendMsg(url)

                elif isVideo(attachmentUrl):
                    for i in TO:
                        url = f"{baseUrl}/sendVideo?video={attachmentUrl}&caption={reWriteCaption(userMessage, author)}&chat_id={i}"
                        sendMsg(url)

                elif isDoc(attachmentUrl):
                    for i in TO:
                        url = f"{baseUrl}/sendDocument?document={attachmentUrl}&caption={reWriteCaption(userMessage, author)}&chat_id={i}"
                        sendMsg(url)

        elif len(message.embeds) > 0:
            embed = message.embeds[0].to_dict()

            if str(embed['type']) == "rich":
                if 'title' in embed.keys() and 'description' in embed.keys():
                    messageToSend = removeTags(reWriteEmbed(
                        title=embed['title'], description=embed['description'], author=author))
                elif 'title' in embed.keys():
                    messageToSend = removeTags(reWriteEmbed(
                        title=embed['title'], author=author))
                elif 'description' in embed.keys():
                    messageToSend = removeTags(reWriteEmbed(
                        description=embed['description'], author=author))

            elif str(embed['type']) == "link":
                messageToSend = removeTags(reWriteEmbed(
                    title=embed['title'], description=embed['description'], url=embed['url'], author=author))

            for i in TO:
                url = f"{baseUrl}/sendMessage?text={messageToSend}&chat_id={i}"
                sendMsg(url)

        elif len(userMessage) > 0:
            for i in TO:
                url = f"{baseUrl}/sendMessage?text={reWriteMessage(message=userMessage, author=author)}&chat_id={i}"
                sendMsg(url)

        else:
            botTG.send_message(chat_id=TO[i], text=reWriteMessage(
                message=userMessage, author=author))
    else:
        pass


def sendMsg(url):
    attempts = 0
    while True:
        if attempts < 5:
            try:
                print("Sending Message to Telegram...")
                resp = requests.post(url)
                if resp.status_code == 200:
                    print("Message sent.\n")
                    break
                elif resp.status_code != 200:
                    raise OSError
            except OSError:
                attempts += 1
                print(
                    f"Sending failed.\n[+] Trying again... (Attempt {attempts}/5)")
                continue
            except KeyboardInterrupt:
                print("\nPlease wait untill all messages in queue are sent.\n")
        else:
            print(
                "Message was not sent in 5 attempts. \nPlease check your network.")
            break


print("Bot has started.")

try:
    botDS.run(DISCORD_BOT_TOKEN)
except Exception as e:
    print(e)
botTG.infinity_polling()
