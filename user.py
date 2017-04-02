import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
users = ["shinzie", "djcaution", "getrichdieyoung"]

for username in users:
    for submission in reddit.redditor(username).submissions.new(limit=1):
        print(submission.title)
        submission.reply("Nice post, bro. Here's an upvote. - DanBot")
        # comment.reply("Nice comment, bro. Here's an upvote. - DanBot")
        # comment.upvote()
        # print("Bot replying to:", comment)
