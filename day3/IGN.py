from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.data_utils import to_categorical, pad_sequences, VocabularyProcessor

from sklearn.cross_validation import train_test_split


import pandas as pd
import numpy as np

data = pd.read_csv('ign.csv')
data = data[['score_phrase', 'title']]
data.fillna(value='', inplace=True)
totalX = data.title
totalY = data.score_phrase

vocab_proc = VocabularyProcessor(15)
totalX = np.array(list(vocab_proc.fit_transform(totalX)))

vocab_proc2 = VocabularyProcessor(1)
totalY = np.array(list(vocab_proc2.fit_transform(totalY))) - 1
totalY = to_categorical(totalY, nb_classes=11)

print(totalX)
print(totalY)

trainX, testX, trainY, testY = train_test_split(totalX, totalY, test_size=0.1)

# Neural Network Building
net = tflearn.input_data([None, 15])
net = tflearn.embedding(net, input_dim=10000, output_dim=128)
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 11, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001, loss='categorical_crossentropy')

# Training
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True, batch_size=32)