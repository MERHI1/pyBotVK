import vk_api, random
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import datetime

from data_vk_bot import token

vk_session = vk_api.VkApi(token=token)
vk_session._auth_token()

photos = [""]

while True:
    messages = vk_session.method("messages.getConversations", {"offset":0, "count":20, "filter":"unanswered"})

    if messages["count"] >= 1:
        text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']

        if text.lower() == 'привет':
            vk_session.method("messages.send", {"user_id": user_id, "message": "Hello", "random_id": random.randint(1, 1000)})
        elif text.lower() == 'фото':
            uploader = vk_api.upload.VkUpload(vk_session)
            img = uploader.photo_messages()
            media_id = str(img[0]['id'])
            owner_id = str(img[0]['owner_id'])
            print("photo" + owner_id + "_" + media_id)
            vk_session.method("messages.send", {"user_id": user_id, "attachment":"photo" + owner_id + "_" + media_id, "message": "OK", "random_id": random.randint(1, 1000)})
        else:
            vk_session.method("messages.send", {"user_id":user_id, "message":"Ne ponimat", "random_id":random.randint(1, 1000)})