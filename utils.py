#import time

#collects what the entity is e.g. mealtype
# and its value e.g. breakfast, lunch or dinner
def whatmeal(message): #prev message_text
        #start = time.time()
        entity = None
        value = None

        if "dino" in message:
                value = "dino"
        elif "breakfast" in message or "breaky" in message or "brekky" in message:
                value = "breakfast"
        elif "lunch" in message:
                value = "lunch"
        elif "dinner" in message or "dins" in message or "supper" in message:
                value = "dinner"
        if value is not None:
                entity = 'mealtype:mealtype'
        #end = time.time()
        #print(end - start)
        return (entity, value)
