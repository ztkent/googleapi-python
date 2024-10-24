# GoogleAPI-Python
Simplify python interactions with the [Google Cloud API](https://cloud.google.com/apis/docs/overview).  
This module extends usability of the modern [Google Cloud SDK](https://github.com/googleapis/google-cloud-python).  

Start development for applications that:  
- Fetch [Unread] Gmail messages.
- Fetch [Today's] Calendar events.
- Fetch [Today's] Tasks.

## Setup
- This setup assumes you have permissions to access the Google Cloud API in your workspace.
    - For individuals, you can use your personal Google account.
    - For organizations, you can use a service account.
- Visit the [Google Cloud Console](https://console.cloud.google.com/) to create a new project.
- Select this project, and navigate to the [APIs & Services](https://console.cloud.google.com/apis/dashboard) page.
- Enable any of the following APIs for your project:
    - Gmail API
    - Calendar API
    - Tasks API
- Create a new set of credentials for your project.
    - Navigate to the [API Credentials](https://console.cloud.google.com/apis/credentials) page.
    - Create a new set of OAuth credentials for your project.
        - Select the OAuth 2.0 Client ID option.
        - Select the application type as "Desktop App".
- Save the credentials file as a JSON file. You will need this file to authenticate your application.

### Install GoogleAPI-Python
```bash
pip install git+https://github.com/ztkent/googleapi-python.git
```

### Authorize the application
- When creating a new connection, your application will connect via the [Google Cloud SDK](https://github.com/googleapis/google-cloud-python).
- During the connection flow, the user is redirected to their default web-browser to login.
- After a successful login, an application connection is generated from the response.
- This connection is used for future requests.
```python
async def example_connection(client_id, tenant_id):
    try: 
        google_api = NewGoogleAPI(
            scopes=["mail","calendar"],
            credentials_path='credentials.json')
    except GoogleAuthorizationException as e:
        print(f"{e}")
        return
```