import tweepy
import config

def connection():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_token, config.access_token_secret)

  api = tweepy.API(auth)
  return api

def searchKeywords(keyword):
  api = connection()
  tweets = api.search(keyword,count = 5)
  returned_tweets = {}

  for tweet in tweets:
    returned_tweets[tweet.id] = tweet.text
  print(returned_tweets)