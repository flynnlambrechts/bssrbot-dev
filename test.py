import re

def get_custom_message(message):
	try:
		custom_message = re.search("'(.+?)'", message).group(1)
	except AttributeError:
		custom_message = "no message"
		print('no message found')
	return custom_message
message = "dookie: dinner 'hello'"
print(get_custom_message(message))