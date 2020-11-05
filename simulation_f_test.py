# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.feature_selection import f_classif

#%%

#np.random.seed(999)

#%% Create data

MU = 5.0
VAR = 8.0
GROUP_SIZE = 100

popu = pd.DataFrame(np.random.normal(loc=MU,scale=VAR,size=50000), columns=['data'])                     
group1 = pd.DataFrame(np.random.normal(loc=MU,scale=VAR,size=GROUP_SIZE), columns=['data'])
group2 = pd.DataFrame(np.random.normal(loc=MU,scale=VAR,size=GROUP_SIZE), columns=['data'])
group3 = pd.DataFrame(np.random.normal(loc=MU,scale=VAR,size=GROUP_SIZE), columns=['data'])

text_labels = ['population', 'group1', 'group2', 'group3']

popu['label'] = 0
group1['label'] = 1
group2['label'] = 2
group3['label'] = 3

df = pd.concat([popu, group1, group2, group3], ignore_index=True, axis=0)
df_group = pd.concat([group1, group2, group3], ignore_index=True, axis=0)


#%% Plot data

for dataset in [0,1,2,3]:
    
    sns.distplot(df.loc[df['label']==dataset, 'data'], hist=False, kde=True, label=text_labels[dataset])

plt.title('Density Plot')

#%% Variance between groups

# Group means
group_means = df_group.groupby('label').mean()
group_means['label'] = group_means.index

# The mean of the group means
means_mean = group_means['data'].mean()

# The sum of squared differences
squared_sum_b = GROUP_SIZE*sum((group_means['data'] - means_mean)**2)

# The between-group mean square value
df_b = 2
ms_b = squared_sum_b/df_b 

#%% Variance within groups

df_group_joined = df_group.join(group_means, rsuffix='_means', on='label')

# The sum of squares
squared_sum_w = sum((df_group_joined['data'] - df_group_joined['data_means'])**2)

# The within-group mean square value
df_w = 3*(GROUP_SIZE-1)
ms_w = squared_sum_w/df_w

#%% F Statistic

F_stat = ms_b/ms_w


#%% Calculate F Statistic and corresponding p values using sklearn library

xdata = np.array(df_group['data']).reshape(-1,1)
ydata = np.array(df_group['label'])

F_statistic, p_values = f_classif(xdata, ydata)

print('F statistics ',F_statistic,' and p-value ',p_values)






