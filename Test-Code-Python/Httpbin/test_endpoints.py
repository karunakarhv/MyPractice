import pytest
from BaseApi import BaseApi
from Endpoints import HTTPBinMethods

class TestHTTPBinMethods:
    @pytest.fixture(scope="class")
    def httpbin_methods(self):
        return HTTPBinMethods()

    def test_get_endpoint(self, httpbin_methods):
        assert httpbin_methods.get().status_code == 200

    def test_post_endpoint(self, httpbin_methods):
        assert httpbin_methods.post().status_code == 200

    def test_put_endpoint(self, httpbin_methods):
        assert httpbin_methods.put().status_code == 200

    def test_delete_endpoint(self, httpbin_methods):
        assert httpbin_methods.delete().status_code == 200
        
