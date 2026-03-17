import requests

url = 'http://google.com/'

response = requests.options(url)
print(f"Response status code: {response.headers}")
if 'Allow' in response.headers:
    allowed_methods = response.headers['Allow']
    print(f"Allowed methods for {url}: {allowed_methods}")
    if 'TRACE' in allowed_methods:
        print("The TRACE method is likely supported.")
    else:
        print("The TRACE method is not listed as allowed.")
else:
    print("The 'Allow' header was not found in the response.")
    
if __name__ == "__main__":
    print("This script checks if the TRACE method is supported by the specified URL.")

