#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
tokenizer = Tokenizer(num_words=10000)


# In[ ]:


with open('word_index.pickle', 'rb') as handle:
    word_index = pickle.load(handle)


# In[ ]:


def rumourdetect(msg):
 msg = msg.lower().split(' ')
 test_seq = np.array([word_index[word] for word in msg])
 test_seq = np.pad(test_seq, (189-len(test_seq), 0),
 'constant', constant_values=(0))
 test_seq = test_seq.reshape(1, 189)
 model = load_model("spammodel.h5")
 pred = model.predict_classes(test_seq)
 print("pred = " + str(pred[0]))
 if pred == [0]:
    return 0
 elif pred == [1]:
     return 1
 else:
    return 2


# In[ ]:
    


# In[ ]:




