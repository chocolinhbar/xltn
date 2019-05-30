import os

import librosa
import numpy as np
from keras.models import load_model

from preprocessing import load_audio, get_audio_piece, process_audio, genre_list

model = load_model('my_model.linh')

def get_input_audio(file_path):
	audio = load_audio(file_path)
	audios_mfcc = []

	for i in range(3):
		a = get_audio_piece(audio, 5, 22050)
		audio_mfcc = process_audio(a)
		audios_mfcc.append(audio_mfcc)

	audios_mfcc = np.array(audios_mfcc)

	return audios_mfcc[:,:,:,None]

def predict(input_audio, threshold=0.75):
	probs = model.predict(input_audio)
	probs = np.mean(probs, axis=0)
	print(probs)
	prediction = np.argmax(probs)

	if probs[prediction] < threshold:
		genre = 'unknown'
	else:
		genre = genre_list[prediction]

	return genre

if __name__ == '__main__':

	while True:
		input_audio = get_input_audio(input('file path: '))
		genre = predict(input_audio)

		print(genre)