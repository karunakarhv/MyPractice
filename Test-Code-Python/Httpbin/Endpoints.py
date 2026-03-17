
from BaseApi import BaseApi
import requests

class HTTPBinMethods(BaseApi):
    
    def sendMethods(self, endpoint):
        # Map end point to the corresponding HTTP method
        method_map = {
            "get": requests.get,
            "post": requests.post,
            "put": requests.put,
            "delete": requests.delete
        }
        http_method = method_map.get(endpoint)
        if not http_method:
            raise ValueError(f"Unsupported endpoint: {endpoint}")

        try:
            response = http_method(f"{self.base_url}/{endpoint}")
            response.raise_for_status()  # Check if the request was successful
        except requests.RequestException as e:
            print(f"Error occurred while making {endpoint} request: {e}")
            raise
        return response
    
    def get(self):
        return self.sendMethods("get")

    def post(self):
        return self.sendMethods("post")

    def put(self):
        return self.sendMethods("put")

    def delete(self):
        return self.sendMethods("delete")

class HTTPBinAuthMethods(BaseApi):
    def basic_auth(self, username, password):
        return requests.get(f"{self.base_url}/basic-auth/{username}/{password}", auth=(username, password))
    def bearer(self, token):
        return requests.get(f"{self.base_url}/bearer", headers={"Authorization": f"Bearer {token}"})
    def hidden_basic_auth(self, username, password):
        return requests.get(f"{self.base_url}/hidden-basic-auth/{username}/{password}", auth=(username, password))