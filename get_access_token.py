from instagram.client import InstagramAPI
import sys

client_id = '923490f7659a44fb8a83db1a4134992f'
client_secret = '58999a8bbb0c42e78213585de310cafe'
# redirect_uri = 'http://192.168.0.82:8515/oauth_callback'
redirect_uri = 'https://192.168.0.82'
raw_scope = input("Requested scope (separated by spaces, blank for just basic read): ").strip()
scope = raw_scope.split(' ')
# For basic, API seems to need to be set explicitly
if not scope or scope == [""]:
    scope = ["basic"]

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope=scope)

print("Visit this page and authorize access in your browser: " + redirect_uri)

code = (str(input("Paste in code in query string after redirect: ").strip()))

access_token = api.exchange_code_for_access_token(code)
print("access token: ")
print(access_token)
