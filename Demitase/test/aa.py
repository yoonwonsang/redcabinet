import tweepy

CONSUMER_KEY = 'QN5inGo2xmA7717qxCQ'
CONSUMER_SECRET = 'dxOvz4PmcWBrQlEkFpK9lu68dT1q0QNEB4UVMYWpmRI'


def copy(auth):
    print "copy"
    print auth

def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    print "main"
    print auth
    copy(auth)
main()
