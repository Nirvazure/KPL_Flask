import urllib.request
import json
import os
class Spider:

    def __init__(self):
        pass

    def getHeros(self)->list:
        heros = []

        url = "http://pvp.qq.com/web201605/js/herolist.json"

        v_herolist_url = urllib.request.urlopen(url)
        v_herolist = v_herolist_url.read().decode('utf-8')
        v_hero = v_herolist.encode('utf8')[3:].decode('utf-8')
        heros = json.loads(v_hero)
        return heros
