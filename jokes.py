#jokes
import pyjokes

def getjoke():
    the_joke = pyjokes.get_joke(language="en",category="neutral")
    print(the_joke)

getjoke()
