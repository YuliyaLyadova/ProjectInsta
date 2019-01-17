import vk
import requests
import json


#session = vk.AuthSession(owner_id='6793749', login='+19172142526', password='baran123', scope='wall,account,photos,messages')
session = vk.Session(
        access_token='d2f5660e65e69324e0658cb78d2065a2d1c55b2a54d2528924f9285c68002a5b2bc0d4c6d6d3046420eaf'
        )
vk_api = vk.API(session, v='5.74')

def main():
#https://api.vk.com/method/users.get?user_id=210700286&v=5.52
    group_id=-30666517
    response=requests.get('https://api.vk.com/method/wall.get', params={'owner_id':group_id,'count':2,'offset':0,'v': 5.74})
    print(response.json())


if __name__ == '__main__':
    main()