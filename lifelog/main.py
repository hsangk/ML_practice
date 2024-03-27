'''
Class
-------------------------------------
0 : 정상군 |  1 : 고위험군  | 2 : 환자군
-------------------------------------
'''

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

import xgboost

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data_path = "./data/result.csv"

df = pd.read_csv(data_path)
df = df.iloc[:, 1:]

X = df.iloc[:, 2:-1]
X = X.fillna(X.mean())
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=42)
col_names = X.columns

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ===============================================
# RandomForest

RandomForest = RandomForestClassifier()
RandomForest.fit(X_train_scaled, y_train)
feature_importance = RandomForest.feature_importances_

RandomForest_pred = RandomForest.predict(X_test_scaled)
RandomForest_score = RandomForest.score(X_test_scaled, y_test)
a = accuracy_score(RandomForest_pred, y_test)

cm_RF = confusion_matrix(y_test, RandomForest_pred)
cm_RF = pd.DataFrame(cm_RF).rename(index={0: '실제값(0)', 1: '실제값(1)', 2: '실제값(2)'},
                             columns={0: '예측값(0)', 1: '예측값(1)', 2: '예측값(2)'})

# ===============================================


# ===============================================
# XGBoost

XGBoost = xgboost.XGBClassifier().fit(X_train_scaled, y_train)
XGBoost_pred = XGBoost.predict(X_test_scaled)
XGBoost_score = accuracy_score(XGBoost_pred, y_test)

cm_XGBoost = confusion_matrix(y_test, RandomForest_pred)
cm_XGBoost = pd.DataFrame(cm_XGBoost).rename(index={0: '실제값(0)', 1: '실제값(1)', 2: '실제값(2)'},
                             columns={0: '예측값(0)', 1: '예측값(1)', 2: '예측값(2)'})

# ===============================================


# ===============================================
# Ensemble

logistic_regression = LogisticRegression()
kNN = KNeighborsClassifier()

voting_ensemble = VotingClassifier(estimators=[("LogisticRegression", logistic_regression), "KNN", kNN], voting='soft')
voting_ensemble.fit(X_train_scaled, y_train)
ensemble_pred = voting_ensemble.predict(X_test_scaled)
ensemble_score = accuracy_score()



# ===============================================

# sorted_idx = feature_importance.argsort()[::-1]
# plt.figure(figsize=(35, 6))
# plt.bar(range(X_train.shape[1]), feature_importance[sorted_idx], align="center")
# plt.xticks(range(X_train.shape[1]), col_names[sorted_idx])
# plt.ylim([0, 0.1])
# plt.xlabel("Feature Index")
# plt.ylabel("Feature Importance")
# plt.title("Feature Importance from Random Forest")
# plt.show()



print('done')
