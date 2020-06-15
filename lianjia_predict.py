from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import pandas as pd
import numpy as np


raw = pd.read_csv('D:\\Git\\Repositories\\lianjia\\cd_information.csv')

raw['Renovation1'] = raw['Renovation'].map({'精装': 3, '简装': 2, '毛坯': 1, '其他': 0})
# 将不同的朝向分别单独出来一列
raw['dong'] = raw['Region'].apply(lambda x: '东'in x).map({True: 1, False: 0})
raw['nan'] = raw['Region'].apply(lambda x: '南'in x).map({True: 1, False: 0})
raw['xi'] = raw['Region'].apply(lambda x: '西'in x).map({True: 1, False: 0})
raw['bei'] = raw['Region'].apply(lambda x: '北'in x).map({True: 1, False: 0})
# print(raw)
raw['Size1'] = raw['Size'].apply(lambda x: np.round(float(x.split('㎡')[0]), 2))
# print(raw['Size1'])
# 将室与厅单独统计出来
raw['shi'] = raw['Layout'].apply(lambda x: int(x.split('室')[0]))
raw['ting'] = raw['Layout'].apply(lambda x: int(x.split('室')[1].split('厅')[0]))
# print(raw['ting'])

raw['Elevator1'] = raw['Elevator'].map({'有': 1, '无': 0})
# print(raw['Elevator1'])

# 删除不需要的列
raw = raw.drop(['District', 'Floor', 'Id', 'Layout', 'Size', 'Region', 'Renovation', 'Elevator', 'Year'], axis=1)
# print(raw.head())

# 查看剩余属性是否具有缺失值
# print(np.isnan(raw).any())

# 删除缺失值所在的行"Price, Renovation1, Renovation1"
raw.dropna(inplace=True)
# print(np.isnan(raw).any())

# 除了价格的其他列
# print(raw.iloc[:, 1:])
# 实际价格
# print(raw.iloc[:, 0])


X_train, X_test, y_train, y_test = train_test_split(raw.iloc[:, 1:], raw.iloc[:, 0], test_size=0.33, random_state=0)

lr = LinearRegression()
# 使用训练数据进行参数估计
lr.fit(X_train, y_train)
# 回归预测
lr_y_predict = lr.predict(X_test)
# print(lr_y_predict)

for m, n in zip(lr_y_predict, y_test):
    print("预测房价是:", m, "实际房价是:", n)

score = r2_score(y_test, lr_y_predict)
print("模型拟合优度：", score)



