import requests
import pprint

url = "https://api.upbit.com/v1/orderbook"

querystring = {"markets":"KRW-BTC"}

response = requests.request("GET", url, params=querystring)
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(response.text)