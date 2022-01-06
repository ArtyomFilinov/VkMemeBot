from typing import ForwardRef
import vocabulary as voc

import vk_api
from vk_api import bot_longpoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token = "TOP SECRET")
longpool = VkBotLongPoll(vk, 203612865)

def has_photo(d, photo):
    return photo in d.photos.keys()

def get_photo(d, photo):
    return d.photos[photo]

def send_photo(id, photo) :
    post = {
        "chat_id" : id, 
        "attachment" : photo, 
        "random_id" : 0
        }

    vk.method("messages.send", post)

for event in longpool.listen(): 
    print(event.type)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            name = event.object.message["text"]

            if (has_photo(voc, name)): send_photo(id, get_photo(voc, name))