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

with open('data.json') as data_file:    
    data = json.load(data_file)
pprint.pprint(data)
viz_dict = {}
viz_dict['name'] = 'My Songs'
viz_dict['children'] = []
temp_children = []
for i in range(1,11):
	new_cluster = {}
	new_cluster['name'] = 'Cluster ' + str(i)
	new_cluster['children'] = []
	temp_children.append(new_cluster)
viz_dict['children'] = temp_children
# pprint.pprint(viz_dict)

for key, value in data.iteritems():
	print(key)
	cluster_name = 'Cluster ' + str(int(value['cluster'])+1)
	list_index = next(index for (index, d) in enumerate(viz_dict['children']) if d["name"] == cluster_name)
	temp_song = {}
	temp_song = value
	temp_song['name'] = value['title']
	temp_song['size'] = 10
	viz_dict['children'][list_index]['children'].append(temp_song)

pprint.pprint(viz_dict)



with open('flare1.json', 'w') as outfile:
    json.dump(viz_dict, outfile)
	# print(value)












