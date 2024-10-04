# Rediditorials

🎉 **Welcome to Rediditorials!** 🎉

Rediditorials is an open-source Reddit bot designed to fetch and summarize interesting stories from various subreddits based on user-defined keywords. The bot categorizes the stories into trending, popular, and underrated, providing a seamless way to explore Reddit content.

## Features

**Keyword Search:** Enter a keyword to fetch relevant subreddits.  
**Story Categories:** Retrieve stories categorized as trending, popular, and underrated.  
**User-Friendly Interface:** Enjoy a simple and engaging command-line interface.  
**Open Source:** Contributions are welcome! Feel free to fork the repository and submit your improvements.  

## Getting Started

### Prerequisites

- Python 3.6 or higher  
- Reddit account for API access  

### Installation

1. Clone the repository:  
```bash
git clone https://github.com/Prateesh-Sulikeri/redditorials.git
cd redditorials
```
2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Create a config.py file in the project root directory with your Reddit API credentials:
```bash
# Reddit API credentials
REDDIT_CLIENT_ID = 'your_client_id'
REDDIT_CLIENT_SECRET = 'your_client_secret'
REDDIT_USER_AGENT = 'RediditorialsBot/0.1'
REDDIT_USERNAME = 'your_username'
REDDIT_PASSWORD = 'your_password'
```
4. Run the bot:
```bash
python bot.py
```
5. Example Usage:
```bash
Enter a keyword to search for relevant subreddits: horror
Fetching stories from r/horror...

🎉 Trending Stories 🎉
📖 Title: Oddity is out on Shudder, go check it out!
   ⭐ Score: 449
   🔗 URL: https://www.reddit.com/r/horror/comments/1frp335/oddity_is_out_on_shudder
```

### Contributing
We welcome contributions! If you'd like to improve Rediditorials, please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.