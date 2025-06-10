from RedditScraper import RedditScraper

reddit  = RedditScraper()
posts = reddit.get_posts("booksuggestions", sort="top", time_filter='day', limit=10)
for post in posts:
    post_data = reddit.extract_post_data(post)
    print(post_data)
    comments = reddit.get_comments(post.id)
    for comment in comments:
        print(comment)
