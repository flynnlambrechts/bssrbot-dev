#response
import os #make to import from a settings file
import requests
import json

class Response:
	def __init__(self,text=None,button=None,attachment=None):
		self.text = text
		self.attachment = attachment

		self.buttons = []
		self.quick_replies = []

	def addbutton(self,button):
		self.buttons.append(button)

	def addquickreply(self, quick_reply):
		self.quick_replies.append(quick_reply)


	def send(self, recipient_id):
		params = {
		   "access_token": os.environ["ACCESS_TOKEN"]
		}

		headers = {
			"Content-Type": "application/json"
		}

		if self.attachment:
			data = {
		    	"recipient": {"id": recipient_id},
		    	"message": {
		            "attachment": self.attachment
		            	}
			}
		else: #must be text
			if self.buttons:
				data = {
					"recipient": {"id": recipient_id},
					"message": {
						"attachment":{
							"type":"template",
							"payload":{
								"template_type":"button",
								"text": self.text,
								"buttons": self.buttons
							}
						}
					}
				}
			else: #No buttons
				data = {
					"recipient": {"id": recipient_id},
					"message": {
						"text": self.text}
				}

		if self.quickreplies:
			data["message"]["quick_replies"] = self.quickreplys #a list

		data = json.dumps(data)
		r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)



class Button:
	def __init__(self,title):
		self.title = title


class UrlButton(Button):
	def __init__(self,title,url):
		super().__init__(title)
		self.url = url
		self.button = {
			"type": "web_url",
			"url": self.url,
			"title": self.title
			}
		return self.button


	# def get_button(self):
	# 	button = {
 #                    "type": "web_url",
 #                    "url": self.url,
 #                    "title": self.title
 #                    }

	# 	return button


class QuickReply:
	def __init__(self,title,payload):
		self.title = title
		self.payload = payload
		#self.image = None

	def get_quickreply(self):
		quickreply = {
				"content_type":"text",
				"title":self.title,
				"payload":self.payload
				}
		return quickreply


class Gif:
	def __init__(self,text):
		self.gifurl = self.search_gif(text)

	def searh_gif(self,text):
		payload = {'s': text, 'api_key': 'ey1oVnN1NGrtEDHFGBJjRj5AgegLFVeT', 'weirdness': 1}
		r = requests.get('http://api.giphy.com/v1/gifs/translate', params=payload)
		r = r.json()
		# sprint(r)
		try:
			url = r['data']['images']['original']['url']
		except:
			print('failed to get gif')

		return url

	def get_gif(self):
		self.attachment = {
		"type": "image",
		"payload": {
			"url": self.gifurl}
		}
		return self.attachment





