import os
from flask import Flask, request
from fbmessenger import BaseMessenger
from fbmessenger import quick_replies
from fbmessenger.elements import Text
from fbmessenger.thread_settings import GreetingText, GetStartedButton, MessengerProfile, PersistentMenu, PersistentMenuItem


greeting_text = GreetingText('Welcome to BssrBot')
get_started = GetStartedButton(payload='start')

menu_item_1 = PersistentMenuItem(item_type='postback', title='Weather Status', payload='start')
menu = PersistentMenu(menu_items=[menu_item_1])

messenger_profile = MessengerProfile(persistent_menus=[menu], get_started=get_started, greetings=[greeting_text])
messenger.set_messenger_profile(messenger_profile.to_dict())

def postback(self, message):
        payload = message['postback']['payload']

        if 'start' in payload:
            quick_reply_1 = quick_replies.QuickReply(title='Location', content_type='location')
            quick_replies_set = quick_replies.QuickReplies(quick_replies=[
                quick_reply_1
            ])
            text = {'text': 'Share your location'}
            text['quick_replies'] = quick_replies_set.to_dict()
            self.send(text)