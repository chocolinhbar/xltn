import os

import librosa
import numpy as np
from keras.utils import to_categorical

def load_audio(file_path):
	audio_file, sr = librosa.core.load(file_path, sr=22050)
	return audio_file

def get_audio_piece(audio, set_length, sr):
	set_length *= sr

	if len(audio) > set_length:
		max_start_point = len(audio) - set_length
		start_point = np.random.randint(max_start_point)
		audio_piece = audio[start_point : start_point + set_length]
	elif len(audio) < set_length:
		audio_piece = np.pad(audio, pad_width=(0, set_length - len(audio)), mode='constant', constant_values=0)
	else:
		audio_piece = audio

	return audio_piece

def process_audio(audio_file):
	audio_mfcc = librosa.feature.mfcc(audio_file, sr=22050, n_mfcc=20)
	return audio_mfcc

def get_all_filepaths(data_folder, genre_list):
	filepaths = []
	for subdir in os.listdir(data_folder):
		if subdir not in genre_list:
			continue
		for subsubdir in os.listdir(os.path.join(data_folder,subdir)):
			filepaths.append(os.path.join(data_folder,subdir,subsubdir))

	return filepaths

def getX(filepaths):
	X = []
	for f in filepaths[:500]:
		x = load_audio(f)
		x = get_audio_piece(x, 5, 22050)
		x = process_audio(x)
		X.append(x)

	return np.array(X)
	# return X

genre_list = ["metal", "classical", "blues", "hiphop", "reggae"]
# paths = get_all_filepaths('genres/', genre_list)
# X = getX(paths)
# np.save('extracted',X)

# y = [genre_list.index(genre) for genre in genre_list]

y = []
for g in genre_list:
	y += [genre_list.index(g)] * 100
y_onehot = to_categorical(y)
np.save('labels', y_onehot)