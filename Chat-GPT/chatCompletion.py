"""
This API allows us to correct the spellin mistakes.
"""
import requests
import helper

CHATS = "chat/completions"

POST_DATA ={
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": "Resume for Software Engineer for Python Automation Developer"}]
}

response = requests.post(helper.BASE_URL + CHATS,
              headers=helper.HEADER,
              json=POST_DATA,
              timeout=30)

print(response.json())
