import tweepy
import json
from time import sleep
from credentials import *
from keywords import *
from classes.tuit import Tuit
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#data = api.search(q='AyudaCDMX',
#        result_type="recent")
# print(data[1])

tuits = []



counter = 0

while counter < 1:
    data = api.search(q='AyudaCDMX',
            result_type="recent")

    for d in data:
        tuits.append(Tuit(d.author.screen_name, d.text))

    counter += 1

#for t in tuits:
 #   print(t.toString())


for t in tuits:
    for kw in kws:
        if t.getText().find(kw) != -1:
            print(t.toString())
        
