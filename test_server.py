import requests

data = {'mail': '12123', 'password': '123123'}
for i in range(1200):

    requests.post(url='http://127.0.0.1:5000/api/add-mail', json={'mail':str(i),'password':'123'})
