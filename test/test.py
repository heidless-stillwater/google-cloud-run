import requests

# esp = requests.post("https://getprediction-tqc5taiqdq-lm.a.run.app", files={'file': open('eight.png', 'rb')})
resp = requests.post("http://localhost:5000/", files={'file': open('three.png', 'rb')})

print(resp.json())
