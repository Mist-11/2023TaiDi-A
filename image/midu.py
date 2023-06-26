import pandas as pd
import pymssql
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

plt.rcParams['font.sans-serif'] = ['SimHei']

# 连接数据库
conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')

sqlstr = 'SELECT grid_point_id,x_coordinate,y_coordinate FROM 场所信息表'
place = pd.read_sql(sqlstr, conn)
print("完成所有地点获取")
sqlstr = 'SELECT grid_point_id,user_id FROM 场所码扫码信息表'
jilu = pd.read_sql(sqlstr, conn)
print("完成扫码记录获取")
jilu = jilu.groupby('grid_point_id').count().reset_index()
place = pd.merge(place, jilu, on='grid_point_id').rename(columns={'user_id': 'count'})
print('完成合并')

count = place['count']
bins = [0, 1000, 2000, 10000, np.inf]
colors = ['#D9EDEC', '#00C5EF', '#00E6CE', '#3E45D4']
label = ['两月内人流量小于1000', '两月内人流量小于2000', '两月内人流量小于10000', '两月内人流量大于10000']
color_indices = np.digitize(count, bins)
color_map = [colors[i - 1] for i in color_indices]
place = place.sort_values(by='count', ascending=False)
print('完成颜色处理')
x = place['x_coordinate']
y = place['y_coordinate']
sizes = place['count'] / 100
plt.scatter(x, y, s=sizes, c=color_map, label=label)
plt.savefig(r'./image/人口密度大致分布图.png')
plt.show()

# 关闭数据库连接
# conn.close()
