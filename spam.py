
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

df=pd.read_csv("SPAM text message 20170820 - Data.csv")
df.head(10)

def classes(category):
        if(category=='ham'):
            return 1
        else:
           return 0


df['Category']=df['Category'].apply(classes)

df.tail(10)

df.isnull().sum()

df.describe()

df.dtypes

messages=np.asarray(df['Message'])

messages

classes=np.asarray(df['Category'])
classes

from tensorflow.keras.preprocessing.text import Tokenizer

final=[]

def total(messages):
    for i in messages:
        final.append(messages)  
    
df['Message'].nunique()

tokenizer = Tokenizer(num_words=10000)#keep 10000 most frequent classes,ignore the others
tokenizer.fit_on_texts(messages)
sequences = tokenizer.texts_to_sequences(messages)

sequences[0]

len(sequences)

len(sequences[0])

len(sequences[100])

max=0

for i in sequences:
    h=len(i)
    if(h>max):
        max=h
        
print('Maximum sequence length in the list of sequences:', max)

from tensorflow.keras.preprocessing.sequence import pad_sequences

word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=189)

data

X=data

X.shape

Y=df['Category']

import tensorflow.keras.utils as ku

Y=ku.to_categorical(Y)

Y

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,SimpleRNN,LSTM

model = Sequential()
model.add(Embedding(input_dim=10000,output_dim=32,input_length=189))
model.add(SimpleRNN(units=32))
model.add(Dense(2, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy',
 metrics=['acc'])
model.summary()

batch_size = 60
model.fit(X_train, Y_train, epochs = 10, batch_size=batch_size, validation_split=0.2)

acc = model.evaluate(X_test,Y_test)
print("Test loss is {0:.2f} accuracy is {1:.2f} ".format(acc[0],acc[1]))

def message_to_array(msg):
 msg = msg.lower().split(' ')
 test_seq = np.array([word_index[word] for word in msg])
 test_seq = np.pad(test_seq, (189-len(test_seq), 0),
 'constant', constant_values=(0))
 test_seq = test_seq.reshape(1, 189)
 return test_seq

custom_msg = input("Enter the message - ")
test_seq = message_to_array(custom_msg)
pred = model.predict_classes(test_seq)
print(pred)


