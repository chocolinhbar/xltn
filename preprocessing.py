#genres\metal\metal.00000.au
import librosa
import numpy as np
#import IPython.display
#from IPython.display import Audio #as ipd
#from playsound import playsound
#import matplotlib.pyplot as plt
#import librosa.display

#import sklearn

import os
#import pathlib
#audio_path = 'genres\metal\metal.00000.au'

#audio_path = (librosa.util.example_audio_file())

# Load the signal
#x, sr = librosa.load('genres\metal\metal.00000.au')

#IPython.display.Audio(data=x, rate=sr)

#playsound(audio_path)
#print('done')

"""
# Plot the signal
plt.figure(figsize=(14,5))
librosa.display.waveplot(x, sr=sr)

# Zooming in
n0 = 9000
n1 = 9100
plt.figure(figsize=(14,5))
plt.plot(x[n0:n1])
plt.grid()

plt.show()
"""

"""
# Feature 1
# Count the zero crossings
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings))
"""

"""
# Feature 2
# Compute the spectral centroid
spectral_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
#spectral_centroid.shape()
# librosa.feature.spectral_centroid computes the spectral centroid for each
# frame in a signal

# Compute the time variable for visualisation
frames = range(len(spectral_centroid))
t = librosa.frames_to_time(frames)

# Normalise the spectral centroid for visualisation
def normalise(x, axis=0):
	return sklearn.preprocessing.minmax_scale(x, axis=axis)

# Plot the spectral centroid along the waveform
librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalise(spectral_centroid), color='r')
plt.show()
"""

"""
# Feature 3
# Compute the rolloff frequency for each frame in a signal
spectral_rolloff = librosa.feature.spectral_rolloff(x+0.01, sr=sr)[0]
librosa.display.waveplot(x, sr=sr, alpha=0.4)
plt.plot(t, normalise(spectral_rolloff), color='r')
plt.show()
"""

"""
# Feature 4
# MFCC - a small set of features which concisely describe the overall shape
# of a spectral envelop
mfccs = librosa.feature.mfcc(x, sr=sr)
#librosa.display.specshow(mfccs, sr=sr, x_axis='time')
#plt.show()

# Feature scaling - zero mean and unit variance (chuẩn tắc?)
mfccs = sklearn.preprocessing.scale(mfccs, axis=1)
librosa.display.specshow(mfccs, sr=sr, x_axis='time')
plt.show()
"""

"""
# Feature 5
# Chroma frequencies
hop_length = 512
chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
plt.figure(figsize=(15,5))
librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')
plt.show()
"""

"""
cmap = plt.get_cmap('inferno')

plt.figure(figsize=(10,10))
genres = 'metal classical blues hiphop reggae'.split()

for g in genres:
	pathlib.Path(f'img_data/{g}').mkdir(parents=True, exist_ok=True)
	for filename in os.listdir(f'./genres/{g}'):
		songname = f'./genres/{g}/{filename}'
		y, sr = librosa.load(songname, mono=True, duration=5)
		#plot a spectrogram, parameters' explanation's in the documentation
		plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=cmap, sides='default', mode='default', scale='dB')
		plt.axis('off') #turn off all axis and their values --> less confusing to get data from figure
		plt.savefig(f'img_data/{g}/{filename[:-3].replace(".", "")}.png') #safe current figure, delete 3 0's and replace the midde dot with nothing
		plt.clf() #clear current figure
"""

"""
def read_audio(file_path):
	audio = librosa.core.load(file_path, sr=22050, res_type='kaiser_best')
	return audio

def process_audio(audio):
	audio_mfcc = librosa.feature.mfcc(audio, sr=22050, n_mfcc=20)
	return audio_mfcc
"""

### Pre-process
def load_audio(file_path):
	audio_file, sr = librosa.core.load(file_path, sr=22050)
	return audio_file

def process_audio(audio_file):
	audio_mfcc = librosa.feature.mfcc(audio_file, sr=22050, n_mfcc=20)
	return audio_mfcc

def get_all_filepaths(data_folder):
	filepaths = []
	for subdir in os.listdir(data_folder):
		if subdir not in ["metal", "classical", "blues", "hiphop", "reggae"]:
			continue
		for subsubdir in os.listdir(os.path.join(data_folder,subdir)):
			filepaths.append(os.path.join(data_folder,subdir,subsubdir))
	return filepaths

def getX(filepaths):
	X = []
	for f in filepaths[:100]:
		x = load_audio(f)
		y = process_audio(x)
		X.append(y)
	return np.array(X)

paths = get_all_filepaths('genres')
X = getX(paths)
np.save('extracted',X)