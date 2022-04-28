import string
from collections import Counter
from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import cgi, os

def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    negative = score['neg']
    positive = score['pos']
    if negative > positive: 
        sentiment = 'Negatyive Sentiment!'
    else: 
        sentiment = 'Positive Sentiment!'
    return sentiment

form = cgi.FieldStorage()

# Text Input
#text = open('read.txt', encoding='utf-8').read()

def analyze(text):
    # Clean Text (lowercase, remove punctiations)
    lowercase_text = text.lower()
    print(string.punctuation) # List of punctuations in python
    cleaned_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokenized_words = word_tokenize(cleaned_text, 'english')

    stopwords = nltk.corpus.stopwords.words('english')
    final_words = []
    for word in tokenized_words:
        if word not in stopwords:
            final_words.append(word)

    # NLP Emotion ALgorithm
    emotion_list = []
    with open('emotions.txt', 'r') as f:
        for line in f: 
            line_clear = line.replace('\n', '').replace(',', '').replace("'", '').strip() # remove new line, quotation, comma
            word, emotion = line_clear.split(':')
            
            if word in final_words:
                emotion_list.append(emotion)
    
    detected_emotions = Counter(emotion_list)           
    print(detected_emotions)
    
    sentiment = sentiment_analyze(cleaned_text)

    fig, axl = plt.subplots()
    axl.bar(detected_emotions.keys(), detected_emotions.values())
    fig.autofmt_xdate()
    plt.savefig('static/graph.png')
    plt.show()
    
    return sentiment