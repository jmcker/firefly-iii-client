# firefly_iii_client.DataApi

All URIs are relative to *https://demo.firefly-iii.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**destroy_data**](DataApi.md#destroy_data) | **DELETE** /api/v1/data/destroy | Endpoint to destroy user data


# **destroy_data**
> destroy_data(objects)

Endpoint to destroy user data

A call to this endpoint permanently destroys the requested data type. Use it with care and always with user permission. The demo user is incapable of using this endpoint. 

### Example

* OAuth Authentication (firefly_iii_auth):
```python
from __future__ import print_function
import time
import firefly_iii_client
from firefly_iii_client.rest import ApiException
from pprint import pprint
configuration = firefly_iii_client.Configuration()
# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://demo.firefly-iii.org
configuration.host = "https://demo.firefly-iii.org"
# Create an instance of the API class
api_instance = firefly_iii_client.DataApi(firefly_iii_client.ApiClient(configuration))
objects = firefly_iii_client.DataDestroyObject() # DataDestroyObject | The type of data that you wish to destroy.

try:
    # Endpoint to destroy user data
    api_instance.destroy_data(objects)
except ApiException as e:
    print("Exception when calling DataApi->destroy_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **objects** | [**DataDestroyObject**](.md)| The type of data that you wish to destroy. | 

### Return type

void (empty response body)

### Authorization

[firefly_iii_auth](../README.md#firefly_iii_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response when data has been destroyed. |  -  |
**500** | Internal error, or user is unauthorized to destroy data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

