"""
requests documentation:
    https://requests.kennethreitz.org/en/master/

HTTP basics:
    https://www.w3schools.com/tags/ref_httpmethods.asp

HTTP tutorials:
    https://www.youtube.com/watch?v=ng2o98k983k&t=3s
    https://realpython.com/python-requests/

Webscraping:
    BeautifulSoup, requests
"""
import requests
from requests.exceptions import HTTPError
import pprint

pp = pprint.PrettyPrinter(indent=4)

urls = ["https://api.github.com", "https://api.github.com/invalid"]
urls = ["https://api.github.com/search/repositories"]

for url in urls:
    try:
        # params can be dictionary as well as a list of tuples
        # params are key-value pairs in url query string
        # most likely, need to pass auth as well.
        response = requests.get(
            url,
            params={"q": "requests+language:python"},
            headers={"Accept": "application/vnd.github.v3.text-match+json"},
            timeout=0.001,
        )
        # If the response was successful, no Exception will be raised
        response.raise_for_status()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
    except Exception as err:
        print(f"Other error occurred: {err}")  # Python 3.6
    else:
        # print(dir(response))
        json_response = response.json()  # load the content as json
        # print(json_response.keys())

        # print(response.content) # contents in bytes
        # response.encoding = "utf-8"  # Optional: requests infers this internally
        # print(response.text) # contents after decoding.
        # print(response.headers)
        # print(response.url)

        print(json_response["items"][0].keys())


"""
Other HTTP requests methods:
    requests.post('https://httpbin.org/post', data={'key':'value'})
    requests.put('https://httpbin.org/put', data={'key':'value'})
    requests.delete('https://httpbin.org/delete')
    requests.head('https://httpbin.org/get')
    requests.patch('https://httpbin.org/patch', data={'key':'value'})
    requests.options('https://httpbin.org/get')

    data takes a dictionary, a list of tuples, bytes, or a file-like object in POST/PUT/PATCH method.
    if the data is a json, can use json argument as well, e.g.
        requests.post('https://httpbin.org/post', json={'key':'value'})
"""
