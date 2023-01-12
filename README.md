1.	Rename .env.sample file as .env. Then open .env file and edit fields.
    a.  “TELEGRAM_BOT_TOKEN” - Bot can be created and bot token can be found in https://core.telegram.org/bots#6-botfather

    b.  “DISCORD_BOT_TOKEN” – Can be found in https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

    c.  “TO_CHANNEL” – Channel ID(s) of the channel(s) you will be forwarding messages to. If you will add more than 1 channel you should separate channel ID(s) with “;“. 

    d.  “BLACKLIST_WORDS” – Enter blacklisted word(s) split by ";" or just one blacklist word.  

    e.  “CHANGE_FOR” – There are 3 ways to use CHANGE_FOR
        i.   If CHANGE_FOR will be empty, bot will delete all the BLACKLIST_WORDS from the message and forward.
        ii.   If you will enter one variable for CHANGE_FOR, bot will change all the BLACKLIST_WORDS from the messages as CHANGE_FOR and forward.
        iii.   If you will enter CHANGE_FOR for each BLACKLIST_WORDS, bot will change all the BLACKLIST_WORDS respectively with the CHANGE_FOR from the message and forward. (If you will not enter CHANGE_FOR for each BLACKLIST_WORDS, bot will just delete the BLACKLIST_WORDS. 

    f. "THROW_IF_MESSAGE_CONSIST_WORDS" – Enter word(s) split by ";" or just one word. If message consists any of the words defined here, the message will not be forwarded.

    g. "FORWARD_IF_MESSAGE_CONSIST_WORDS" - Enter word(s) split by ";" or just one word. If message consists any of the words defined here, the message will be forwarded, otherwise it wont be forwarded.

    h. "THROW_IF_MESSAGE_CONSIST_URL" – Enter 1 or 0. If you enter 1, bot will not forward the message if it contains any URL.

    i. "THROW_IF_MESSAGE_CONSIST_MEDIA" – Enter 1 or 0. If you enter 1, bot will not forward the message if it contains any attachment.

    j. "DELETE_URL_FROM_MESSAGE" – Enter 1 or 0. If you enter 1, bot will forward the message but URL(s) will be deleted from the message.

    ATTENTION: If you will enter 1 for the THROW_IF_MESSAGE_CONSIST_URL, DELETE_URL_FROM_MESSAGE should be 0, reversible. But if you will enter 0 or 1 for both THROW_IF_MESSAGE_CONSIST_URL and DELETE_URL_FROM_MESSAGE, the bot will not proccess URL(s)'s in the message and directly forward the URL(s).

2.	Clone the repo in your Heroku, CPanel or any any other platform where you can run a python app.

3.  Install requirments with the command: pip install requiremnts -r requirements.txt

4.	Run: python3 bot.py

Note: Your bot in Discord should have access to read messages, your bot in Telegram should have a right to send messages in your Telegram channel