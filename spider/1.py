import urllib.request
import json
import os
import pandas as pd
import numpy as np

v_herolist_url = urllib.request.urlopen(
    "http://pvp.qq.com/web201605/js/herolist.json")
v_herolist = v_herolist_url.read().decode('utf-8')
v_hero = v_herolist.encode('utf8')[3:].decode('utf-8')
hero_json = json.loads(v_hero)
print(type(hero_json))

df = pd.DataFrame(hero_json)
df = df[['cname', 'ename', 'hero_type']]

a=np.array(df)
print(df[df['hero_type'] == 6])


cards: [
    {
        title: "干将莫邪",
        src:
        "https://game.gtimg.cn/images/yxzj/img201606/heroimg/182/182.jpg",
        flex: 3,
        color: "purple",
        rank: 5
    },
    {
        title: "庄周",
        src:
        "https://game.gtimg.cn/images/yxzj/img201606/heroimg/113/113.jpg",
        flex: 3,
        color: "teal lighten-1",
        rank: 2
    },
    {
        title: "鲁班七号",
        src:
        "https://game.gtimg.cn/images/yxzj/img201606/heroimg/112/112.jpg",
        flex: 3,
        color: "amber darken-3",
        rank: 3
    },
    {
        title: "嬴政",
        src:
        "https://game.gtimg.cn/images/yxzj/img201606/heroimg/110/110.jpg",
        flex: 3,
        color: "grey darken-1",
        rank: 4
    }
]

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
        {'a': 2, 'b': 4, 'c': 6, 'd': 48, 'e': 5}]
hero = {}
hero['a'] = 5
hero['b'] = 10
hero['c'] = 5
hero['d'] = 10
hero['e'] = 5
data.append(hero)
data.append({'a': 3, 'b': 6, 'c': 9, 'd': 8, 'e': 5})

json = json.dumps(data)
print(json)
