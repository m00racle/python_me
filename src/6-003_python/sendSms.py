from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC590e0a47a54f74956ad01aab48d3ffa7"
# Your Auth Token from twilio.com/console
auth_token  = "my_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6287838412300", 
    from_="+14159038712",
    body="Hello from Python!")

print(message.sid)
