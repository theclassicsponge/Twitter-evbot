import tweepy
import time
import configparser

config = configparser.ConfigParser()
config.read('keys.ini')

auth = tweepy.OAuthHandler(f'{config["KEY"]["keyp1"]}', f'{config["KEY"]["keyp2"]}')
auth.set_access_token(f'{config["KEY"]["authp1"]}', f'{config["KEY"]["authp2"]}')

# Create API object
API = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = API.me()

search = 'electriccar'
nrTweets = 500


def like_by_ec():
    for tweet in tweepy.Cursor(API.search, search).items(nrTweets):
        try:
            print('Tweet Liked')
            tweet.favorite()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def follower():
    for follower in tweepy.Cursor(API.followers).items():
        try:
            print('Followed Follower')
            follower.follow()
            time.sleep(10)
        except tweepy.TweepError as f:
            print(f.reason)
        except StopIteration:
            break


follower()

like_by_ec()


