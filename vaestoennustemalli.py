# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:39:46 2021

@author: heidi
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Training data, Population in Finland 31.12. 
# Datasource: Statistics Finland
train_data = pd.DataFrame(np.array([[2010,5375276],[2011,5401267],[2012,5426674],[2013,5451270],[2014,5471753],[2015,5487308],[2016,5503297],[2017,5513130],[2018,5517919],[2019,5525292]]), columns=['Vuosi','Vaesto'])

X = np.array(train_data['Vuosi']).reshape((-1,1))
Y = np.array(train_data['Vaesto'])

# Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model = model.fit(X_poly, Y)

Y_pred = model.predict(X_poly)

# Plot the result
plt.scatter(X,Y)
plt.plot(X, Y_pred)
plt.xlabel('Vuosi')
plt.ylabel('Vaestoennuste')
plt.show()

# Show the model
print(model.coef_)
print(model.intercept_)

#%%

# Predict a single given value

pred_val = 2019

val = poly.fit_transform(np.array([[pred_val]]).reshape((-1,1)))
print(model.predict(val))

# Predict a single given value

pred = model.coef_[2]*pred_val**2 + model.coef_[1]*pred_val + model.intercept_
print(pred)

