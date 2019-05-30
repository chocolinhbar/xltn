import os

import librosa
import numpy as np
from keras.utils import to_categorical

def load_audio(file_path):
	audio, sr = librosa.core.load(file_path, sr=22050)
	return audio

def create_more_audio(audio, set_length, sr, hop_size):
	set_length *= sr
	hop_size *= sr
	audio_pieces = []

	if len(audio) <= set_length:
		audio_pieces = [np.pad(audio, pad_width=(0, set_length - len(audio)), mode='constant', constant_values=0)]
	else:
		max_start_point = len(audio) - set_length
		for s in range(0, max_start_point + 1, hop_size):
			audio_pieces.append(audio[s : s + set_length])

	return audio_pieces

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

def process_audio(audio):
	audio_mfcc = librosa.feature.mfcc(audio, sr=22050, n_mfcc=40)
	return audio_mfcc

def get_all_filepaths(data_folder, genre_list):
	filepaths = []
	for subdir in os.listdir(data_folder):
		if subdir not in genre_list:
			continue
		for subsubdir in os.listdir(os.path.join(data_folder,subdir)):
			filepaths.append(os.path.join(data_folder,subdir,subsubdir))

	return filepaths

def get_X_and_y(filepaths):
	X = []
	y = []

	for f in filepaths[:500]:
		x = load_audio(f)
		x_arr = create_more_audio(x, 5, 22050, 2)
		p = os.path.dirname(f)
		label = os.path.split(p)[-1]
		label_i = genre_list.index(label)
		for x in x_arr:
			x = process_audio(x)
			X.append(x)
			y.append(label_i)

	return np.array(X), y
	# return X

genre_list = ["metal", "classical", "blues", "hiphop", "reggae"]

if __name__ == '__main__':
	
	paths = get_all_filepaths('genres/', genre_list)
	X, y = get_X_and_y(paths)
	np.save('extracted', X)

	# y = [genre_list.index(genre) for genre in genre_list]

	y_onehot = to_categorical(y)
	np.save('labels', y_onehot)