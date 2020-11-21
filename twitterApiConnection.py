import tweepy
import config
import tweetSummarization
import topicModeling
import sentimentAnalysis

def connection():
  auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
  auth.set_access_token(config.access_token, config.access_token_secret)

  api = tweepy.API(auth)
  return api

def searchKeywords(keyword, count):
    api = connection()
    filters = " -is:retweet -has:media -has:images -has:videos -has:links lang:en"
    
    returned_tweets = {}
    tweets = tweepy.Cursor(api.search,
                q = keyword + filters,
                lang = "en",
                until = "2020-11-19",
                count = 100, 
                wait_on_rate_limit = True).items(1000)

    for tweet in tweets:
        returned_tweets[tweet.id] = tweet.text
        
    print('.......Tweet count....', len(returned_tweets))
    return returned_tweets

def sendDirectMessage(user, message):
    api = connection()
    user = api.get_user(user)
    api.send_direct_message(user.id,message)

def sendDirectMessageWithMedia(user, message, attachment, attachment_id):
    api = connection()
    user = api.get_user(user)
    api.send_direct_message(user.id,message,attachment,attachment_id)





def get_trends():

    api = connection()

    trends_location = api.trends_available()

    # to do
    # api.trends_place(id) returns top 10 trending topics for a given WOEID


    for tl in trends_location:
        print(tl)
        print(api.trends_place(tl['woeid']))
    
    return trends_location
