import urllib.request
import os

categories = {
    'https://pitstop.rv.ua/s/catalog?Parent=(1d6f5bec-d49c-11e4-8586-002590aa75d3)': 'tires_discs_chains',
    'https://pitstop.rv.ua/s/catalog?Parent=(a5aa1e6f-d49b-11e4-8586-002590aa75d3)': 'accessories'
}

for category in categories:
    with urllib.request.urlopen(category) as response:
        file_name = categories[category] + '.json'
        file = open('resources' + os.sep + file_name, 'w', encoding='utf-8')
        file.write(response.read().decode())