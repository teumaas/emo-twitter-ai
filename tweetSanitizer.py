from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
import string

#Set of typed emoticons to filter out.
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3',
])

#Set of typed emoticons to filter out.
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
])

#Combines the happy/sad emoticons.
emoticons = emoticons_happy.union(emoticons_sad)

#Removes all emojis from the string(Tweet)
def removeEmoji(string):
    emoji_pattern = re.compile("["
        u"\U00010000-\U0010ffff"
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

#Main function to sanitize tweet.
def cleanTweets(tweet):
    # List of stopwords example: https://www.researchgate.net/profile/Tran_Ho2/publication/262182428/figure/tbl1/AS:669687805390875@1536677423664/Example-of-stop-words.png
    stop_words = set(stopwords.words('english'))
   
    #Removes RT and Junk ASCII Symbols.
    tweet = re.sub(r'RT', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+','', tweet)

    #Removes URLS
    tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', tweet)
    
    #Removes Emoji.
    tweet = removeEmoji(tweet)

    #Tokenize string and lowercases string.
    word_tokens = word_tokenize(tweet.lower())
    
    #Filters tweet if it's contains a stopword.
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []

    #Joins cleaned tokenized words in a string.
    for w in word_tokens:
        if w not in stop_words and w not in emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)