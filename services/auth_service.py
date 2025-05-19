from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import logging
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL

def get_oauth_session():
    try:
        client = BackendApplicationClient(client_id=CLIENT_ID)
        oauth = OAuth2Session(client=client)
        oauth.fetch_token(token_url=TOKEN_URL, client_secret=CLIENT_SECRET, include_client_id=True)
        return oauth
    except Exception as e:
        logging.error("Error obtaining OAuth2 session: %s", e)
        raise