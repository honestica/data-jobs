import requests
import uuid

from lib.communication_generator import sample_communication

ENDPOINT = "http://127.0.0.1:5000"

for _ in range(1000):
  try:
    requests.post(ENDPOINT,json={
      'communication': sample_communication(uuid.uuid4())
    })
  except requests.ConnectionError:
    print(f'Connection refused on {ENDPOINT}')