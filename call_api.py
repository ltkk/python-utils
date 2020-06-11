import requests
from urllib.parse import urlencode, quote_plus

# Call POST API
def post(data, url, method, timeout=3):
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "6a410524-a8e2-79c7-bd9d-53e4b68c84c7"
    }
    data = urlencode(data, quote_via=quote_plus)
    response = requests.request(method, url, data=data, headers=headers, timeout=timeout)
    return response
    
    
