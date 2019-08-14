import requests
import json
account_number = input("Enter the account number to request:")

# url = 'https://api.temenos.com/api/v1.0.0/holdings/PSD2/accounts/' + account_number
url = 'https://api.temenos.com/api/v1.0.0/holdings/portfolios/' + account_number +'/positions'
headers = {'Accept': 'application/json', 'apikey': 'PUT_YOUR_KEY_HERE'}
response = requests.get(url, headers=headers)
jData = json.loads(response.content)
if '404' in str(jData):
    print(jData) 
else:
    print(json.dumps(jData, sort_keys=True, indent=4, separators=(', ', ': ')))
