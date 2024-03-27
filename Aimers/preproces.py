import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostClassifier, Pool, metrics, cv
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
import xgboost
from lightgbm import LGBMClassifier

df_train2 = pd.read_csv("train.csv")
df_train = pd.read_csv("train_processed_new.csv")
df_test = pd.read_csv("submission.csv") # 테스트 데이터(제출파일의 데이터)

# df_train.head() # 학습용 데이터 살펴보기
# df_train.info()
#
# df_train.isnull().sum()
print(df_train['expected_timeline'].unique())
print(df_train['expected_timeline'].value_counts())
print(df_train2['expected_timeline'].value_counts())
print('s')
