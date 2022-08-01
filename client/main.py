import os
import sys

import urllib
import google.auth.transport.requests
import google.oauth2.id_token
from urllib.parse import urlparse, urlunparse


def get_authorized(url):
    u = urlparse(url)
    audience = urlunparse((u.scheme, u.hostname, u.path, None, None, None))

    try:
        response = make_authorized_get_request(url, audience)
        return response

    except Exception as e:
        print(e)
        return str(e)

def make_authorized_get_request(endpoint, audience):
    req = urllib.request.Request(endpoint)

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    req.add_header("Authorization", f"Bearer {id_token}")
    response = urllib.request.urlopen(req)

    return response.read()

if __name__ == '__main__':
    if len(sys.argv) < 1:
        raise SystemExit

    print(get_authorized(sys.argv[1]))
