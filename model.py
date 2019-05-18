##import sox
##sox -t auto metal.00000.au -e signed-integer metal_00.wav
#
#import sys
#import os
#
## Store all command line args in genre_dirs
#genre_dirs = sys.argv[1:]
#
#for genre_dir in genre_dirs:
	## change directory to genre_dir
	#os.chdir(genre_dir)
#
	## echo contents before altering
	#print('Contents of ' + genre_dir + ' before conversion: ')
	#os.system("ls")
#
	## loop through each file in current dir
	#for file in os.listdir(genre_dir):
		## SOX
		#os.system("sox " + str(file) + " " + str(file[:-3]) + ".wav")
#	
	## delete .au from current dir
	##os.system("rm *.au")
	## echo contents of current dir
	#print('After conversion:')
	#os.system("ls")
	#print('\n')
#
#print("Conversion complete. Check respective directories.")

#import sox

#a = 'metal.00000'
#b = 'metal_00'
#sox a.au b.wav

#import os
#from pydub import AudioSegment
#
#audio_file = AudioSegment.from_file('genres\metal\metal.00000.au')
#audio_file.export(path[:-3]+"wav",format='wav')
#print("done")

from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras import metrics

model = Sequential() #linear stack of layers

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu', input_shape=(20,1293,1)))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(Conv2D(32, (3,3), strides=(1,1), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2,3), strides=(2,3)))

model.add(Flatten())
model.add(Dense(5, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy')