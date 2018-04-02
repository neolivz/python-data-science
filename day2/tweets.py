from textblob import TextBlob
import tweepy

consumer_key = 'N1q2LYsuCe5FRVUuiiKka6XwT'
consumer_secret = 'YEs3n64maqlRFV6UwXz1Hx0pWPVK0Nc2tJFDhSgkETdtNkqegq'

access_token = '2384703540-XNSzXXpDxL7HMdbCct5PSfSQ7fZQ8c8TwTbfCVb'
access_token_secret = '31qHHzq8LUzQP93acaUi8rApS89HJ6L06BeTz7bRHrTtG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('#lfc')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)