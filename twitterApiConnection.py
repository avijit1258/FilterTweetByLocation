import tweepy
import config
import tweetSummarization

def connection():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_token, config.access_token_secret)

  api = tweepy.API(auth)
  return api

def searchKeywords(keyword, count):
  api = connection()
  tweets = api.search(keyword,count = count)
  returned_tweets = {}

  for tweet in tweets:
    returned_tweets[tweet.id] = tweet.text
  # returned_tweets_as_list = list(returned_tweets.values())
  
  return returned_tweets

def sendDirectMessage(user, message):
  api = connection()
  user = api.get_user(user)
  api.send_direct_message(user.id,message)

def sendDirectMessage(user, message, attachment, attachment_id):
  api = connection()
  user = api.get_user(user)
  api.send_direct_message(user.id,message,attachment,attachment_id)

def summarize_tweets():

    tweets = searchKeywords('covid', 100)
    print(tweetSummarization.text_summarize(tweets))