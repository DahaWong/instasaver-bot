import urllib
# import urlparse
import oauth2 as oauth
import json

consumer_key="5ffaa85c5d8f405987adf4b41822472f"
consumer_secret="79b6290c1db44b0b8c024c0731753cd8"
access_token_url = 'https://www.instapaper.com/api/1/oauth/access_token'
verify_url = 'https://www.instapaper.com/api/1/account/verify_credentials'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
client.add_credentials("dahawong@gmail.com","cqmyg1ysdss2228")
client.authorizations

params = {}
params["x_auth_username"] = "dahawong@gmail.com"
params["x_auth_password"] = "cqmyg1ysdss2228"
params["x_auth_mode"] = 'client_auth'

client.set_signature_method = oauth.SignatureMethod_HMAC_SHA1()
res, token = client.request(access_token_url, method="POST",body=urllib.parse.urlencode(params))

print (res)
access_token = dict(urllib.parse.parse_qsl(token))

print (access_token)

access_token = oauth.Token(access_token[b'oauth_token'], access_token[b'oauth_token_secret']) 
client = oauth.Client(consumer, access_token)
res, user_data = client.request(verify_url, method="POST")
user_data = json.loads(user_data)

print (user_data)