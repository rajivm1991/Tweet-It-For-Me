def make_tweet_list(tweet):
    if len(tweet) <= 140:
            return [tweet]
    else:
        tweet_list = []
        while tweet:
            tweet_list.append(tweet[:137] + ('...' if tweet[137:] else ''))
            tweet = tweet[137:]
        return tweet_list


def pop_a_tweet(tweet_stack='tweet_stack.txt'):
    import os
    DATA_DIR = os.path.dirname(os.path.abspath(__file__))
    STACK_FILE = os.path.join(DATA_DIR, tweet_stack)
    tweets = open(STACK_FILE, 'r').readlines()
    if tweets:
        popped_tweet = tweets.pop().strip()
        f = open(STACK_FILE, 'w')
        f.writelines(tweets)
        f.close()
        return make_tweet_list(popped_tweet)


import sys
tweet_list = []
for tweet in sys.argv[1:]:
    tweet_list += make_tweet_list(tweet)
if not tweet_list:
    tweet_list = pop_a_tweet()

#"""
if tweet_list:
    from twitter import Api as TwitterApi
    print 'Attempting Twitter Api Login...'
    Twitter = TwitterApi(
        consumer_key="FILL YOUR TWITTER API CREDENTIAL HERE",
        consumer_secret="FILL YOUR TWITTER API CREDENTIAL HERE",
        access_token_key="FILL YOUR TWITTER API CREDENTIAL HERE",
        access_token_secret="FILL YOUR TWITTER API CREDENTIAL HERE"
    )
    ME = Twitter.VerifyCredentials().screen_name
    print "Current user is @" + ME
    if tweet_list[0] == '-g':
        user_list = tweet_list[1:]
        if user_list:
            for user in user_list:
                print
                print "Recent tweets from " + user + ":"
                print "===================" + "=" * (len(user) + 1)
                tweets = Twitter.GetUserTimeline(user[1:])
                #count = 0
                for tweet in tweets:
                    #if count == 5: break;
                    print "$", tweet.text
                    #count += 1
        else:
            print
            print "Recent tweets from friends:"
            print "==========================="
            for tweet in Twitter.GetFriendsTimeline():
                if tweet.user.screen_name != ME:
                    print "@" + tweet.user.screen_name + ":", tweet.text
    else:
        for tweet in tweet_list:
            Twitter.PostUpdate(tweet)
            print 'Tweeting:', tweet
        print "Tweeted successfully!"
else:
    print "Oops!. No tweets found in the tweet_stack!"
#"""
