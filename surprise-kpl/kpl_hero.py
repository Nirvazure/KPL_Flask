import os
import io

from surprise import Dataset
from surprise import Reader
from surprise import KNNBaseline


def read_user_names():
    file_name = 'u.user'
    rid_to_name = {}
    name_to_rid = {}
    with io.open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[2]
            name_to_rid[line[2]] = line[0]
    return rid_to_name, name_to_rid


def read_item_names():
    """Read the u.item file from MovieLens 100-k dataset and return two
    mappings to convert raw ids into movie names and movie names into raw ids.
    """

    file_name = 'u.item'
    rid_to_name = {}
    name_to_rid = {}
    with io.open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
            name_to_rid[line[1]] = line[0]

    return rid_to_name, name_to_rid


# path to dataset folder
file_path = 'u.data'

# This time, we'll use the built-in reader.

reader = Reader(line_format='user item rating', sep='\t')

data = Dataset.load_from_file(file_path, reader=reader)
print(data.raw_ratings)
# for urid, irid, r, timestamp in raw_trainset:
trainset = data.build_full_trainset()
sim_options = {'name': 'pearson_baseline', 'user_based': False}
algo = KNNBaseline(sim_options=sim_options)
algo.fit(trainset)


# Read the mappings raw id <-> movie name
rid_to_item, item_to_rid = read_item_names()
print(rid_to_item, item_to_rid)

# Retrieve inner id of the movie Toy Story
toy_story_raw_id = item_to_rid['公孙离']
toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)

# Retrieve inner ids of the nearest neighbors of Toy Story.
toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=3)

# Convert inner ids of the neighbors into names.
toy_story_neighbors = (algo.trainset.to_raw_iid(inner_id)
                       for inner_id in toy_story_neighbors)
toy_story_neighbors = (rid_to_item[rid]
                       for rid in toy_story_neighbors)

rid_to_user, user_to_rid = read_user_names()
print(rid_to_user, user_to_rid)

tar_raw_id = user_to_rid['Nirvazure']
tar_inner_id = algo.trainset.to_inner_iid(tar_raw_id)
tar_neighbors = algo.get_neighbors(tar_inner_id, k=1)
tar_neighbors = (algo.trainset.to_raw_iid(inner_id)
                 for inner_id in tar_neighbors)
tar_neighbors = (rid_to_user[rid]for rid in tar_neighbors)

print()
print('The 1 nearest neighbors of Nirvauzre are:')
for movie in tar_neighbors:
    print(movie)
