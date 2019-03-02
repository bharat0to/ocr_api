import unittest
import requests
URL = 'http://127.0.0.4:5000/scan'

class APITest(unittest.TestCase):
    def test_scan(self):
        resp = requests.post(URL, json={"data": "base64Data"})
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()