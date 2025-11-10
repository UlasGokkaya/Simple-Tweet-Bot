import tweepy
import os # Necessary to read environment variables (GitHub Secrets)


# --- Configuration: API Keys (Read from Environment) ---
API_KEY=os.environ.get("TWITTER_API_KEY")
API_KEY_SECRET=os.environ.get("TWITTER_API_SECRET")
ACCESS_TOKEN=os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET=os.environ.get("TWITTER_ACCESS_SECRET")


#Check if required keys are loaded
if not all([API_KEY,API_KEY_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET]):
    print("Error: Required Twitter API keys were not loaded from environment variables.")
    print("Please ensure TWITTER_API_KEY, etc., are correctly set in GitHub Secrets.")
    exit()

#Tweet content (Simple static text)
tweet_content="This is my simple automated tweet. Everything is secure!"

try:
    #Connect to X
    client=tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_KEY_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    client.create_tweet(text=tweet_content)
    print("Tweet sent successfully.")
# Catch specific API errors (e.g., rate limits, invalid credentials)
except tweepy.TweepyException as tweepyerror:
    print("ERROR: Tweepy/API error occurred while sending the tweet.")
    print(f"Details: {tweepyerror}")
# Catch all other unexpected errors
except Exception as e:
    print("ERROR: An unexpected error occured.")
    print(f"Details: {e}")
finally:
    print("The work of code has done.")
