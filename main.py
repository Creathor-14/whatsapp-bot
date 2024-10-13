from fastapi import FastAPI, Request, Form
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse  # Importa PlainTextResponse para enviar respuesta como texto plano


app = FastAPI()

# Middleware para habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las fuentes, ajústalo si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtén las credenciales desde las variables de entorno
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.get("/")  # Endpoint GET para probar la aplicación
async def read_root():
    return {"message": "Hello World"}

@app.post("/whatsapp")
async def whatsapp_bot(request: Request):
    data = await request.form()
    message_body = data.get("Body").lower()  # Mensaje de WhatsApp

    # Lógica del chatbot
    if "hello" in message_body:
        response_msg = "Hi! How can I help you today?"
    else:
        response_msg = "Sorry, I didn't understand that."

    # Twilio MessagingResponse para generar la respuesta en formato TwiML (XML)
    response = MessagingResponse()
    response.message(response_msg)

    # Retorna la respuesta como texto plano (XML) con el Content-Type correcto
    return PlainTextResponse(str(response), media_type="text/xml")