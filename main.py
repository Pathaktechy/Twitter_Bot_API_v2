import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("JIEZf1pA5AnsKSEMzR6AJRtdL",
    "kUuDRX6j6lvrCriQnALII2wgFxOZqK8kUeIMytuginF5GHybKN")
auth.set_access_token("1645261847074054144-sCItaEEaVfy2OsR37NqJExzGqqndFD",
    "ZzCwgzbfXxNTvgOg6ynx6OkR2weLQCQjmGeKk4ZHKnrAf")

api = tweepy.API(auth)
try :
    api.verify_credentials()
    print("Authentication OK ")
except :
    print("Error during authentication ")


target_screen_name = "kanak_shilledar"


try:
    # Retrieve user information
    user_data = api.get_user(screen_name=target_screen_name)

    print(f"User: {user_data.name} (@{user_data.screen_name})")
    print(f"Followers: {user_data.followers_count}")
    print(f"Following: {user_data.friends_count}")
    print(f"Tweets: {user_data.statuses_count}")

except tweepy.error.TweepError as e:
    print(f"Error: {e}")



