import requests
import sys
import time
import os


HOST = "http://localhost:5279"


def get_claim_id():
    """
    Input: url
    Output: Claim ID of the resolved claim.
    """
    print("Resolving channel...", end="", flush=True)
    response = requests.post(HOST,
                             json={"method": "resolve",
                                   "params": {
                                       "urls": "lbry://@JouninReact#d"
                                   }}).json()
    claim = [response["result"][key] for key in response["result"]][0]
    try:

        claim_id = claim["claim_id"]
    except:
        print("channel not found. Exiting.")
        sys.exit(-1)
    print(f"done.\nThe claim_id is {claim_id}.", flush=True)
    return claim_id


def get_streams(claim_id, limit=None):
    print("Searching for publications...", end="", flush=True)
    response = requests.post(HOST,
                             json={"method": "claim_search",
                                   "params": {
                                       "channel_ids": [claim_id],
                                       "order_by": "release_time",
                                   }}).json()
    num = response["result"]["total_items"]
    pages = response["result"]["total_pages"]
    print(f"There are {num} files in this channel.", flush=True)

    # Loop over page, get canonical urls of the streams, and sd hashes
    urls = []
    sd_hashes = []
    for page in range(1, pages+1):
        print(f"\rProcessing page {page}/{pages}.", flush=True, end="")
        response = requests.post(HOST,
                                 json={"method": "claim_search",
                                       "params": {"page": page,
                                                  "channel_ids": [claim_id],
                                                  "order_by": "release_time"}}).json()

        urls += [item["canonical_url"] for item in response["result"]["items"]
                 if item["value_type"] == "stream"]

        sd_hashes += [item["value"]["source"]["sd_hash"]
                      for item in response["result"]["items"]
                      if item["value_type"] == "stream"]

        if limit is not None and len(urls) >= limit:
            urls = urls[0:limit]
            sd_hashes = sd_hashes[0:limit]
            break

    print("")

    print(urls)

    return [urls, sd_hashes]


claim_id = 'd23a0b118dba233ec4767b309a449820f781b748'
get_streams(claim_id, limit=None)
