from shutil import rmtree
from pathlib import Path
import requests
import wget
def vk():
    access_token = 'ENTER YOUR VK_TOKEN'
    url = f'https://api.vk.com/method/board.getComments?group_id=158830121&topic_id=37235959&access_token={access_token}&v=5.1999'
    response = requests.get(url)
    mass = response.json()['response']['items'][response.json()['response']['count']-1]
    if "заочного" in mass['text']:
        mass = response.json()['response']['items'][response.json()['response']['count']-2]
        if "заочного" in mass['text']:
            mass = response.json()['response']['items'][response.json()['response']['count']-3]
    result = []
    len_obj = len(mass['attachments'])

    for path in Path('/pdf').glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()

    for i in range(0, len_obj):
        url = mass['attachments'][i]['doc']['url']
        wget.download(url, f'../pdf/pdf_v2{i}.pdf')
        result.append({'title':mass['attachments'][i]['doc']['title'], 'url':mass['attachments'][i]['doc']['url'], 'name':f'../pdf/pdf_v2{i}.pdf'})
    return result

