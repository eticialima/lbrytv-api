import requests
from datetime import datetime

data = requests.post("http://localhost:5279", json={
    "method": "claim_search",
    "params": {
        "claim_ids": [],
        "channel": "@Jouninreact",
        "channel_ids": [],
        "not_channel_ids": [],
        "has_channel_signature": False,
        "valid_channel_signature": False,
        "invalid_channel_signature": False,
        "is_controlling": False,
        "stream_types": [],
        "media_types": [],
        "any_tags": [],
        "all_tags": [],
        "not_tags": [],
        "any_languages": [],
        "all_languages": [],
        "not_languages": [],
        "any_locations": [],
        "all_locations": [],
        "not_locations": [],
        "order_by": "release_time",
        "no_totals": False,
        "include_purchase_receipt": False,
        "include_is_my_output": False,
        "remove_duplicates": False,
        "has_source": False,
        "has_no_source": False,
        "page": 1,
        "page_size": 50,
        "total_items": 2000,
        "total_pages": 1
    }}).json()
result = data['result']['items']


# print(result)
print(data['result']['page'], "\n")
print(data['result']['page_size'], "\n")
print(data['result']['total_items'], "\n")
print(data['result']['total_pages'], "\n")

response = [el['address'] for el in result]

print("Quantidade de itens:", len(response))

title = [el['value']['title'] for el in result]

data_create = [datetime.fromtimestamp(
    el['timestamp']).strftime('%d/%m/%y') for el in result]

print(title)

search = 'VMZ'

b = filter(lambda k: search in k, title)

print(list(b))
