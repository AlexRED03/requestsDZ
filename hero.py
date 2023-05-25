from pprint import pprint

import requests
import json

def test1():
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
 
    response = requests.get(url)
    return response.json()

def powerstats(id):
    url = f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/{id}.json"
    response = requests.get(url)
    return response.json()




if __name__ == '__main__':
    hero = ("Hulk", "Captain America", "Thanos")
    f = test1()
    f1 = powerstats(1)
    f2 = {}
    # c1 = f["name"]
    for c in f:
        if c["name"] in hero:
            f1 = powerstats(c['id'])
            f2[c["name"]] = f1['intelligence']
    f3 = max(f2.values())
    for a,b in f2.items():
        if b == f3:
            print(a)
   