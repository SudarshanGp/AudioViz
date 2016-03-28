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
# data.replace([np.inf, -np.inf], np.nan)
# print(data['2_differences_1_sample_skewness'])
data = data.fillna(0)
# print(data['2_differences_1_sample_skewness'])

# data = data.replace(r'\s+', 0, regex=True)
# print(data.info())
pca = PCA(n_components=31).fit_transform(data.values)
# print(pca)
kmeans = cluster.KMeans(n_clusters=10)
data1 = kmeans.fit_predict(pca)
# print(data1)	
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
		# print(path)
		# print(files)
		# Check that the file is a WAV fil
		if f.endswith('.mp3'):
			temp_dict = {}
			name = ''.join(f.split('.mp3')[-2])
			tag = TinyTag.get(path + name + '.mp3')
			# print(name + '.mp3')
			for key, value in mapping.iteritems():
				for i, v in enumerate(value):
					if name + '.mp3' in v:
						temp_dict['cluster'] = str(key)
						print(key)
			# print(mapping[name + '.mp3'])
			temp_dict['title'] = tag.title.encode('ascii','ignore')
			if tag.genre is None:
				temp_dict['genre'] = 'None'
			else:
				temp_dict['genre'] = tag.genre.encode('ascii','ignore')
			temp_dict['album'] = tag.album.encode('ascii','ignore')
			temp_dict['artist'] = tag.artist.encode('ascii','ignore')
			song_information[tag.title.encode('ascii','ignore')] = temp_dict

pprint.pprint(song_information)
print(type(song_information))
with open('data.json', 'w') as outfile:
    json.dump(song_information, outfile)
# viz_dict = {}
# viz_dict['name'] = 'My Songs'
# viz_dict['children'] = []
# temp_children = []
# for i in range(1,11):
	
# for key, value in song_information.iteritems():



# kmeans.fit(x_train)
# y = kmeans.predict(x_test)

# x, y = zip(*pca)

# plt.scatter(x, y)
# plt.show()
