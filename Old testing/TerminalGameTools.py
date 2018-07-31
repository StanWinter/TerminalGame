import sys
import time
import random

def slowprint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    print('')

def FakeLoading(text, text2 = ""):
    sys.stdout.write(text)
    amount = random.randint(5,12)
    for x in range(amount):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05, 0.15))
        
    print('')
    print(text2)
    print('')
