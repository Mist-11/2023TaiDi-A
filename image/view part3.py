import numpy as np
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import use_way

# 设置画图中文
plt.rcParams['font.sans-serif'] = ['SimHei']

# 连接数据库
conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')

P_agestr = "SELECT user_id,age from 人员信息表"
P_age = pd.read_sql(P_agestr, conn)

P_str = "SELECT user_id from 阳性人员"
P = pd.read_sql(P_str, conn)

merged = pd.merge(P_age, P, on='user_id')
counts = merged.groupby('age').count()
data1 = counts.reset_index()
print(data1)
P_temp = pd.DataFrame(columns=['user_id', 'temperature'])
f1 = pd.read_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\result1.csv')
f1 = f1.drop(f1.columns[0], axis=1)
print(f1)
a = 0
for index, row in f1.iterrows():
    a += 1
    print("遍历第%s行数据" % str(a))
    sqlstr = 'SELECT user_id,temperature from [%s] where grid_point_id = %s and user_id = %s' % (
        str(row['day']), str(row['grid_point_id']), str(row['user_id']))
    result1 = pd.read_sql(sqlstr, conn)
    P_temp = pd.concat([P_temp, result1])

merged = pd.merge(P_temp, P, on='user_id')
mean_temp = merged.groupby('user_id')['temperature'].mean()
merged2 = pd.merge(P_temp, mean_temp, on='user_id')
# merge重复拼接相同列名会把一个名后面+_x，一个+_y，需要改一下表头
merged2 = merged2.drop('temperature_x', axis=1).rename(columns={'temperature_y': 'temperature'})
merged2 = merged2.drop_duplicates()  # 拼接完后有重复数据，需要去重
counts = merged2.groupby('temperature').count()
data2 = counts.reset_index()
print(data2)
conn.close()

x1 = data1['age']
y1 = data1['user_id']
plt.figure(figsize=(12, 6))
plt.plot(x1, y1)
plt.xticks(np.arange(1, 100, 5))
plt.xlabel('age')
plt.ylabel('amount')
plt.title('年龄与感染人数')
plt.savefig(r'./image/年龄与阳性人数关系图-折线.png')
plt.show()

x1 = data1['age']
y1 = data1['user_id']
plt.figure(figsize=(12, 6))
plt.scatter(x1, y1)
plt.xticks(np.arange(1, 100, 5))
plt.xlabel('age')
plt.ylabel('amount')
plt.title('年龄与感染人数')
plt.savefig(r'./image/年龄与阳性人数关系图-散点.png')
plt.show()

x2 = data2['temperature']
y2 = data2['user_id']
plt.figure(figsize=(12, 6))
plt.xticks(np.arange(35.6, 37.2, 0.1))
plt.plot(x2, y2)
plt.xlabel('temperature')
plt.ylabel('amount')
plt.title('温度与感染人数')
plt.savefig(r'./image/温度与阳性人数关系图-折线.png')
plt.show()

x2 = data2['temperature']
y2 = data2['user_id']
plt.figure(figsize=(12, 6))
plt.xticks(np.arange(35.6, 37.2, 0.1))
plt.scatter(x2, y2)
plt.xlabel('temperature')
plt.ylabel('amount')
plt.title('温度与感染人数')
plt.savefig(r'./image/温度与阳性人数关系图-散点.png')
plt.show()

sqlstr = 'SELECT user_id,age from 人员信息表'
f1 = pd.read_sql(sqlstr, conn)
f1 = f1[(f1['age'] >= 0) & (f1['age'] <= 100)]
result1 = f1.groupby('age').count().reset_index()

sqlstr = 'SELECT user_id from 阳性人员'
f2 = pd.read_sql(sqlstr, conn)
f2 = pd.merge(f2, f1, on='user_id').groupby('age').count().reset_index().rename(columns={'user_id': 'p_count'})
# print(f2)
f3 = pd.merge(result1, f2, on='age', how='outer').rename(columns={'user_id': 'count'}).fillna(0)
f3['bili'] = round(f3['p_count'] / f3['count'] * 100, 2)

# print(result1)
x1 = f3['age']
y1 = f3['bili']
plt.figure(figsize=(12, 6))
plt.plot(x1, y1)
plt.xticks(np.arange(1, 100, 5))
plt.gca().yaxis.set_major_formatter(FuncFormatter(use_way.to_percent()))
plt.xlabel('年龄')
plt.ylabel('百分比')
plt.title('不同年龄之间阳性比例')
plt.savefig(r'./image/不同年龄之间阳性比例.png')
plt.show()
