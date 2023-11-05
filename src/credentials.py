from os import environ

class CREDENTIALS:
    apiKey = environ.get('IMMUDB_VALUT_API_KEY') or '<YOUR_SECRET_API_KEY>'
    readOnlyApiKey = environ.get('IMMUDB_VALUT_API_KEY_READONLY') or '<YOUR_SECRET_READ_ONLY_API_KEY>'

