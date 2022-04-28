import GetOldTweets3 as got
import string

def getTweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Urkaine')\
                                            .setSince("2022-01-01")\
                                            .setUntil("2022-03-31")\
                                            .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    tweets_text = [[tweets_text] for tweets in tweets]
    for tweet in tweets:
        tweets_text.append(tweet.text)
    print(tweets_text)
    
text = ''
tweets_text = getTweets()
length = len(tweets_text)

for i in range(0, length):
    text = tweets_text[i][0] + " " + text

# Clean Text (lowercase, remove punctiations)
lowercase_text = text.lower()
cleaned_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))

# Tokenization
tokenized_words = cleaned_text.split()