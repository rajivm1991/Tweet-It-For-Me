Tweet-It-For-Me
===============

A Very simple app for tweeting a message to twitter wall and get your friends tweets. You can either use it in command line to tweet your message or Save your tweets in tweet_stack.txt and tell the cronjob to automatically send tweets for you. ~ Enjoy Tweeting

Usage:
------

### Commandline usage:

Copy the **tweet** script file to your **/usr/bin/** directory

#### To Tweet a tweet:

- $ **tweet** "Hi [@rajivm1991](http://twitter.com/rajivm1991) Tweet-It-For-Me is very usefull"

- $ **tweet** "Hi [@rajivm1991](http://twitter.com/rajivm1991) your blog [GulzarManzil.tk](http://gulzarmanzil.tk) is awesome ;-)"

#### To Get your friends's recent tweets:

- $ **tweet** -g

#### To Get the recent tweets of a particular user(s):

- $ **tweet** -g [@rajivm1991](http://twitter.com/rajivm1991) [@ijeyanthan](http://twitter.com/ijeyanthan)

### Automate your Tweets:

Open your terminal and follow the steps below,

step1: $ crontab -e

step2: Add the line

    0,30 * * * * python ~/snowfall/snowspace/Tweet-It-For-Me/tweet_it_for_me.py

and save the cronjob file.

step3: Save your tweet messages one per line in the **tweet_stack.txt**

step4: Just go and do your work or sleep :-).. your messeges will be one by one in 30 minute intervals.

Note:
-----

- You must register for Twitter API and fill your API credentials in the **credentials.json** file

- **snowfall/snowspace/Tweet-It-For-Me/tweet_it_for_me.py** is where I saved my files, you give your file path in both **cronjob** and **tweet** script file also.

