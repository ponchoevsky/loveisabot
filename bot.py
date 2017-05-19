import tweepy
from time import sleep


consumer_key = '2TlIMKxYX9iHRDtZuJFRBTGZB'
consumer_secret = 'SHYXWlCxvn2JrKO5OoF1TJRej2VL3mYgMGPpoJDf3dIFCYGQNh'
access_token = '865013763535118336-dYJZzpi2J5msDeGF8N40i3z8KigWYNT'
access_token_secret = 'JaoZ4fjSOzo24idyzKpDu9YZcuXDD4JPRa6WLPpbcmsNH'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


file = open('adjectives_file.txt','r')
file_lines = file.readlines()
file.close()


for line in file_lines:
	try:
		api.update_status(line)
		sleep(60)
	except tweepy.TweepError as e:
		print e.reason
		sleep(5)