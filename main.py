import vocabulary

from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("TOKEN")
group_id = os.getenv("GROUP_ID")

import vk_api
from vk_api import bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token = access_token)
longpoll = VkBotLongPoll(vk, group_id)

def has_attachment(dictionary, attachment):
    return attachment in dictionary.attachments.keys()

def get_attachment(dictionary, attachment):
    return dictionary.attachments[attachment]

def send_attachment(chat_id, attachment):
    post = {
        "chat_id" : chat_id, 
        "attachment" : attachment, 
        "random_id" : 0
        }

    vk.method("messages.send", post)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            chat_id = event.chat_id
            command = event.object.message["text"].lower()

            if has_attachment(vocabulary, command):
                send_attachment(chat_id, get_attachment(vocabulary, command))