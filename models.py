#first attempts using classes
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

class Sender:
	def __init__(self, recipient_id):
		URL = "".join("https://graph.facebook.com/v2.6/", recipient_id, "?fields=first_name,last_name&access_token=", ACCESS_TOKEN)
		r = requests.get(url = URL)
		data = r.json()
		self.first_name = data['first_name']
		self.last_name = data['last_name']
		self.psid = recipient_id
		self.full_name  = " ".join(data['first_name'],data['last_name'])

	def get_firstname():
		return self.first_name

	def get_lastname():
		return self.lastname

	def get_fullname():
		return self.full_name

# user = Sender(recipient_id)
# print(user.get_fullname())