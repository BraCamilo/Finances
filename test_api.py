import urllib.request
import json
import logging

try:
    resp = urllib.request.urlopen('http://127.0.0.1:8000/movimientos')
    data = json.loads(resp.read())
    with open('test_output.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("SUCCESS")
except Exception as e:
    print("FAILED:", e)
