import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

# Twitter Developer credentials
consumer_key = "wcw8VnSPTWooQILA6SWdqizjy"
consumer_sec = "DZYTqymQyTfDC5v9sgqRpnPKxsNykMbKbMqONvBKTElbAUkkAu"
access_token = "1520059770958360576-Q0jSog3jclBRJO7poJVVDPVuAFqFQD"
access_token_sec = "7phlweTKEfs8ymiv0sgNeGKwCEDtAgSaC3RkWDrZFAX0O"

# Twitter authentication and API setup
auth = tweepy.OAuthHandler(consumer_key, consumer_sec)
auth.set_access_token(access_token, access_token_sec)
api = tweepy.API(auth)

# Search tweets related to a topic
query = 'unemployment'
tweet_data = api.search_tweets(q=query, count=100)

# Initialize sentiment counters
pos = 0
neg = 0
neu = 0

# Analyze tweet sentiments
for tweet in tweet_data:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        print("Positive")
        pos += 1
    elif polarity == 0:
        print("Neutral")
        neu += 1
    else:
        print("Negative")
        neg += 1

# Plot sentiment distribution
plt.figure(figsize=(6, 6))
plt.pie([pos, neg, neu], labels=['Positive', 'Negative', 'Neutral'], autopct="%1.1f%%", colors=["green", "red", "blue"])
plt.title("Sentiment Analysis on Tweets about 'Unemployment'")
plt.show()
