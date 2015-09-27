__author__ = 'Eric Huynh'
__copyright__ = "Copyright 2015, Lightwave"
__version__ = "0.0.1"
__email__ = "eric.huynh@lightwave.io"
__status__ = "Development"

import requests
import json

root_url = 'https://api.lightwave.io'
db_url = '/v0/IP6_BEACON_20'
startkey_url = '?startKey=1443189600000'
# endkey_url = '&endKey=1443221742194'
endkey_url = ''
limit_url = '&limit=1000'
lw_login = 'hacking-art'
lw_pass = '4l1ghtwav3'

# Initial request
initial_request = root_url + db_url + startkey_url + endkey_url + limit_url
response = requests.get(initial_request, auth=(lw_login, lw_pass))
print('Initial request url is:', initial_request)
response_dict = json.loads(response.text)

next_page = response_dict.get('next', None)
count = response_dict.get('count')
results = response_dict.get('results')
values = [result.get('value') for result in results]

total_count = count

print('Total items retrieved:', total_count, end=' ')
print('and next page is:', next_page)

# Follow pagination if any
while next_page is not None:
    response = requests.get(root_url + next_page, auth=(lw_login, lw_pass))
    response_dict = json.loads(response.text)
    next_page = response_dict.get('next', None)
    count = response_dict.get('count')
    results = response_dict.get('results')
    values += [result.get('value') for result in results]
    total_count += count
    print('Total items retrieved:', total_count, end=' ')
    print('and next page is:', next_page)

# You have now a dictionnary with all the items
print('Final extracted List has', len(values), 'objects retrieved')

with open('file1.json', 'w') as f:
    json.dump(results,f)

