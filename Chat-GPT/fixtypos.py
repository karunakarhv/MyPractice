"""
This API allows us to correct the spellin mistakes.
"""
import requests
import helper

EDITS = "edits"

POST_DATA ={
"model": "text-davinci-edit-001",
"input": "What day it is today?",
"instruction": "Fix the spelling mistakes"
}

response = requests.post(helper.BASE_URL + EDITS,
              headers=helper.HEADER,
              json=POST_DATA,
              timeout=30)

print(response.json())
