import urllib.request
import json
import os
import pandas as pd

v_herolist_url = urllib.request.urlopen(
    "http://pvp.qq.com/web201605/js/herolist.json")
v_herolist = v_herolist_url.read().decode('utf-8')
v_hero = v_herolist.encode('utf8')[3:].decode('utf-8')
hero_json = json.loads(v_hero)
print(type(hero_json))

df = pd.DataFrame(hero_json)
df = df[['cname', 'ename', 'hero_type']]


print(df[df['hero_type'] == 6])
