import subprocess
import os
# subprocess.call(['ffmpeg', '-i', 'test.mp3',
#                    'file.wav'])
for path, dirs, files in os.walk('source/'):
	# print(files)
	print(path)
	for f in files:
		print(f)
		subprocess.call(['ffmpeg', '-i', path + f,'music/' + f+'.wav'])
# for i in os.listdir(os.getcwd()):
# 	print(i)