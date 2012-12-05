Tweet-It-For-Me
===============

Very simple app for tweeting a message to twitter wall. You can either use it in commandline to tweet your message or Save your tweets in tweet_stack.py and tell the cronjob to automatically send tweets for you. ~ Enjoy Tweeting

Usage:
------

### Commandline usage:

- python tweet_it_for_me.py "Hi [@rajivm1991](http://twitter.com/rajivm1991) Tweet-It-For-Me is very helpfull"
    
- python tweet_it_for_me.py "Hi [@rajivm1991](http://twitter.com/rajivm1991) your blog [GulzarManzil.tk](http://gulzarmanzil.tk) is very beautiful"

### Automate your Tweets

Open terminal:
    
step1: $ crontab -e

step2: Add the line 

    0,30 * * * * python ~/snowfall/snowspace/Tweet-It-For-Me/tweet_it_for_me.py

and save the cronjob file.

step3: Save your tweet messages one per line in the **tweet_stack.txt**
    
step4: Just go and do your work or sleep :-).. your messeges will be one by one in 30 minute intervals.