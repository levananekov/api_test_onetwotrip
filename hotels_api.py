import requests

host = 'https://www.onetwotrip.com/_hotels/api/suggestRequest'

def get_hotels_info(city):
    req_params = {'query': city}
    response = requests.get(host, params=req_params)
    return response

