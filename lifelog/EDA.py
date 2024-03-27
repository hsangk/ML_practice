# 필요한 라이브러리를 가져옵니다
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 수집
# 여기에서 데이터를 수집하는 코드를 작성합니다. 데이터는 파일에서 읽어오거나 API를 통해 가져올 수 있습니다.
# 예를 들어 CSV 파일을 불러올 때는 pandas의 read_csv 함수를 사용할 수 있습니다.
data = pd.read_csv("./data/result.csv")
data = data.iloc[:, 3:]
data.fillna(data.mean())

print("dtypes : ", data.dtypes)
print("describe : ", data.describe(include='all'))
data.plot.hist(alpha=0.5)
plt.show()

# 데이터 탐색
# 데이터의 구조를 이해하기 위해 데이터를 살펴봅니다.
print(data.head())  # 데이터의 처음 5개 행 출력
print(data.describe())  # 기술통계 정보 출력
print(data.info())  # 데이터 형식 및 누락된 값 확인

# 데이터 시각화
# 데이터를 시각적으로 표현하여 특성을 이해합니다.
plt.figure(figsize=(12, 5))
sns.pairplot(data)  # 산점도 행렬
plt.show()

# 데이터 분석
# 데이터를 분석하여 원하는 정보를 얻습니다.
mean_value = data['column_name'].mean()
max_value = data['column_name'].max()

# 결과 출력
print("평균 값:", mean_value)
print("최댓값:", max_value)
