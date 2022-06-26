import tweepy

def gettweettext(url):
    
    consumer_key = "pXIBM3atLaxe8QC84nOEEMJpL"
    consumer_secret = "lYunBiif0Ggl2iR5LH26hGzOoAbWa7Uuaa61jYtX8HlWAZ9pS1"
    access_token = "1489493682302894084-VKf9q5gRhsuzLViTvxl335fHEbUsLm"
    access_token_secret = "hPa69IDi2BlflJm3iUjDfAMkYG7yR5qcIwpLGoWRpjMyr"
  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
    auth.set_access_token(access_token, access_token_secret)
  
    api = tweepy.API(auth)

    a = url.split("/")
    id = a[5]
  
    status = api.get_status(id)
  
    text = status.text

    print("---------------------Completed running gettweettext---------------------")
  
    return(text)
