from fastapi import FastAPI, HTTPException
from reddit_search import subreddit_selector
from stories.fetcher import fetch_stories

app = FastAPI() 

@app.get("/subreddits")
def get_subreddits(keyword: str):
    subreddit_name = subreddit_selector(keyword)
    if not subreddit_name:
        raise HTTPException(status_code=404, detail="Subreddit not found!!")
    
    print(f"Selected Subreddits: {subreddit_name}")

    stories = fetch_stories(subreddit_name)
    if not stories:
        raise HTTPException(status_code=404, detail="No relevent stories found")

    print(f"Fetching stories from subreddit: {subreddit_name}")
    print("Fetched stories: ", stories)

    return {"subreddit" : subreddit_name, "stories" : stories}
