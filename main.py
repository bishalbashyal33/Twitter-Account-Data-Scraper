import tweepy

# Set up your Twitter API credentials here
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET'

# Authenticate with Twitter's API using Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Set your inputs here
social_media_platform = 'Twitter'  # Example: Twitter
account_name = 'OpenAI'  # Example: OpenAI
n = 10  # Example: 10
keywords = ['artificial intelligence', 'machine learning']  # Example keywords

# Get the most recent n posts from the account
posts = api.user_timeline(screen_name=account_name, count=n)

# Loop through each post and check for the keywords in the comments
for post in posts:
    comments = api.search(q='to:{} filter:replies'.format(account_name), since_id=post.id, tweet_mode='extended')
    for comment in comments:
        text = comment.full_text.lower()
        if any(keyword in text for keyword in keywords):
            # Print out the relevant information for the post and comment
            print('Social Media Platform: {}'.format(social_media_platform))
            print('Account Name: {}'.format(account_name))
            print('Post Text: {}'.format(post.text))
            print('Comment Text: {}'.format(text))
            print('Keyword(s) Found: {}'.format(', '.join(keyword for keyword in keywords if keyword in text)))
            print('\n')