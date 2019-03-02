import unittest
import requests
import time

URL = 'http://localhost:5000/scan'

class PerfTest(unittest.TestCase):
    def test_requests_per_sec(self):
        c = 0
        tic = time.time()
        while True:
            resp = requests.post(URL, json={"data": "base64Data"})
            c += 1
            if time.time() - tic >= 1:
                break
        print("Requests Per Second: ", c)

    # def test_parallel_connections(self):
    #     connections = 0
    #     while True:
    #         resp = requests.post(URL, json={"data": "base64Data"})

if __name__ == '__main__':
    unittest.main()