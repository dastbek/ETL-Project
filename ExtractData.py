import pandas as pd
import numpy as np
import requests 

CLIENT_ID = 'cc456fd0fcec40dd8a9c9fb039b39ce4'
CLIENT_SECRET = 'fc14921e0b104b76a0b724a1ce9544b4'
scope = 0

# Requesting user Auth

base_url = 'https://accounts.spotify.com/authorize?'
redirect_uri = ''
params = {
    'response_type': 'code',
    'client_id': CLIENT_ID,
    'scope': scope,
    'redirect_uri': redirect_uri,
    'state': 'duyhuynh'
}


