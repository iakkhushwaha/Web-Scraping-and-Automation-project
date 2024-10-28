import re 
import tweepy

# CLIENTID = "RHJfM0J4dWVsV1ljT0hqVGxpMkQ6MTpjaQ"
# CLIENTSECRET = "pcf17IIYIs6xwLJwXgabL_Ifv7MxxjTkya0EUZfjhSeS5uQWKH"

API_KEY = "4VdbxnyBGTvZ2sjPjSZLc9xiT"
API_KEY_SECRET = "moTCCmSgC1u8Efa6t4LnfSlbGkpAO13ZLxviN8zajjiVS1A2gL"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHlVwAEAAAAACPaJCZYQZYidw2X8CzwJknvmtv0%3D0lcQHsIhEXhq7FvTnj5bMVHyRViCUgZG6AG7XcwlZTdP19BB6u"
ACCESS_TOKEN = "1750115991047290880-oqFlVfTm3u5z3NjGRhCxCyozLCpI8r"
ACCESS_TOKEN_SECRET = "FtR2kvcmFStws1xfLMf5yHNcfNgAsoLLFzgIvx4quqWhs"

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,consumer_key=API_KEY , consumer_secret = API_KEY_SECRET ,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



with open('input.txt' , 'r') as f:
    tweets = f.read().splitlines()

print(tweets[0].__contains__("1."))
tweets= [tweet  for tweet in tweets if not re.match(r'^(100|[1-9][0-9]?)\.', tweet)]
print(tweets[0].__contains__("1."))

if re.match(r'^(100|[1-9][0-9]?)\.', tweets[0]) :
        print("yessssssss")

text = ""
tweets_list= []
for t in tweets:
    if t  != '' :
        text += t + "\n"
    if t== '':
import re 
import tweepy

API_KEY = "API_KEY"
API_KEY_SECRET = "API_KEY_SECRET"
BEARER_TOKEN = "BEARER_TOKEN"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,consumer_key=API_KEY , consumer_secret = API_KEY_SECRET ,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET
)
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



with open('input.txt' , 'r') as f:
    tweets = f.read().splitlines()

print(tweets[0].__contains__("1."))
tweets= [tweet  for tweet in tweets if not re.match(r'^(100|[1-9][0-9]?)\.', tweet)]
print(tweets[0].__contains__("1."))

if re.match(r'^(100|[1-9][0-9]?)\.', tweets[0]) :
        print("yessssssss")

text = ""
tweets_list= []
for t in tweets:
    if t  != '' :
        text += t + "\n"
    if t== '':
        text = text.removesuffix("\n")
        tweets_list.append(text)
        # text.remove(t)
        text = ""


# print(tweets_list[30])

# print(len(tweets))


for index, tweet in enumerate(tweets_list):
    try:
        media_path = f"Pictures/tweets/{index+1}.jpg"
        media = api.media_upload(media_path)
        client.create_tweet(
            text=tweet, 
            media_ids=[media.media_id])
        print(f"tweeted {index+1}")
        
    except:
        client.create_tweet(text=tweet)
        print(f"tweeted {index+1}")


