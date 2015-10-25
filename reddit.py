import praw

my_user_agent="TGINE:v1.0 by /u /pailroco"
my_sub_reddit="science"
limite=25

r = praw.Reddit(user_agent=my_user_agent)

subreddit = r.get_subreddit(my_sub_reddit)

for submission in subreddit.get_hot(limit = limite):
    print("Title: "+submission.title)
    print("Text: "+submission.selftext)
    print("Score: "+"%d" % submission.score)
    print("---------------------------------\n")
