#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold


# In[2]:


dataframe = pd.read_csv("diabetes.csv")
dataframe


# In[3]:


from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

X = dataframe.iloc[:,0:8]
Y = dataframe.iloc[:,8]

kfold = StratifiedKFold(n_splits=10,random_state= 3,shuffle=True)

model = RandomForestClassifier(n_estimators=200,random_state=20,max_depth=None)
results = cross_val_score(model, X, Y, cv=kfold)
print(results)
print(results.mean())



# In[ ]:





# # Hyper parameter tuning using GridSearchCV

# In[ ]:


from sklearn.model_selection import GridSearchCV
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
params = {
    'max_depth': [2,3,5,None],
    'min_samples_leaf': [5,10,20],
    'n_estimators':[50,100,200,500],
    'max_features':["sqrt","log2",None],
    'criterion':["gini","entopy"]  
}
grid_search = GridSearchCV(estimator=rf,
                        param_grid=params,
                        cv = 5,
                        n_jobs=-1, verbose=10, scoring='accuracy')
grid_search.fit(X,Y)


# In[ ]:


print(grid_search.best_params_)
print(grid_search.best_score_)


# In[ ]:


grid_search.best_estimator_


# Feature Selection usiong random forest 

# In[ ]:


model_best = RandomForestClassifier(criterion='entropy', max_depth=5, max_features=None,
                                   min_samples_leaf=5, n_jobs=-1, random_state=42)
model_best.fit(X,Y)
model_best.feature_importances_


# In[ ]:


X = dataframe.iloc[:,0:8]
X.columns


# In[ ]:


df = pd.DataFrame(model_best.feature_importances_, columns = ["Importance score" ],index  = X.columns)
df.sort_values(by = "Importance score", inplace = True, ascending = False,)


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns 
plt.bar(df.index, df["Importance score"])


# In[ ]:




