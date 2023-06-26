import pandas as pd
import pymssql
import numpy as np

import use_way

conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')
str1 = "SELECT 场所码扫码信息表.grid_point_id,name,x_coordinate,y_coordinate " \
       "from 场所码扫码信息表,场所信息表,阳性人员 " \
       "where 阳性人员.user_id = 场所码扫码信息表.user_id " \
       "and 场所码扫码信息表.grid_point_id = 场所信息表.grid_point_id"
result1 = pd.read_sql(str1, conn).drop_duplicates()
str2 = "SELECT grid_point_id,x_coordinate,y_coordinate from 场所信息表"
result2 = pd.read_sql(str2, conn)
# print(result1)
# print(result2)
# 筛选半径300内的场所
affected_places = []
radius = use_way.distance(conn)/25
print(radius)
# print(radius)
# 时间复杂度相对太高，弃用
# for index1, row1 in result1.iterrows():
#     for index2, row2 in result2.iterrows():
#         distance = math.sqrt(
#             (row1['x_coordinate'] - row2['x_coordinate']) ** 2 + (row1['y_coordinate'] - row2['y_coordinate']) ** 2)
#         if distance <= radius:
#             affected_places.append(row2['grid_point_id'])
# 将坐标列转换为数组
coords1 = np.array(result1[['x_coordinate', 'y_coordinate']])
coords2 = np.array(result2[['x_coordinate', 'y_coordinate']])

# 计算所有点之间的距离矩阵
dist_matrix = np.sqrt(np.sum((coords1[:, np.newaxis, :] - coords2) ** 2, axis=2))
# print(dist_matrix)

# 使用where()函数找出满足条件的点
idx1, idx2 = np.where(dist_matrix <= radius)
affected_places = list(result2.iloc[idx2]['grid_point_id'].values)
affected_places = list(set(affected_places))
print(len(affected_places))

# 进一步做体温判断
temp = use_way.temp_threshold(conn)
print(temp)
# 获取每个环境的温度，以日期为单位
str3 = "SELECT grid_point_id,temperature from 场所码扫码信息表"
g_temp = pd.read_sql(str3, conn)
g_temp = g_temp[g_temp['grid_point_id'].isin(affected_places)]  # 从所有扫码信息表中提取可能被影响区域
# 按照 grid_point_id 分组，计算均值
g_temp = g_temp.groupby(g_temp['grid_point_id'])['temperature'].mean().reset_index()
# g_temp['temperature'] = round(g_temp['temperature'], 1)  # 保留一位小数
result1 = pd.merge(result1, g_temp, on='grid_point_id', how='left')
result1.to_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\ptemp.csv')
# print(result1)
# result1 = result1.sort_values('temperature')
# result1 = result1.head(10)
# print(g_temp)
result1 = result1[result1['temperature'] >= temp]

# 不算密接地点
sqlstr = 'SELECT grid_point_id,name,point_type from 场所信息表'
result2 = pd.read_sql(sqlstr, conn)
point_type1 = ['医疗', '其他', '住宿', '办公', '邮政', '住宅', '旅游', '工作']
point_type2 = ['交通', '购物']
low_place = result2[result2['point_type'].isin(point_type1)]['grid_point_id'].tolist()
list2 = result2[result2['point_type'].isin(point_type2)]
for index, row in list2.iterrows():
    if '交通查验点' in row['name']:
        low_place.append(int(row['grid_point_id']))
        # print(row['name'])
    elif '加油站' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '公交站' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '码头' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '地铁站' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '超市' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '农集贸市场' in row['name']:
        low_place.append(int(row['grid_point_id']))
    elif '出租车' in row['name']:
        low_place.append(int(row['grid_point_id']))
    else:
        continue
result1 = result1[~result1['grid_point_id'].isin(low_place)]
print(result1)


conn.close()
