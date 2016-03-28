import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pprint
import os
import json
import copy 

with open('data.json') as data_file:    
    data = json.load(data_file)
viz_dict = {}
viz_dict['name'] = 'My Songs'
viz_dict['children'] = []
temp_children = []
for i in range(1,9):
	new_cluster = {}
	new_cluster['name'] = 'Cluster ' + str(i).zfill(2)
	new_cluster['children'] = []
	temp_children.append(new_cluster)
viz_dict['children'] = temp_children
final_dict = copy.deepcopy(viz_dict)
for key, value in data.iteritems():
	cluster_name = 'Cluster ' + value['cluster']
	list_index = next(index for (index, d) in enumerate(viz_dict['children']) if d["name"] == cluster_name)
	find_index = -1
	for i, v in enumerate(viz_dict['children']):
		if v['name'] == str(cluster_name):
			find_index = i
			break
	temp_song = {}
	temp_song = value
	temp_song['name'] = value['title']
	temp_song['size'] = 10
	viz_dict['children'][find_index]['children'].append(temp_song)
copy_songs = {} # by cluster

for key, value in enumerate(viz_dict['children']):
	curr_cluster = key + 1
	cluser_name = value['name']
	curr_songs = copy.deepcopy(value['children'])
	copy_songs[cluser_name] = curr_songs

for key, value in copy_songs.iteritems():
	# curr_cluster = key + 1
	cluser_name = key
	# curr_songs = copy.deepcopy(value['children'])
	by_artist_temp = {}
	by_artist_temp['name'] = 'Artists'
	by_artist_temp['children'] = []

	for i, v in enumerate(value):
		found = False
		for i1, v1 in enumerate(by_artist_temp['children']):
			if v['artist'] in v1['name']:
				found = True
		if found is False:
			temp_artist = {}
			temp_artist['name'] = v['artist']
			temp_artist['children'] = []
			by_artist_temp['children'].append(temp_artist)
	for i, v in enumerate(value):
		for i1, v1 in enumerate(by_artist_temp['children']):
			if v['artist'] in v1['name']:
				v1['children'].append(v)
	find_index = -1
	for i, v in enumerate(final_dict['children']):
		if v['name'] is key:
			find_index = i
			break;

	final_dict['children'][i]['children'].append(by_artist_temp)

for key, value in copy_songs.iteritems():
	# curr_cluster = key + 1
	cluser_name = key
	# curr_songs = copy.deepcopy(value['children'])
	by_artist_temp = {}
	by_artist_temp['name'] = 'Genre'
	by_artist_temp['children'] = []

	for i, v in enumerate(value):
		found = False
		for i1, v1 in enumerate(by_artist_temp['children']):
			if v['genre'] in v1['name']:
				found = True
		if found is False:
			temp_artist = {}
			temp_artist['name'] = v['genre']
			temp_artist['children'] = []
			by_artist_temp['children'].append(temp_artist)
	for i, v in enumerate(value):
		for i1, v1 in enumerate(by_artist_temp['children']):
			if v['genre'] in v1['name']:
				v1['children'].append(v)
	find_index = -1
	for i, v in enumerate(final_dict['children']):
		if v['name'] is key:
			find_index = i
			break;

	final_dict['children'][i]['children'].append(by_artist_temp)

with open('visual.json', 'w') as outfile:
    json.dump(final_dict, outfile)










