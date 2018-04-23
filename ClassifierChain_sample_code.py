
# coding: utf-8

# In[19]:


#https://tensorflow.blog/2018/02/16/%EB%B6%84%EB%A5%98%EA%B8%B0-%EC%B2%B4%EC%9D%B8-classifierchain/
#https://github.com/rickiepark/introduction_to_ml_with_python/blob/master/ClassifierChain.ipynb

import numpy as np
import pandas as pd 
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split

yeast = fetch_mldata('yeast')

X = yeast['data'] #x 설정  
Y = yeast['target'] #y 설정 

Y = Y.transpose().toarray() #y의 행과 열을 바꾸어 정렬한다 
                            # toarray() N-dimensional array를 numpy array로 바꾼다  #http://scidb-py.readthedocs.io/en/stable/access.html

#훈련 데이터와 테스트 데이터 분리 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, 
                                                    random_state=42)
#train_test_split: http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html


# In[20]:


#로지스틱 회귀 
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

ovr = OneVsRestClassifier(LogisticRegression())
ovr.fit(X_train, Y_train)
pred_ovr = ovr.predict(X_test)


# In[5]:


from sklearn.metrics import jaccard_similarity_score
ovr_score = jaccard_similarity_score(Y_test, pred_ovr)
ovr_score


# In[6]:


from sklearn.multioutput import ClassifierChain

cc = ClassifierChain(LogisticRegression(), order='random', random_state=42)
cc.fit(X_train, Y_train)
pred_cc = cc.predict(X_test)
cc_score = jaccard_similarity_score(Y_test, pred_cc)
cc_score


# In[7]:


chains = [ClassifierChain(LogisticRegression(), order='random', random_state=42+i)
          for i in range(10)]
for chain in chains:
    chain.fit(X_train, Y_train)

pred_chains = np.array([chain.predict(X_test) for chain in chains])
chain_scores = [jaccard_similarity_score(Y_test, pred_chain)
                    for pred_chain in pred_chains]


# In[8]:


proba_chains = np.array([chain.predict_proba(X_test) for chain in chains])
proba_ensemble = proba_chains.mean(axis=0)
ensemble_score = jaccard_similarity_score(Y_test, proba_ensemble >= 0.5)

