# AudioViz

Here are the steps you would need to take to create the visualization:
1)	Place the .mp3 songs you would want to visualize in the source folder
2)	On the terminal run the command ‘python convert.py’ to convert the mp3 files into .wav files. The generated .wav files are placed in the music folder
3)	On the terminal run the command ‘python parse.py’ to parse the .wav files in the music folder to create a feature set data.csv
4)	On the terminal run the command ‘python analyze.py’ to run KMeans on the dataset that was created by parsing the .wav files
5)	On the terminal run the command ‘python visualize.py’ to create visual.json, a file that is used to render the visualization
6)	On the terminal run the command ‘python  -m SimpleHTTPServer’ and go to ‘localhost:8000’ on the Google Chrome browser to view the visualization

