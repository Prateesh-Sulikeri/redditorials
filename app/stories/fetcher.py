import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,  
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
)

def fetch_stories(subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Fetching trending, underrated, and popular stories
        trending_stories = [story for story in subreddit.top(limit=5) if story.is_self]
        popular_stories = [story for story in subreddit.hot(limit=5) if story.is_self]
        underrated_stories = [story for story in subreddit.new(limit=5) if story.is_self]

        if not trending_stories and not popular_stories and not underrated_stories:
            print(f"No text-based stories found in r/{subreddit_name}.")
            return None

        stories = {
            "trending": [{"title": story.title, "score": story.score, "url": story.url, "description": story.selftext} for story in trending_stories],
            "popular": [{"title": story.title, "score": story.score, "url": story.url, "description": story.selftext} for story in popular_stories],
            "underrated": [{"title": story.title, "score": story.score, "url": story.url, "description": story.selftext} for story in underrated_stories]
        }

        return stories  # Return the constructed stories dictionary

    except praw.exceptions.PRAWException as e:
        print(f"An error occurred while fetching data from r/{subreddit_name}: {e}")
        if '403' in str(e):
            print("This may be due to subreddit restrictions or privacy settings.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    return stories
