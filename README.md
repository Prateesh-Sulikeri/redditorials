# Redditorials

Redditorials is a project designed to fetch trending, popular, and underrated stories from Reddit based on user-selected subreddits and preferences. It utilizes FastAPI for building backend APIs and can be extended with AI-based features like summarization and text-to-speech in the future.

## Features
- Fetches stories from Reddit based on subreddit keyword search.
- Categorizes stories into trending, popular, and underrated.
- Backend APIs built using FastAPI for scalable integration.
- Modular architecture to easily add features like AI-based story summarization and text-to-speech.
- Future roadmap includes video generation based on stories for social media platforms.
  
## Project Structure
```py
Redditorials/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── reddit_search.py
│   ├── stories/
│   │   ├── __init__.py
│   │   └── fetcher.py
│   ├── config.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup
To set up the project on your local machine, follow these steps:

- Clone the repository:
```bash
git clone https://github.com/your-github-username/repository-name.git
```
- Navigate to the project directory:
```bash
cd Redditorials
```
- Configure Reddit API Access:

To use the Reddit API, you will need to create a Reddit account if you don't have one.
Go to Reddit's Developer Portal and create a new app.
After creating the app, you'll get the following credentials:
```py
client_id
client_secret
user_agent
username
password
```
- Edit config.py:

Open the config.py file located inside the app/ directory.
Replace the placeholders with your actual Reddit API credentials:
``` py
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USER_AGENT = "your_user_agent"
REDDIT_USERNAME = "your_reddit_username"
REDDIT_PASSWORD = "your_reddit_password"
```
- Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Install Dependencies:
```bash
pip install -r requirements.txt
```
- Run the application:
```bash
uvicorn app:app --reload
```
The API should now be running on http://127.0.0.1:8000.

## API Endpoints
- /subreddits
   * Method: GET
   * Description: Fetches stories from subreddits based on the given keyword.
   * Parameters:
      keyword (query parameter) – The keyword to search subreddits.
   * Response:
   * Returns the subreddit name and stories if found.
   * Returns 404 error if no relevant subreddit or stories are found.
   * Example:
   ```bash
   curl "http://127.0.0.1:8000/subreddits?keyword=horror"
   ```
## Future Features (Roadmap)
- AI Summarization: Summarize each fetched Reddit story.
- Text-to-Speech: Convert the text of the story into speech.
- Video Generation: Automate video creation for platforms like YouTube and TikTok based on selected stories.
- Community-Driven Features: Make the project community-driven for collaboration and improvement.

