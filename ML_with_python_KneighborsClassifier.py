
# coding: utf-8

# 머신러닝의 적용
# https://github.com/rickiepark/introduction_to_ml_with_python/blob/master/01-introduction.ipynb
# 
# 데이터 적재
# -----------

# In[1]:


from sklearn.datasets import load_iris
iris_dataset = load_iris()


# In[5]:


print("iris_dataset의 키: {}".format(iris_dataset.keys()))


# In[15]:


print(iris_dataset['DESCR'][:193] + "\n...") 
#이게 무슨 뜻인지를 알아야 언어를 돌리지 


# In[14]:


#print("데이터의 크기: {}".format(iris_dataset['data'].shape))
#print("데이터의 타입: {}".format(type(iris_dataset['data'])))
#print("특성의 이름: {}".format(iris_dataset['feature_names']))
#print("타깃의 이름: {}".format(iris_dataset['target_names']))
#print("데이터의 처음 다섯행: Wn{}".format(iris_dataset['data'][:5]))

#print("타겟의 타입: {}".format(type(iris_dataset['target'])))
#print("타겟의 크기: {}".format(iris_dataset['target'].shape))
print("타깃:\n{}".format(iris_dataset['target']))


# 성과측정: 훈련 데이터와 테스트 데이터
# ------------------------------------

# In[23]:


#코드의 의미 이해하기 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)


# In[24]:


print("X_train의 크기: {}".format(X_train.shape))
print("y_train의 크기: {}".format(y_train.shape))


# In[25]:


print("y_test의 크기: {}".format(X_test.shape))
print("y_test의 크기: {}".format(y_test.shape))


# In[30]:


#py -m pip install mglearn (windows)
#pip install mglearn (Mac OS X)

#feature_names를 딴 컬럼을 가진 df 만들기
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                          hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)

