import requests

data = requests.post("http://localhost:5279",
                     json={"method": "resolve", "params": {"urls": ["@jouninreact"]}}).json()

print(data)
>