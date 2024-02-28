class GoogleAPIException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message="An error occurred in the Google API"):
        self.message = message
        super().__init__(self.message)

class GoogleAuthorizationException(Exception):
    """Exception raised when failing to connect to the Google API."""
    def __init__(self, message="Failed to connect to the Google API"):
        self.message = message
        super().__init__(self.message)

class GoogleRequestException(Exception):
    """Exception raised when a Google API request fails."""
    def __init__(self, message="Google API request failed"):
        self.message = message
        super().__init__(self.message)