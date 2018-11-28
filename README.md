# Installation
TBD
# Usage
## Creating a client instance
```python
from q2_api_client.client import Q2APIClient

client = Q2APIClient(host="secure.fi.com", username="username", password="P@ssw0rd")
``` 
Options that can be set when creating a client instance:

* `scheme`: The URI scheme that will be used. If no scheme is specified, `https` will be used.
* `host`: The hostname for the server.
* `base_path`: The base path for the server.
* `port`: The port that the API server uses to allow connections.
* `username`: The account username used to authenticate with the service.
* `password`: The account password used to authenticate with the service.
* `connect_timeout`: The amount of time (in seconds) that the client will wait when making calls to the server before timing out. If no value is provided, the timeout is set to **60** seconds.
* `read_timeout`: The amount of time (in seconds) that the client will wait when receiving a response from the server before timing out. If no value is provided, the timeout is set to **120** seconds.
* `query_parameters`: The query parameters that will be used throughout the session. This should only be set in special cases.
* `headers`: The headers that will be used throughout the session. This should only be set in special cases.
* `fragment`: The URL fragment that will be used throughout the session. This should only be set in special cases.

The client will make a `POST` request to the defined server upon instantiation using the provided credentials in order to obtain a Q2 token that will be used for the remainder of the session. If the credentials are not valid or the request was not successful, an exception will be raised.
## Making API calls
After creating a client instance, HTTP calls can be made accordingly. The implemented methods provide a 1-for-1 abstraction of the HTTP calls defined in the Swagger documentation.
```python
q2_config = client.q2_config.get_q2_config()
institution = client.v2.pfm.get_institution(123)
```
The client utilizes the [Requests](https://github.com/requests/requests) library to make API calls to the server.
## Parsing responses
The API calls return a [Response](http://docs.python-requests.org/en/master/api/#requests.Response) object. For example, given the following API call:
```python
response = client.v2.banking.get_banking_groups()
```
The response can then be parsed accordingly.
```python
response_status_code = response.status_code
response_url = response.url
response_headers = response.headers
response_body = response.text
```
If the response body is in JSON format, the response body can be loaded to a `dict`.
```python
json_response_body = response.json()
```
The response object also includes a [PreparedRequest](http://docs.python-requests.org/en/master/api/#requests.PreparedRequest) object which includes information about the HTTP request that was made and can also be parsed:
```python
request_method = response.request.method
request_url = response.request.url
request_body = response.request.body
request_headers = response.request.headers
```
