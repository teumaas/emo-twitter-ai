from requestAPI import RequestAPI
from tweetSanitizer import cleanTweets
from textblob import TextBlob
import csv
from datetime import date, datetime

def writeReport(searchTerm, amountOfTweets, language):
    #Initialize Request API 
    api = RequestAPI(searchTerm, amountOfTweets, language)
    # Creates CSV fieldnames.
    fieldNames = ['original_tweet', 'sanitized_tweet', 'polarity', 'rating']
    # Creates filename for CSV
    filename = 'data/%s-report-%s-%s.csv' %(searchTerm, datetime.now().strftime('%d_%m_%y'), datetime.now().strftime("%H_%M_%S"))

    #Start writing CSV.
    with open(filename, 'w') as csvfile:    
        csvwriter = csv.writer(csvfile, delimiter=';')  
        csvwriter.writerow(fieldNames)  
        
        #Loops though API results and rates the polarity based on rating.
        for result in api.getData():
            rows =  { result : 'original_tweet',  cleanTweets(result): 'sanitized_tweet', TextBlob(cleanTweets(result)).sentiment.polarity: 'polarity'}

            if TextBlob(cleanTweets(result)).sentiment.polarity >= 0.20:
                rows.update({'Positive': 'rating'})
                csvwriter.writerow(rows)
            elif TextBlob(cleanTweets(result)).sentiment.polarity == 0.0:
                rows.update({'Natural': 'rating'})
                csvwriter.writerow(rows)
            else:
                rows.update({'Negative': 'rating'})
                csvwriter.writerow(rows)

    print("\n Report generation complete! It can be found at the following path:", filename)

#Input for user.
searchterm = input("\n Enter a search term: ")
while True:
  try:
    amountOfTweets = input("\n Enter amount of tweets between 1 and 200: ")
    if amountOfTweets.isdigit():
       amountOfTweets=int(amountOfTweets)
    else:   
       raise ValueError()
    if 1 <= amountOfTweets <= 200:
        break
    raise ValueError()
  except ValueError:
    print("\n Input must be an between 1 and 200.")

writeReport(searchterm, amountOfTweets, 'en')