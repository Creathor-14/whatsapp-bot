from fastapi import FastAPI, Request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
import logging

app = FastAPI()

# Configura el logger
logging.basicConfig(level=logging.INFO)

# Obtén las credenciales desde las variables de entorno
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

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

