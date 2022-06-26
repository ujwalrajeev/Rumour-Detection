import csv
import tweepy
import ssl

def getreplies(url):
    

    ssl._create_default_https_context = ssl._create_unverified_context

    # Oauth keys
    consumer_key = "pXIBM3atLaxe8QC84nOEEMJpL"
    consumer_secret = "lYunBiif0Ggl2iR5LH26hGzOoAbWa7Uuaa61jYtX8HlWAZ9pS1"
    access_token = "1489493682302894084-VKf9q5gRhsuzLViTvxl335fHEbUsLm"
    access_token_secret = "hPa69IDi2BlflJm3iUjDfAMkYG7yR5qcIwpLGoWRpjMyr"

    # Authentication with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
    #name = 'CMBCNFT'
    #tweet_id = '1531793256152854528'

    #get username and tweet id
    a = url.split("/")
    name = a[3]
    tweet_id = a[5]
    

    replies=[]
    for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name, result_type='recent').items(1000):
        #print(tweet)
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                 #print(tweet)
                 replies.append(tweet)



    with open('replies_clean.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
        csv_writer.writeheader()
        for tweet in replies:
            row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
            csv_writer.writerow(row)



    print("Replies stored")






