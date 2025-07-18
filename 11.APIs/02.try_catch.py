# in Python, the errors are not built-in like in JS, we need to import them from requests.exceptions
# we have to enable HTTPErrors with .raise_for_status()
from requests.exceptions import ConnectionError, HTTPError
import requests

url ="http://wronghost:3000/albums"
try: 
    r = requests.get(url) 
    r.raise_for_status()  # Enable raising errors for all error status_codes
    print(r.status_code)
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')


####
# 
while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
    
    # Add your fix here
    time.sleep(3)

print('The longest track in my music library is: ' + longestTrackTitle)		