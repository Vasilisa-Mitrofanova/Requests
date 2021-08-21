import requests

token = '2619421814940190'
characters = ['Hulk', 'Captain America', 'Thanos']
characters_dict = {}
for character in characters:
    url = 'https://superheroapi.com/api/' + token + '/search/' + character
    resp = requests.get(url=url)
    characters_dict[resp.json()['results'][0]['powerstats']['intelligence']] = character
sorted_keys = sorted(characters_dict.keys())
print(f'Самый умный супергерой - {characters_dict[sorted_keys[0]]}')