#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set_style('whitegrid')

#%%
df = pd.read_csv('kyphosis.csv')

#%%
df.head()

#%%
df.info()

#%%
df.describe()

#%%
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

#%%
sns.pairplot(df, hue='Kyphosis')

#%%
from sklearn.model_selection import train_test_split

X = df.drop('Kyphosis', axis = 1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#%%
from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

#%%
predictions = dtree.predict(X_test)

#%%
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))

#%%
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(classification_report(y_test, rfc_pred))
print(confusion_matrix(y_test, rfc_pred))