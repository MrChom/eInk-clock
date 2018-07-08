from datetime import datetime
import json
import random
with open('quotes.json') as f:
    quotes = json.load(f)
timeprinted = None
donestuff = None
quoteamount = len(quotes["quotations"])
try:
    while True:
        seconds = datetime.now()
        if (timeprinted != seconds.second % 15):
            print(datetime.now())

            timeprinted=seconds.second % 15
        if (seconds.second % 15 == 7 and donestuff != seconds.second):
            quotenumber = random.randint(0,quoteamount-1)
            print ( quotes["quotations"][quotenumber]["line"] + "\n -" + quotes["quotations"][quotenumber]["who"] )
            donestuff = seconds.second            
except KeyboardInterrupt:
    print("Exiting...")
    pass