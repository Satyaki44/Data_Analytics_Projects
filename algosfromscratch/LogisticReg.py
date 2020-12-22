#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.0001, n_iters=1000):
        self.lr=0.0001
        self.n_iters=1000
        self.weights=None
        self.bias=None
        
    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.weights=np.zeros(n_features)
        self.bias=0
        
        #gradient_descent
        for _ in range(self.n_iters):
        #sigmoid_function
            y_pred=1/(1+np.exp(-np.dot(X,self.weights)-self.bias))
        
            dw=(1/n_samples)*np.dot(X.T,(y-y_pred))
            db=(1/n_samples)*np.sum(y-y_pred)
        
            self.weights-=self.lr*dw
            self.bias-=self.lr*db
        
    def predict(self,X):
        y_pred=1/(1+np.exp(-np.dot(X,self.weights)-self.bias))
        y_pred_class=[1 if i > 0.5 else 0 for i in y_pred]
        return np.array(y_pred_class)

