import bottle
import beaker.middleware
from bottle import route, redirect, post, run, request, hook
from instagram import client, subscriptions
from instagram.client import InstagramAPI

CONFIG = {
    'client_id': '923490f7659a44fb8a83db1a4134992f',
    'client_secret': '58999a8bbb0c42e78213585de310cafe',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}
unauthenticated_api = client.InstagramAPI(**CONFIG)


def access_token():
    scope = []
    api = InstagramAPI(client_id=CONFIG['client_id'], client_secret=CONFIG['client_secret'],
                       redirect_uri=CONFIG['redirect_uri'])
    redirect_uri = api.get_authorize_login_url(scope=scope)

    print("Visit this page and authorize access in your browser:\n", redirect_uri)
    code = input("Paste in code in query string after redirect: ").strip()
    access_token = api.exchange_code_for_access_token(code)
    print(access_token)
    return access_token


token = access_token()
api = InstagramAPI(access_token=token, client_secret=CONFIG['client_secret'])
recent_media, next_ = api.user_recent_media(user_id="190353205", count=10)
for media in recent_media:
    print(media.caption.text)
