# Project name: Send Text
# Course: Udacity Full Stack Nanodegree

from twilio import rest

# Your Account info from twilio.com/console
account_sid = "0123ABC"
auth_token  = "9876ZYX"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+15555555", 
    from_="+15555555",
    body="Hello from Python!")

print(message.sid)
