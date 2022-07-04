import requests
import sys
import time
import os

def get_claim_id():
        """
        Input: url
        Output: Claim ID of the resolved claim.
        """
        print("Resolving channel...", end="", flush=True)
        response = requests.post("http://localhost:5279", 
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

get_claim_id()