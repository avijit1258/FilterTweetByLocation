import tweepy
import config

def connection():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_token, config.access_token_secret)

  api = tweepy.API(auth)
  
  public_tweets = api.home_timeline()
  user = api.get_user('NzOishie') 
  print(user)

  