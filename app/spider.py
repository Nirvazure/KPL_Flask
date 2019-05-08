import urllib.request
import json
import os
import pandas as pd
import numpy as np


class Spider:

    def __init__(self):
        pass

    def getHeros(self)->list:
        heros = []
        hero_type = {1: '战士', 2: '法师', 3: '坦克', 4: '刺客', 5: '射手', 6: '辅助', }
        url = "http://pvp.qq.com/web201605/js/herolist.json"

        v_herolist_url = urllib.request.urlopen(url)
        v_herolist = v_herolist_url.read().decode('utf-8')
        v_hero = v_herolist.encode('utf8')[3:].decode('utf-8')
        hero_json = json.loads(v_hero)

        df = pd.DataFrame(hero_json)
        df = df[['cname', 'ename', 'hero_type', 'title']]
        items = np.array(df)

        for item in items:
            hero = {}
            hero['name'] = str(item[0])
            hero['src'] = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + \
                str(item[1])+"/"+str(item[1])+".jpg"
            hero['type'] = hero_type[item[2]]
            hero['title'] = item[3]

            heros.append(hero)

        # heros = json.dumps(heros, ensure_ascii=False)
        # return json
        return heros
