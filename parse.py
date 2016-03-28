import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')

import os
import pandas as pd
import argparse
from lib import munge
from tinytag import TinyTag


# Command-line argument for choosing the music folder
parser = argparse.ArgumentParser()
parser.add_argument('folder', metavar='folder', type=str,
					help='Folder containing .wav files.')
args = parser.parse_args()

data = {}

for path, dirs, files in os.walk('music/'):
	for f in files:
		# print(path)
		# print(files)
		# Check that the file is a WAV fil
		if f.endswith('.wav'):
			name = ''.join(f.split('.wav')[-2])
			tag = TinyTag.get(path + name + '.wav')
			print(tag.artist)
			# Get the name of the WAV file
			
			# Extract the features from the WAV file
			data[name] = munge.features(path + name)
# for path, dirs, files in os.walk('source/'):
# 	for f in files:
# 		# print(path)
# 		# print(files)
# 		# Check that the file is a WAV fil
# 		if f.endswith('.mp3'):
# 			name = ''.join(f.split('.mp3')[-2])
# 			tag = TinyTag.get(path + name + '.mp3')
# 			print(tag.artist)
			# Get the name of the WAV file
			
			# Extract the features from the WAV file

df = pd.DataFrame.from_dict(data, orient='index')
df.columns = next(iter(data.values())).keys()
# print(df)


df.to_csv('data.csv')
