from twilio.rest import Client

print("Starting call script...")

account_sid = "AC52d11d0bdc70730010aa11a203233655"
auth_token = "d23cc8c08962404079b670c35348cfcc"

client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://conversational-ivr-modernization-nzvv.onrender.com/twilio-webhook",
    to="+919982486999",
    from_="+16184645514"
)

print("Call SID:", call.sid)
print("Call Status:", call.status)