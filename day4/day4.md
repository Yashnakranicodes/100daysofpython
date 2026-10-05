# 🖼️ Day 4

In day 4 I am making a programme that gets the *jokes* form a json format web, may be around 50 jokes.
we can hear random jokes and can save it to a json file and can get the saved jokes.

---

## Used library & built in python functions

used lib's :
* requests
* json
* random
* time

random and time are for just one function to make it more fun.

**code**

```py
import requests
import json
import time
import random

#request for getting website data
response = requests.get("https://official-joke-api.appspot.com/jokes/random/50")
jcon = response.json()



list_of_id = []

def load():
    while True:
        jokedict = random.choice(jcon)
        if jokedict["id"] not in list_of_id :
            list_of_id.append(jokedict["id"])
            return jokedict
while True :
    print(
        "---------joke stimulator---------\n" \
        "1. want to hear joke\n" \
        "2. want to save previous joke\n" \
        "3. load the saved jokes\n" \
        "4. exit the program\n"
    )
    try:
        inp = int(input("your choice : "))
    except :
        print("pls write the write number")
    if inp ==1 :
        joked = load()
        print(joked['setup'])
        time.sleep(random.randint(2,4))
        print(f"{joked["punchline"]}\n")

    elif inp == 2 :# to save the previous joke
        joke_id = list_of_id[-1]
        joke_m = {}
        for every in jcon:
            if every['id'] == joke_id:
                joke_m = every
            else :
                continue
        try :
            with open("jokes.json" , "r") as jks :
                new_d = json.load(jks)
        except FileNotFoundError:
            new_d = []
        if joke_m in new_d :
            print("The joke is already saved!")
        else:
            new_d.append(joke_m)
            with open("jokes.json", "w") as jks2 :
                json.dump(new_d , jks2, indent=1)
            print("jokes saved\n")

    elif inp == 3:
        with open("jokes.json") as jk:
            jok = json.load(jk)
            if len(jok) != 0:
                for each in jok :
                    if each['id'] != 0:
                        print(
                            f"setup : {each['setup']}\n"
                            f"punchline : {each['punchline']}\n", end="\n"
                        )
                    else:
                        pass
            else:
                print("NO jokes saved")
    elif inp == 4 :
        print("Thankyou")
        break
```

### That's it for now 
I am a bit inconsistent now day, i will make sure that i will be consistent.
If there is any error in any code you can say to me.
The next project will be for web scraping or sql related.

**NOTE** -->
used concepts:
* loops
* conditionals
* json
* exceptional handling
