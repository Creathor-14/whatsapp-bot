from fastapi import FastAPI, Request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

# Twilio credentials (retrieved from your Twilio dashboard)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.post("/whatsapp")
async def whatsapp_bot(request: Request):
    data = await request.form()
    message_body = data.get("Body").lower()  # WhatsApp message

    # Logic for the chatbot
    if "hello" in message_body:
        response_msg = "Hi! How can I help you today?"
    else:
        response_msg = "Sorry, I didn't understand that."

    # Twilio MessagingResponse
    response = MessagingResponse()
    response.message(response_msg)

    return str(response)
