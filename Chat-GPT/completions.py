"""
This API allows us to correct the spellin mistakes.
"""
import requests
import helper

EDITS = "completions"

POST_DATA ={
"model": "text-davinci-003",
"prompt": "Say this is a test",
# "instruction": "Fix the spelling mistakes"
}

response = requests.post(helper.BASE_URL + EDITS,
              headers=helper.HEADER,
              json=POST_DATA,
              timeout=30)

print(response.json())
