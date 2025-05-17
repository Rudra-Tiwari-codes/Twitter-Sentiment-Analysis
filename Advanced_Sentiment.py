# Install required libraries (for Jupyter/Colab only)
# !pip install nltk pycountry langdetect wordcloud Pillow

# Import Libraries
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SI
from langdetect import detect
from wordcloud import WordCloud, STOPWORDS
import nltk
import re
import string

# Download VADER Lexicon
nltk.download('vader_lexicon')

# Twitter API Authentication
consumer_key = "wcw8VnSPTWooQILA6SWdqizjy"
consumer_secret = "DZYTqymQyTfDC5v9sgqRpnPKxsNykMbKbMqONvBKTElbAUkkAu"
access_token = "1520059770958360576-Q0jSog3jclBRJO7poJVVDPVuAFqFQD"
access_token_secret = "7phlweTKEfs8ymiv0sgNeGKwCEDtAgSaC3RkWDrZFAX0O"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Sentiment Analysis Settings
def percentage(part, whole):
    return 100 * float(part) / float(whole)

keyword = 'Unemployment'
no_of_tweets = 1000
tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(no_of_tweets)

# Sentiment Counters
positive = 0
negative = 0
neutral = 0
polarity = 0

# Lists to store tweets
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

analyzer = SI()

# Analyze Tweets
for tweet in tweets:
    text = tweet.text
    tweet_list.append(text)
    analysis = TextBlob(text)
    score = analyzer.polarity_scores(text)

    neg = score['neg']
    neu = score['neu']
    pos = score['pos']

    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(text)
        negative += 1
    elif pos > neg:
        positive_list.append(text)
        positive += 1
    else:
        neutral_list.append(text)
        neutral += 1

# Calculate Percentages
positive_pct = percentage(positive, no_of_tweets)
negative_pct = percentage(negative, no_of_tweets)
neutral_pct = percentage(neutral, no_of_tweets)
polarity_pct = percentage(polarity, no_of_tweets)

# Format percentages
positive_pct = format(positive_pct, '.1f')
negative_pct = format(negative_pct, '.1f')
neutral_pct = format(neutral_pct, '.1f')

# Print tweet counts
print('Total Tweets:', len(tweet_list))
print('Positive Tweets:', len(positive_list))
print('Negative Tweets:', len(negative_list))
print('Neutral Tweets:', len(neutral_list))

# Pie Chart
labels = [
    f'Positive [{positive_pct}%]', 
    f'Neutral [{neutral_pct}%]', 
    f'Negative [{negative_pct}%]'
]
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue', 'red']

plt.figure(figsize=(8, 6))
plt.pie(sizes, colors=colors, startangle=90, autopct='%1.1f%%')
plt.title('Sentiment Analysis Result for "Unemployment"')
plt.legend(labels)
plt.axis('equal')
plt.tight_layout()
plt.show()
