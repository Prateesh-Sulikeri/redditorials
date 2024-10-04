import requests

def subreddit_selector(keyword):
    url = f"https://www.reddit.com/subreddits/search.json?q={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    data = response.json()

    subreddits = []
    for item in data['data']['children']:
        subreddits.append(item['data']['display_name'])

    if not subreddits:
        print("No subreddits found for this keyword")
        return None
    
    print("Here are the relevent subreddits: ")
    for index, subreddit in enumerate(subreddits):
        print(f"{index + 1}. {subreddit}")
    
    subreddit_number = int(input("Choose a subreddit number: ")) - 1;
    if subreddit_number < 0 or subreddit_number >= len(subreddits):
        print("Invalid Subreddit number. PLease try again!")
        return None 
    
    return subreddits[subreddit_number]