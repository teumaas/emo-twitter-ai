from config import getAPI
import tweepy
import os

api = getAPI()

#In this class all the request settings will be set for the API.
class RequestAPI:
    def __init__(self, searchTerm, amountOfResult, language):
        self._searchTerm = searchTerm
        self._language = language
        self._amountOfResult = amountOfResult

    #Getters and Setters
    @property
    def searchTerm(self):
        return self._searchTerm
        
    @searchTerm.setter
    def searchTerm(self, value):
        self._searchTerm = value

    @property
    def language(self):
        return self._language
        
    @language.setter
    def language(self, value):
        self._language = value

    @property
    def amountOfResult(self):
        return self._amountOfResult
        
    @amountOfResult.setter
    def amountOfResult(self, value):
        self._amountOfResult = value

    #Pulls the data from twitter.
    def getData(self):
        rawTweets = []

        for tweet in tweepy.Cursor(api.search, q=self._searchTerm, lang=self._language, include_rts=False).items(self._amountOfResult):
            rawTweets.append(tweet.text)
        return rawTweets