import praw

class RedditScraper:
    def __init__(self, client_id="nDetjmiaQ9zMMLGYVISZ7Q", client_secret="rx3qUObEzc5ArP2Xqdo3GTXqEbf7BQ", user_agent="book_suggestions_scraper/0.1 by kovidnathp"):
        
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def get_posts(self, subreddit_name, sort="top", time_filter='day', limit=100):
        subreddit = self.reddit.subreddit(subreddit_name)
        if sort == "top":
            return subreddit.top(limit=limit, time_filter=time_filter)
        elif sort == "new":
            return subreddit.new(limit=limit)
        elif sort == "hot":
            return subreddit.hot(limit=limit)
        else:
            raise ValueError("Invalid sort option.")
    
    def get_comments(self, post_id):
        submission = self.reddit.submission(id=post_id)
        submission.comments.replace_more(limit=0)
        return submission.comments.list()


    def extract_post_data(self, post):
        return {
            "id": post.id,
            "title": post.title,
            "author": str(post.author),
            "score": post.score,
            "created_utc": post.created_utc,
            "url": post.url,
            "num_comments": post.num_comments,
            "selftext": post.selftext
        }    

    