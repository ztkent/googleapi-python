import google_auth_oauthlib.flow
from datetime import datetime, timedelta
from googleapi_python.exceptions import *
from googleapiclient.discovery import build

# Simplify interactions with the Google API.
# This module provides a GoogleAPI class with NewGoogleAPI to initialize the connection.

# The GoogleAPI class provides methods to:
# - Fetch user information. More permissions will provide more information.
# - Fetch [Unread] Emails
# - Fetch [Today's] Calendar events.

def NewGoogleAPI(scopes, credentials_path='credentials.json'):
    """ Create an authenticated Google API connection.
    Args:
    Returns:
        GoogleAPI: The authenticated Google API connection.
    Raises:
        AuthorizationException: If the client fails to authenticate with the Google API.
    """
    selected_scopes = []
    if "mail" in scopes:
       selected_scopes.append('https://www.googleapis.com/auth/gmail.readonly')
    if "calendar" in scopes:
        selected_scopes.append('https://www.googleapis.com/auth/calendar.readonly')
    if len(selected_scopes) == 0:
        raise GoogleAPIException("Invalid authentication scopes. Must be 'mail' or 'calendar'.")

    try:
        creds_client = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials_path, selected_scopes).run_local_server(port=0)
    except Exception as e:
        raise GoogleAuthorizationException(f"Failed to connect to the Google API: {e}")
    return GoogleAPI(creds_client)

class GoogleAPI:
    def __init__(self, creds_client):
        """ Create a new GoogleAPI object.
        Args:
            client: The GoogleAPI client.
        """
        self.creds_client = creds_client
        self.gmail_client = build('gmail', 'v1', credentials=self.creds_client)
        self.calendar_client = build('calendar', 'v3', credentials=self.creds_client)

    def get_gmail_messages(self, label='INBOX'):
        try:
            results = self.gmail_client.users().messages().list(userId='me', labelIds=[label]).execute()
            messages = results.get('messages', [])
            return messages
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_unread_gmail_messages(self, label='INBOX'):
        try:
            results = self.gmail_client.users().messages().list(userId='me', q='is:unread', labelIds=[label]).execute()
            messages = results.get('messages', [])
            return messages
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    
    def get_calendar_events(self):
        try:
            results = self.calendar_client.events().list(calendarId='primary').execute()
            events = results.get('items', [])
            return events
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    
    def get_todays_calendar_events(self):
        try:
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            end = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'
            results = self.calendar_client.events().list(
                calendarId='primary', timeMin=now, timeMax=end, singleEvents=True,
                orderBy='startTime').execute()
            events = results.get('items', [])
            return events
        except Exception as e:
            print(f"An error occurred: {e}")
            return []