import json

data = {
	        		"recipient": {"id": "here recipient_id"},
	        		"message": {
	                    "attachment":{
	                        "type":"template",
	                        "payload":{
	                            "template_type":"button",
	                            "text": "text here",
	                            "buttons": "button here"
                        	}
                    	}
                	}
                }

#print(data)

data["message"]["quick_replies"] = "quick reply here"

data = json.dumps(data)
print(data)
