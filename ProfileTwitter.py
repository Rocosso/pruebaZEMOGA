import tweepy
import json


API_key = "KRy7l0v8wex3w8Sy5zThai3Ea"
API_secret_key = "X2eBm0Y21kYEuR74W3Frqc2JVIizOj8Q1EVGatDsEVVEJo0ucu"
Access_token = "1220032047516921859-otvXjhExyUTZ5GLxssc9h5ORqtPZja"
Access_token_secret = "tmJKqM4ORfQW6CH7wIVV8uKNpmSEmeFAP8lYwGb19uYjj"

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

user_id = "57741058"
user = api.get_user(screen_name="twitterapi")
statuses = api.user_timeline(id=user.id, count=5)

#print(json.dumps(user._json, indent=2))
print(user.name)
print(user.description)
print(user.profile_image_url)
print(statuses)