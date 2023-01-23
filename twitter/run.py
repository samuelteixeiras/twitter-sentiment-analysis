from twitter_auth import API_KEY, API_SECRET
import tweepy as tp
from datetime import datetime
import csv
import time

SOURCE_KEYWORDS = 'electric car' + ' -filter:retweets'

auth = tp.OAuth2AppHandler(
    API_KEY, API_SECRET
)
api = tp.API(auth)

def save_to_csv(tweets):
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in tweets]
    now = datetime.now()
    formatted_now = now.strftime("%m_%d_%Y_%H_%M_%S")
    print(f'electric_{formatted_now}_tweets.csv')
    
    #write the csv  
    with open(f'electric_{formatted_now}_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
        

def get_tweets():
    tweets = api.search_tweets(q=SOURCE_KEYWORDS, count=100, tweet_mode='extended')
    print(tweets.count)
    save_to_csv(tweets)

def background_process():
    while True:
        formatted_now = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        print(f"running {formatted_now}")
        get_tweets()
        time.sleep(60 * 5) # waiting time in seconds > 5 min

if __name__ == "__main__":
    background_process()
    
