import requests

url = "http://localhost:8000/start-attack"
data = {
  "ip": "ip-addres-server",
  "port": port-server,
  "protocol": 754,
  "method": "botjoiner",
  "seconds": 30,
  "target_cps": 10000,
  "api_key": "your_secret_api_key"
}

response = requests.post(url, json=data)
print(response.json)
