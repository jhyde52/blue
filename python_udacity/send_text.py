from twilio.rest import TwilioRestClient

#Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC847e78fecc6f53b004d4d23e49ef4a5f"
auth_token = "5ed404d9b21660e7163e3c841a1cca92"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body="Remember how a few days ago we drove past Twilio and I said what's that? :) -Jess",
	to="+17062185630",
	from_="+16502002995")
print message.sid


#brad was an object or instance of turtle
#brad=turtle.Turtle()