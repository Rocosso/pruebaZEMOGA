import tweepy
import json

def getTweets():
    API_key = "KRy7l0v8wex3w8Sy5zThai3Ea"
    API_secret_key = "X2eBm0Y21kYEuR74W3Frqc2JVIizOj8Q1EVGatDsEVVEJo0ucu"
    Access_token = "1220032047516921859-otvXjhExyUTZ5GLxssc9h5ORqtPZja"
    Access_token_secret = "tmJKqM4ORfQW6CH7wIVV8uKNpmSEmeFAP8lYwGb19uYjj"

    auth = tweepy.OAuthHandler(API_key, API_secret_key)
    auth.set_access_token(Access_token, Access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    user_id = "57741058"
    user = api.get_user(screen_name="twitterapi")
    tweets = api.user_timeline(id=user.id, count=5)
    tweet1 = tweets[0]
    tweet2 = tweets[1]
    tweet3 = tweets[2]
    tweet4 = tweets[3]
    tweet5 = tweets[4]

    tweets = {"name":user.name, "experience":user.description,
              "image":user.profile_image_url, "T1":tweet1.text,"T2":tweet2.text,
              "T3":tweet3.text,"T4":tweet4.text,"T5":tweet5.text}
    return tweets

tweets = getTweets()
for k,v in tweets.items():
    print ("%s -> %s" %(k,v))
#print(tweets)