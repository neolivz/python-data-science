from textblob import TextBlob
import tweepy
import csv

consumer_key = 'N1q2LYsuCe5FRVUuiiKka6XwT'
consumer_secret = 'YEs3n64maqlRFV6UwXz1Hx0pWPVK0Nc2tJFDhSgkETdtNkqegq'

access_token = '2384703540-XNSzXXpDxL7HMdbCct5PSfSQ7fZQ8c8TwTbfCVb'
access_token_secret = '31qHHzq8LUzQP93acaUi8rApS89HJ6L06BeTz7bRHrTtG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#lfc')

with open('tweets.csv', 'w') as csvfile:
    fieldnames = ['Tweet', 'Polarity', 'Subjectivity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        polarity = analysis.sentiment.polarity
        if(polarity > 0):
            writer.writerow({'Tweet': tweet.text, 'Polarity': analysis.sentiment.polarity, 'Subjectivity': analysis.sentiment.subjectivity})

