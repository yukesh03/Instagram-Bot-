from instabot import Bot

# Creating bot variable.
bot = Bot()

# Login using bot
bot. login (username="Your_username",
password="Your_password")

# Make a list of followers/friends
user_ids = ["username1", "username2", "..... "]

# Message
text = "I like GFG"

# Sending messages
bot. send_messages (text, user _ids)
