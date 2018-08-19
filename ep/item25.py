import threading
import requests
import time

def get_response(url):
    r = requests.get(url)
    return r.status_code, r.text

class RequestThread(threading.Thread):

    def __init__(self, url):
        super(RequestThread, self).__init__()
        self._url = url

    def run(self):
        self.output = get_response(self._url)

start = time.time()
urls = ['https://www.google.com',
        'https://www.facebook.com',
        'https://www.apple.com',
        'https://www.netflix.com',
        'https://www.salesforce.com',
        'https://www.intuit.com',
        'https://www.amazon.com',
        'https://www.uber.com',
        'https://www.lyft.com']

threads = []
for url in urls:
    thread = RequestThread(url)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print( "Time taken: %.3f" % (end-start))