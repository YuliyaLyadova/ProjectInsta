import vk
import requests
import json



#app_id = '6793749'
access_token_YL = 'd2f5660e65e69324e0658cb78d2065a2d1c55b2a54d2528924f9285c68002a5b2bc0d4c6d6d3046420eaf'
#user_id = 'id482512310'
#servicekey='b2d1408bb2d1408bb2d1408b7db2b6ea9ebb2d1b2d1408beecf4a4a8e9cec2a2c2cc89e'
 



def main():
    group_id=-30666517
    #https://api.vk.com/method/wall.get?user_id=210700286&v=5.84
    r=requests.get('https://api.vk.com/method/wall.get&access_token=access_token_YL&v=5.92', params={'owner_id':group_id,'count':2,'offset':0})
    print(r.json())

if __name__ == '__main__':
    main()