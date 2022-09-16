1.	Open .env file and edit fields.
    a.  “TELEGRAM_BOT_TOKEN” - Can be found in https://core.telegram.org/bots#6-botfather

    b.  “DISCORD_BOT_TOKEN” – Can be found in https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

    c.  “TO_CHANNEL” – Channel ID(s) of the channel(s) you will be forwarding messages to. If you will add more than 1 channel you should separate channel ID(s) with “;“. 

    d.  “BLACKLIST_WORDS” – Enter blacklisted word(s) split by ";" or just one blacklist word.  
    e.  “CHANGE_FOR” – There are 3 ways to use CHANGE_FOR
        i.   If CHANGE_FOR will be empty, bot will delete all the BLACKLIST_WORDS from the message and forward.
        ii.   If you will enter one variable for CHANGE_FOR, bot will change all the BLACKLIST_WORDS from the messages as CHANGE_FOR and forward.
        iii.   If you will enter CHANGE_FOR for each BLACKLIST_WORDS, bot will change all the BLACKLIST_WORDS respectively with the CHANGE_FOR from the message and forward. (If you will not enter CHANGE_FOR for each BLACKLIST_WORDS, bot will just delete the BLACKLIST_WORDS. 

2.	Clone the repo in your Heroku, CPanel or any any other platform where you can run a python app.
3.	Run: python3 main.py

Note: Your bot in Discord should have access to read messages, your bot in Telegram should have a right to send messages in your Telegram channel