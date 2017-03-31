import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
users = ["shinzie", "djcaution", "getrichdieyoung"]

for submission in reddit.redditor('shinzie').submissions.new(limit=1):
    print(submission.title)
    submission.reply("Nice comment, bro. Here's an upvote. - DanBot")
    # comment.reply("Nice comment, bro. Here's an upvote. - DanBot")
    # comment.upvote()
    # print("Bot replying to:", comment)
