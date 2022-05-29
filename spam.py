#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os


# In[2]:


df=pd.read_csv("SPAM text message 20170820 - Data.csv")
df.head(10)


# In[3]:


def classes(category):
        if(category=='ham'):
            return 1
        else:
           return 0


# In[4]:


df['Category']=df['Category'].apply(classes)


# In[5]:


df.tail(10)


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[8]:


df.dtypes


# In[9]:


messages=np.asarray(df['Message'])


# In[10]:


messages


# In[11]:


classes=np.asarray(df['Category'])
classes


# In[13]:


from tensorflow.keras.preprocessing.text import Tokenizer


# In[14]:


final=[]


# In[16]:


def total(messages):
    for i in messages:
        final.append(messages)  
    


# In[17]:


df['Message'].nunique()


# In[18]:


tokenizer = Tokenizer(num_words=10000)#keep 10000 most frequent classes,ignore the others
tokenizer.fit_on_texts(messages)
sequences = tokenizer.texts_to_sequences(messages)


# In[19]:


sequences[0]


# In[20]:


len(sequences)


# In[21]:


len(sequences[0])


# In[22]:


len(sequences[100])


# In[23]:


max=0


# In[24]:


for i in sequences:
    h=len(i)
    if(h>max):
        max=h


# In[25]:


print('Maximum sequence length in the list of sequences:', max)


# In[26]:


from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[27]:


word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=189)


# In[28]:


data


# In[29]:


X=data


# In[30]:


X.shape


# In[31]:


Y=df['Category']


# In[33]:


import tensorflow.keras.utils as ku


# In[34]:


Y=ku.to_categorical(Y)


# In[35]:


Y


# In[36]:


from sklearn.model_selection import train_test_split


# In[37]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)


# In[39]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding,SimpleRNN,LSTM


# In[40]:


model = Sequential()
model.add(Embedding(input_dim=10000,output_dim=32,input_length=189))
model.add(SimpleRNN(units=32))
model.add(Dense(2, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy',
 metrics=['acc'])
model.summary()


# In[41]:


batch_size = 60
model.fit(X_train, Y_train, epochs = 10, batch_size=batch_size, validation_split=0.2)


# In[42]:


acc = model.evaluate(X_test,Y_test)
print("Test loss is {0:.2f} accuracy is {1:.2f} ".format(acc[0],acc[1]))


# In[43]:


def message_to_array(msg):
 msg = msg.lower().split(' ')
 test_seq = np.array([word_index[word] for word in msg])
 test_seq = np.pad(test_seq, (189-len(test_seq), 0),
 'constant', constant_values=(0))
 test_seq = test_seq.reshape(1, 189)
 return test_seq


# In[ ]:


custom_msg = input("Enter the message - ")
test_seq = message_to_array(custom_msg)
pred = model.predict_classes(test_seq)
print(pred)


# In[ ]:




