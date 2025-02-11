import requests
import os
import wget
def vk():
    access_token = '0236de0a0236de0a0236de0a44011e16a5002360236de0a65976f3262964096e5f289e9'
    url = f'https://api.vk.com/method/board.getComments?group_id=158830121&topic_id=37235959&access_token={access_token}&v=5.1999'
    response = requests.get(url)
    mass = response.json()['response']['items'][response.json()['response']['count']-1]
    if "заочного" in mass['text']:
        mass = response.json()['response']['items'][response.json()['response']['count']-2]
        if "заочного" in mass['text']:
            mass = response.json()['response']['items'][response.json()['response']['count']-3]
    result = []
    len_obj = len(mass['attachments'])
    for path in os.listdir('../pdf'):
        os.unlink("../pdf/" + path)
    for i in range(0, len_obj):
        url = mass['attachments'][i]['doc']['url']
        wget.download(url, f'../pdf/pdf_v2{i}.pdf')
        result.append({'title':mass['attachments'][i]['doc']['title'], 'url':mass['attachments'][i]['doc']['url'], 'name':f'../pdf/pdf_v2{i}.pdf'})

    return result

