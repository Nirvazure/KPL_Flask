#-*- coding:utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import os
import io
from surprise import KNNBaseline
from surprise import Dataset

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a， %d %b %Y %H:%M:%S')


# 训练推荐模型 步骤:1
def getSimModle():
    # 默认载入movielens数据集
    data = Dataset.load_builtin('ml-100k')
    trainset = data.build_full_trainset()
    #使用pearson_baseline方式计算相似度  False以item为基准计算相似度 本例为电影之间的相似度
    sim_options = {'name': 'pearson_baseline', 'user_based': False}
    ##使用KNNBaseline算法
    algo = KNNBaseline(sim_options=sim_options)
    #训练模型
    algo.fit(trainset)
    return algo


# 获取id到name的互相映射  步骤:2
def read_item_names():
    """
    获取电影名到电影id 和 电影id到电影名的映射
    """
    file_name = (os.path.expanduser('~') +
                 '/.surprise_data/ml-100k/ml-100k/u.item')
    rid_to_name = {}
    name_to_rid = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
            name_to_rid[line[1]] = line[0]
    return rid_to_name, name_to_rid


# 基于之前训练的模型 进行相关电影的推荐  步骤：3
def getSimilarMovies(algo, rid_to_name, name_to_rid,movie_name,recommand_num):
    # 获得电影Toy Story (1995)的raw_id
    movie_raw_id = name_to_rid[movie_name]
    logging.debug('raw_id=' + movie_raw_id)
    #把电影的raw_id转换为模型的内部id
    movie_inner_id = algo.trainset.to_inner_iid(movie_raw_id)
    logging.debug('inner_id=' + str(movie_inner_id))
    #通过模型获取推荐电影 这里设置的是recommand_num部
    movie_neighbors = algo.get_neighbors(movie_inner_id,recommand_num)
    logging.debug('neighbors_ids=' + str(movie_neighbors))
    #模型内部id转换为实际电影id
    neighbors_raw_ids = [algo.trainset.to_raw_iid(inner_id) for inner_id in movie_neighbors]
    #通过电影id列表 或得电影推荐列表
    neighbors_movies = [rid_to_name[raw_id] for raw_id in neighbors_raw_ids]
    return neighbors_movies

def web_api(movie_name,neighbor_num):
    rid_to_name, name_to_rid = read_item_names()
    algo = getSimModle()
    neighbors_movies=getSimilarMovies(algo, rid_to_name, name_to_rid,movie_name,neighbor_num)
    return neighbors_movies

if __name__ == '__main__':
    #Hyper parameter
    neighbor_num = 15
    movie_name = 'Seven (Se7en) (1995)'
    # 获取id到name的互相映射
    rid_to_name, name_to_rid = read_item_names()
    # 训练推荐模型
    algo = getSimModle()
    ##显示相关电影
    neighbors_movies = getSimilarMovies(algo, rid_to_name, name_to_rid,movie_name,neighbor_num)

    print("=======================Movie Recommand=============================")
    print('The '+str(neighbor_num)+' nearest neighbors of '+movie_name+' are:')
    for movie in neighbors_movies:
        print(movie)