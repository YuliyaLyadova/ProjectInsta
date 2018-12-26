import vk
import requests
import json


#session = vk.AuthSession(owner_id='6793749', login='+19172142526', password='baran123', scope='wall,account,photos,messages')
session = vk.AuthSession(
        app_id='6793749',
        user_login='+19172142526',
        user_password='baran123',
        scope='wall,account,photos,messages'
        )
vk_api = vk.API(session, v='5.35')

def main():
#https://api.vk.com/method/users.get?user_id=210700286&v=5.52
    group_id=-30666517
    response=requests.get('https://api.vk.com/method/wall.get', params={'owner_id':group_id,'count':2,'offset':0,'v': 5.35})
    print(response.json())


if __name__ == '__main__':
    main()