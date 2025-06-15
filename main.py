import praw

reddit= praw.Reddit('case')

subreddit = reddit.subreddit("Python")

for submission in subreddit.hot(limit=1):
    print("제목: ", submission.title)
    print("내용: ", submission.selftext)
    print("점수: ", submission.score)
    print("------------\n")