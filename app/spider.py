import urllib.request
import json
import os
from haishoku.haishoku import Haishoku
from webcolors import rgb_to_hex


class Spider:

    def __init__(self):
        pass

    def getHeros(self)->list:
        url = "http://pvp.qq.com/web201605/js/herolist.json"

        v_herolist_url = urllib.request.urlopen(url)
        v_herolist = v_herolist_url.read().decode('utf-8')
        v_hero = v_herolist.encode('utf8').decode('utf-8')
        heros = json.loads(v_hero)
        for hero in heros:
            color = self.getColor(hero['ename'])
            hero['color'] = color
        return heros

    def getColor(self, ename):
        img_url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + \
            str(ename) + "/" + str(ename) + ".jpg"
        haishoku = Haishoku.loadHaishoku(img_url)
        color = rgb_to_hex(haishoku.dominant)
        return color
