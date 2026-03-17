# import yaml
from openapi_parser import parse

# def test_openapi_spec():
#     with open('openapi.yaml', 'r') as f:
#         spec = yml.safe_load(f)
    
#     # Check that the OpenAPI version is correct
#     assert spec['openapi'] == '3.0.0'
    
#     # Check that the info section is present
#     assert 'info' in spec
#     assert 'title' in spec['info']
#     assert 'version' in spec['info']
    
#     # Check that the paths section is present
#     assert 'paths' in spec

def test_openapi_spec_1():
    # Parse from a file path
    specification = parse('open_api.yml')
    print(specification.)
    # Accessing Info
    assert specification.info.title == "Hello World API"
    assert specification.info.version == "1.0.0"
    assert specification.info.description == "A simple API that returns a greeting"
    
    for path in specification.paths:
        print(f"Path: {path}")
        for operation in path.operations:
            print(f"    Summary: {operation.summary}")
            print(f"    Description: {operation.description}")
            print(f"    Operation ID: {operation.operation_id}")
            print(f"    Parameters: {operation.parameters}")
            print(f"    Request Body: {operation.request_body}")
            print(f"    Responses: {operation.responses}")
            for response in operation.responses:
                print(f"        Status Code: {response.code}")
                print(f"        Description: {response.description}")
                print(f"        Content: {response.content}")
                for content in response.content:
                    print(f"            Media Type: {content.type}")
                    print(f"            Schema: {content.schema}")

if __name__ == "__main__":
    test_openapi_spec_1()
    print("All tests passed!")