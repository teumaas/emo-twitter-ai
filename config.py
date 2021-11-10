import tweepy
import os

# Sets the Twitter api auth
def getAPI():
   # Add your api keys 
   auth = tweepy.OAuthHandler('', '')
   auth.set_access_token('', '')
   return tweepy.API(auth)
