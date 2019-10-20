"""
https://requests.kennethreitz.org/en/master/user/advanced/#advanced

The Session object allows you to persist certain parameters across requests. 
It also persists cookies across all requests made from the Session instance, 
and will use urllib3’s connection pooling. 
So if you’re making several requests to the same host, 
the underlying TCP connection will be reused,
which can result in a significant performance increase (see HTTP persistent connection).
"""
import requests


s = requests.Session()

s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("https://httpbin.org/cookies")

# or session as context manager
with requests.Session() as s:
    s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
