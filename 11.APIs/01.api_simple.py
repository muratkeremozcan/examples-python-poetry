import requests

API_KEY = 'reqres-free-v1'
HEADERS = {'x-api-key': API_KEY}
BASE = 'https://reqres.in/api/users'

# CREATE
new_user = {'name': 'murat', 'job': 'tester'}
resp = requests.post(BASE, json=new_user, headers=HEADERS)
print('POST →', resp.status_code, resp.json())

# READ (single)
resp = requests.get(f'{BASE}/2', headers=HEADERS)
print('GET 2 →', resp.status_code, resp.json())

# READ (list/page) (public endpoint)
resp = requests.get(BASE, params={'page': 2})
print('GET page 2 →', resp.status_code, resp.json())

# UPDATE (full replace)
update_user = {'name': 'murat ozcan', 'job': 'senior tester'}
resp = requests.put(f'{BASE}/2', json=update_user, headers=HEADERS)
print('PUT 2 →', resp.status_code, resp.json())

# UPDATE (partial)
patch_user = {'job': 'lead tester'}
resp = requests.patch(f'{BASE}/2', json=patch_user, headers=HEADERS)
print('PATCH 2 →', resp.status_code, resp.json())

# DELETE
resp = requests.delete(f'{BASE}/2', headers=HEADERS)
print('DELETE 2 →', resp.status_code)  # should be 204 No Content


######
# In modern REST-style APIs you’ll almost always want to use JSON, but you can also send raw data
# Using `data=` will send application/x-www-form-urlencoded by default
resp = requests.post(BASE, data=new_user, headers=HEADERS)
# Let’s inspect what actually went out
print('Request headers →', resp.request.headers) # application/x-www-form-urlencoded
print('Request body    →', resp.request.body) # name=murat&job=tester
print('Response status →', resp.status_code) # 201
print('Response body   →', resp.text) # {"name":"murat","job":"tester","id":"608","createdAt":"2025-07-14T13:47:56.914Z"}