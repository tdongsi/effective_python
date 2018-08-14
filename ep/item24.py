import threading
import requests


def get_response(url):
    r = requests.get(url)
    return r.status_code, r.text


class RequestThread(threading.Thread):

    def __init__(self, url):
        super(RequestThread, self).__init__()
        self._url = url

    def run(self):
        self.output = get_response(self._url)


print get_response('https://www.google.com')