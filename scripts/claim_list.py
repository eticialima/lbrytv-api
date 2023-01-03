import requests

data = requests.post("http://localhost:5279", json={
    "method": "claim_list",
    "params": {
        "claim_type": [],
        "claim_id": 'd23a0b118dba233ec4767b309a449820f781b748',
        "name": [],
        "is_spent": False,
        "channel_id": [],
        "has_source": False,
        "has_no_source": False,
        "resolve": False,
        "no_totals": False,
        "include_received_tips": False
    }}).json()

result = data['result']['items']

response = [el['address'] for el in result]

print(len(response))

print(result, "\n")
