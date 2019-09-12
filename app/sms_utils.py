import logging
import os

from twilio.rest import Client

logger = logging.getLogger(__name__)


class MessageClient:
    """
    x = MessageClient()
    - The number must be verified for this
    x.send_message('dfds', '+256785372391')
    """

    def __init__(self):
        logger.debug('Initializing messaging client')

        (
            twilio_number,
            twilio_account_sid,
            twilio_auth_token,
        ) = load_twilio_config()
        self.twilio_number = twilio_number
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)

        logger.debug('Twilio client initialized')

    def send_message(self, body, to):
        try:
            self.twilio_client.messages.create(
                body=body,
                to=to,
                from_=self.twilio_number,
            )
        except Exception:
            pass

def load_twilio_config():
    logger.debug('Loading Twilio configuration')

    twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')

    return (twilio_number, twilio_account_sid, twilio_auth_token)
