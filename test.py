import json
from response import QuickReply

quick_replies = []
quickreply1 = QuickReply("Breakfast", "Breakfast").get_quickreply()
quickreply2 = QuickReply("Lunch", "Lunch").get_quickreply()
quickreply3 = QuickReply("Dinner", "Dinner").get_quickreply()

quick_replies.append(quickreply1)
quick_replies.append(quickreply2)
quick_replies.append(quickreply3)

print(quick_replies)