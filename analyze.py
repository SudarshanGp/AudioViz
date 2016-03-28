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

from sklearn import datasets, decomposition, svm, neighbors, cluster

from tinytag import TinyTag


plt.style.use('ggplot')

data = pd.read_csv('data.csv', index_col=0)
data = data.fillna(0)
pca = PCA(n_components=31).fit_transform(data.values)
kmeans = cluster.KMeans(n_clusters=8)
data1 = kmeans.fit_predict(pca)
index = 0
mapping = {}
for key, value in data.iterrows():
	cluster_val = data1[index]
	if cluster_val in mapping.keys():
		mapping[cluster_val].append(key)
	else:
		temp_list = []
		temp_list.append(key)
		mapping[cluster_val] = temp_list
	index += 1

pprint.pprint(mapping)

song_information = {}

for path, dirs, files in os.walk('source/'):
	for f in files:
		if f.endswith('.mp3'):
			temp_dict = {}
			name = ''.join(f.split('.mp3')[-2])
			tag = TinyTag.get(path + name + '.mp3')
			for key, value in mapping.iteritems():
				for i, v in enumerate(value):
					if name + '.mp3' in v:
						print("old key", key)
						temp_dict['cluster'] = str(key+1).zfill(2) 
						print("new key", str(key+1).zfill(2) )
						print(key)
			temp_dict['title'] = tag.title.encode('ascii','ignore')
			if tag.genre is None:
				temp_dict['genre'] = 'Other'
			else:
				temp_dict['genre'] = tag.genre.encode('ascii','ignore')
			temp_dict['album'] = tag.album.encode('ascii','ignore')
			temp_dict['artist'] = tag.artist.encode('ascii','ignore')
			song_information[tag.title.encode('ascii','ignore')] = temp_dict

pprint.pprint(song_information)
print(type(song_information))
with open('data.json', 'w') as outfile:
    json.dump(song_information, outfile)
