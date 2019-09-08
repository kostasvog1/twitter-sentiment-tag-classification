from tweepy import OAuthHandler
import pandas as pd

def fetch_tweets(screen_name,auth_api):
    
    alltweets = []  
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = auth_api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
    #        print "getting tweets before %s" % (oldest)

       #all subsiquent requests use the max_id param to prevent duplicates
       new_tweets = auth_api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

       #save most recent tweets
       alltweets.extend(new_tweets)

       #update the id of the oldest tweet less one
       oldest = alltweets[-1].id - 1

    #        print "...%s tweets downloaded so far" % (len(alltweets))

    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    df = pd.DataFrame(outtweets,columns=['Date','free_text']) 
    return df