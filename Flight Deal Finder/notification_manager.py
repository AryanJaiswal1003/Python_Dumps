import os
import re
from pathlib import Path

from dotenv import load_dotenv
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

# Find the repository-level .env file even when this script is run from another folder.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")


class NotificationManager:
    """Send flight alerts through Twilio SMS or the WhatsApp Sandbox."""

    def __init__(self) -> None:
        # The Account SID and Auth Token authenticate the Twilio REST client.
        account_sid = self._required_setting("TWILIO_SID")
        auth_token = self._required_setting("TWILIO_AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)

    @staticmethod
    def _required_setting(name: str, *aliases: str) -> str:
        # Accept both the descriptive names and the earlier project .env names.
        for setting_name in (name, *aliases):
            value = os.getenv(setting_name)
            if value:
                return value.strip()

        accepted_names = ", ".join((name, *aliases))
        raise ValueError(
            f"{accepted_names} is missing. Add one of these settings to the "
            "repository .env file or configure it as an environment variable."
        )

    @staticmethod
    def _validate_phone_number(value: str, setting_name: str) -> str:
        # Twilio expects international phone numbers in E.164 format, including "+".
        if not re.fullmatch(r"\+[1-9]\d{7,14}", value):
            raise ValueError(
                f"{setting_name} must be an E.164 phone number, such as +14155550123."
            )
        return value

    def send_sms(self, message_body: str, trial_template: bool = True):
        # Trial sender and verified recipient are configured separately in the .env file.
        sender = self._validate_phone_number(
            self._required_setting("TWILIO_VIRTUAL_NUMBER", "TWILIO_FROM_NUMBER"),
            "TWILIO_VIRTUAL_NUMBER",
        )
        recipient = self._validate_phone_number(
            self._required_setting("TWILIO_VERIFIED_NUMBER", "TWILIO_TO_NUMBER"),
            "TWILIO_VERIFIED_NUMBER",
        )
        # Trial accounts accept named templates only; paid accounts can send the full alert.
        body = "sms_internal_alerts" if trial_template else message_body
        if trial_template:
            print("Twilio trial mode sends a generic SMS template, not the custom flight details.")
        try:
            message = self.client.messages.create(
                body=body,
                from_=sender,
                to=recipient,
            )
        except TwilioRestException as error:
            # Explain Twilio's trial restriction rather than showing an opaque SDK traceback.
            if "invalid template name" in str(error).lower():
                raise RuntimeError(
                    "Twilio trial accounts only allow predefined SMS templates, "
                    "so this custom flight alert cannot be sent on the trial. "
                    "Use one of Twilio's supported template names "
                    "(for example, sms_internal_alerts), or upgrade the account "
                    "to send custom flight details."
                ) from error
            raise
        print(message.sid)
        return message

    # Join the Twilio WhatsApp Sandbox before using its WhatsApp sender.
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body: str):
        # WhatsApp addresses require a "whatsapp:" prefix on both sender and recipient.
        sender = self._validate_phone_number(
            self._required_setting("TWILIO_WHATSAPP_NUMBER"),
            "TWILIO_WHATSAPP_NUMBER",
        )
        recipient = self._validate_phone_number(
            self._required_setting("TWILIO_VERIFIED_NUMBER", "TWILIO_TO_NUMBER"),
            "TWILIO_VERIFIED_NUMBER",
        )
        message = self.client.messages.create(
            body=message_body,
            from_=f"whatsapp:{sender}",
            to=f"whatsapp:{recipient}",
        )
        print(message.sid)
        return message
