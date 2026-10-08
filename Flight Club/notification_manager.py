import os
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class NotificationManager:
    def __init__(self) -> None:
        # Create a Twilio client only if an SMS or WhatsApp message is requested.
        self._client = None

    def _twilio_client(self):
        if self._client is None:
            account_sid = os.getenv("TWILIO_SID")
            auth_token = os.getenv("TWILIO_AUTH_TOKEN")
            if not account_sid or not auth_token:
                raise ValueError("TWILIO_SID and TWILIO_AUTH_TOKEN must be set to send SMS.")
            self._client = Client(account_sid, auth_token)
        return self._client

    def send_sms(self, message_body):
        sender = os.getenv("TWILIO_VIRTUAL_NUMBER") or os.getenv("TWILIO_FROM_NUMBER")
        recipient = os.getenv("TWILIO_VERIFIED_NUMBER") or os.getenv("TWILIO_TO_NUMBER")
        if not sender or not recipient:
            raise ValueError("Configure a Twilio sender and verified recipient number.")

        message = self._twilio_client().messages.create(
            from_=sender,
            body=message_body,
            to=recipient,
        )
        print(message.sid)
        return message

    def send_email(self, recipient, subject, message_body):
        """Send a flight notification through the repository Gmail account."""
        sender = os.getenv("GMAIL_ADDRESS")
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        if not sender or not app_password:
            raise ValueError(
                "GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set in the repository .env file."
            )
        if not recipient or "@" not in recipient:
            raise ValueError("A valid recipient email address is required.")

        email = EmailMessage()
        email["From"] = sender
        email["To"] = recipient
        email["Subject"] = subject
        email.set_content(message_body)

        try:
            with smtplib.SMTP("smtp.gmail.com", port=587, timeout=30) as connection:
                connection.starttls(context=ssl.create_default_context())
                connection.login(user=sender, password=app_password)
                connection.send_message(email)
        except (OSError, smtplib.SMTPException):
            raise RuntimeError(f"Could not send the flight notification to {recipient}.") from None

    # Join the Twilio WhatsApp Sandbox before using its WhatsApp sender.
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        sender = os.getenv("TWILIO_WHATSAPP_NUMBER")
        recipient = os.getenv("TWILIO_VERIFIED_NUMBER") or os.getenv("TWILIO_TO_NUMBER")
        if not sender or not recipient:
            raise ValueError(
                "TWILIO_WHATSAPP_NUMBER and a verified recipient number must be configured."
            )

        message = self._twilio_client().messages.create(
            from_=f"whatsapp:{sender}",
            body=message_body,
            to=f"whatsapp:{recipient}",
        )
        print(message.sid)
        return message
