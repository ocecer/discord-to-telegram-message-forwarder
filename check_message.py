from blacklist_check import *
from urlextract import URLExtract
from re import sub
from requests import utils


def checkMgs(message):
    userMessage = str(message.content)

    if THROW_IF_MESSAGE_CONSIST_URL:
        urlExtract = URLExtract()
        urls = urlExtract.find_urls(userMessage)

        if len(urls) > 0:
            userMessage = "THROW_THIS_MESSAGE"
            return userMessage

    if THROW_IF_MESSAGE_CONSIST_MEDIA:
        if len(message.attachments) > 0:
            userMessage = "THROW_THIS_MESSAGE"
            return userMessage

    if len(THROW_IF_MESSAGE_CONSIST_WORDS) > 0:
        for word in THROW_IF_MESSAGE_CONSIST_WORDS:
            if word in userMessage:
                userMessage = "THROW_THIS_MESSAGE"
                return userMessage

    if DELETE_URL_FROM_MESSAGE:
        urlExtract = URLExtract()
        urls = urlExtract.find_urls(userMessage)

        if len(urls) > 0:
            for url in urls:
                if url in userMessage:
                    userMessage = userMessage.replace(url, "")

    if len(FORWARD_IF_MESSAGE_CONSIST_WORDS) > 0:
        found = False
        for word in FORWARD_IF_MESSAGE_CONSIST_WORDS:
            if word in userMessage:
                found = True
                userMessage = blacklistCheck(userMessage)
                break
            else:
                continue

        if not found:
            userMessage = "THROW_THIS_MESSAGE"

    else:
        userMessage = blacklistCheck(userMessage)

    return userMessage


def replaceMentions(mentions, msg, channel):
    if channel:
        for ch in mentions:
            msg = sub(f"<#{ch.id}>", f"#{ch.name}", msg)
            msg = sub(f"<{ch.id}>", f"#{ch.name}", msg)
            msg = sub(f"<*{ch.id}>", f"#{ch.name}", msg)
            msg = sub(f"<*{ch.id}*>", f"#{ch.name}", msg)
            msg = sub(f"<{ch.id}*>", f"#{ch.name}", msg)
    elif not channel:
        for member in mentions:
            msg = sub(f"<@{member.id}>", f"@{member.name}", msg)
            msg = sub(f"<@!{member.id}>", f"@!{member.name} ", msg)
            msg = sub(f"<@&{member.id}>", f"@&{member.name} ", msg)
            msg = sub(f"<*{member.id}>", f"*{member.name} ", msg)
            msg = sub(f"<{member.id}>", f"{member.name} ", msg)
    return str(msg)


def removeTags(msg):
    msg = sub(r"@\w*", '', msg)
    msg = utils.quote(msg)
    return msg


def isPhoto(url):
    imgExts = ["png", "jpg", "jpeg", "webp"]
    if any(ext in url for ext in imgExts):
        return True
    else:
        return False


def isVideo(url):
    vidExts = ["mp4", "MP4", "mkv"]
    if any(ext in url for ext in vidExts):
        return True
    else:
        return False


def isDoc(url):
    docExts = ["zip", "pdf", "gif"]
    if any(ext in url for ext in docExts):
        return True
    else:
        return False


nameSeperator = ":\n"


def reWriteCaption(caption, author):
    if len(caption) + len(author) + len(nameSeperator) > 1024:
        caption = caption[0:len(caption)-(len(caption)-1024) +
                          len(author)+len(nameSeperator)+3] + "..."
    else:
        caption = caption

    return author + nameSeperator + caption


def reWriteMessage(message, author):
    if len(message) + len(author) + len(nameSeperator) > 4096:
        message = message[0:len(message)-(len(message)-4096) +
                          len(author)+len(nameSeperator)+3] + "..."
    else:
        message = message

    return author + nameSeperator + message


def reWriteEmbed(title, description, url, author):
    if len(title) + len(description) + len(url) + len(author) + len(nameSeperator) + len("\n")*2 > 4096:
        description = description[0:len(description)-(len(description)-4096)+len(
            title)+len(url)+len(author)+len(nameSeperator)+len("\n")*2+3] + "..."
    else:
        description = description

    return author + nameSeperator + title + "\n" + description + "\n" + url
