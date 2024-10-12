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
    # Registro de las credenciales (sin mostrar el Auth Token por seguridad)
    logging.info(f"TWILIO_ACCOUNT_SID: {TWILIO_ACCOUNT_SID}")
    logging.info("Recibiendo mensaje...")

    data = await request.form()
    message_body = data.get("Body").lower()  # Mensaje de WhatsApp
    logging.info(f"Mensaje recibido: {message_body}")

    # Lógica para el chatbot
    if "hola" in message_body:
        response_msg = "Hi! How can I help you today?"
    else:
        response_msg = "Sorry, I didn't understand that."

    # Twilio MessagingResponse
    response = MessagingResponse()
    response.message(response_msg)

    # Registro de la respuesta que se enviará
    logging.info(f"Respuesta enviada: {response_msg}")

    return str(response)
