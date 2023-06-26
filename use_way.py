import datetime
import pandas as pd
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt


# 写一些比较爽的方法
def delect_useless(a):
    b = a  # 先把数据copy过去
    # 删除positive_id列下没有用的()和,爽！
    # 原replace是对整个元素操作，加上.str，就会当作是对字符串进行操作，可以修改其中部分内容
    b['positive_id'] = a["positive_id"].astype(str).str.replace("(", "", regex=True)
    b['positive_id'] = a["positive_id"].astype(str).str.replace(")", "", regex=True)
    b['positive_id'] = a["positive_id"].astype(str).str.replace(",", "", regex=True)
    return b


def tianchong(x, y):  # 自动相关信息，填充列表，匹配dataframe的
    a = list()
    for i in range(x.shape[0]):  # 与查询结果行数相匹配的列表，填充相应内容
        a.append(y)
    return a


def default_index(x):
    a = list()
    for i in range(1, x.shape[0] + 1):
        a.append(i)
    return a


def SqlCommit_mijie(db, f1, l1):
    for index, row in f1.iterrows():  # 循环每一行数据
        sqlstr = 'INSERT INTO 密接名单  VALUES (' + "'" + str(row[l1[0]]) + "'" + ',' + "'" + str(
            row[l1[1]]) + "'" + ',' + "'" + str(row[l1[2]]) + "'" + ',' + "'" + str(row[l1[3]]) + "'" + ',' + "'" + str(
            row[l1[4]]) + "'" + ')'
        db.execute(sqlstr)


def SqlCommit_cimijie(db, f1, l1):
    for index, row in f1.iterrows():  # 循环每一行数据
        sqlstr = 'INSERT INTO 次密接名单  VALUES (' + "'" + str(row[l1[0]]) + "'" + ',' + "'" + str(
            row[l1[1]]) + "'" + ',' + "'" + str(row[l1[2]]) + "'" + ',' + "'" + str(row[l1[3]]) + "'" + ',' + "'" + str(
            row[l1[4]]) + "'" + ')'
        db.execute(sqlstr)


def people(conn):
    P_temp = pd.DataFrame(columns=['user_id', 'temperature'])
    f1 = pd.read_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\yangxingout.csv')
    f1 = f1.drop(f1.columns[0], axis=1)
    f1['create_time'] = pd.to_datetime(f1['create_time'])
    f1['day'] = f1['create_time'].dt.strftime('%Y%m%d')
    # print(f1)
    f2 = pd.read_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\mijieout.csv')
    f2 = f2.drop(f2.columns[0], axis=1)
    f2['create_time'] = pd.to_datetime(f2['create_time'])
    f2['day'] = f2['create_time'].dt.strftime('%Y%m%d')
    f2['day'] = f2['day'].astype(int)
    f2 = f2[~(f2['user_id'] == f2['positive_id'])]
    # print(f2)
    # print(f1)
    # 转换感染名单
    p = (f1.drop_duplicates('user_id'))['user_id'].tolist()
    # print(p)
    result5 = pd.DataFrame(columns=['user_id', 'grid_point_id', 'day', 'all_counts', 'p_counts'])
    for index, row in f1.iterrows():
        # print(row['grid_point_id'], row['user_id'], row['day'])
        temp = f2[(f2['grid_point_id'] == row['grid_point_id']) & (f2['positive_id'] == row['user_id']) & (
                f2['day'] == int(row['day']))]
        # print(temp)
        b = temp.shape[0]
        temp = temp[temp['user_id'].isin(p)]
        a = temp.shape[0]
        new_row = {'user_id': row['user_id'], 'grid_point_id': row['grid_point_id'],
                   'day': row['day'], 'all_counts': b, 'p_counts': a}
        result5 = result5.append(new_row, ignore_index=True)
        result5.to_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\pornot.csv')
    # print(result5)
    return result5


def place_temp_mean(conn):
    # 获取每个环境的温度，以日期为单位
    str2 = "SELECT grid_point_id,temperature,create_time from 场所码扫码信息表"
    g_temp = pd.read_sql(str2, conn)
    g_temp['create_time'] = pd.to_datetime(g_temp['create_time'])
    g_temp['day'] = g_temp['create_time'].dt.strftime('%Y%m%d')
    # 按照 grid_point_id 和日期分组，计算均值
    g_temp_mean = g_temp.groupby([g_temp['grid_point_id'], g_temp['day']])[
        'temperature'].mean().reset_index()
    g_temp_mean['temperature'] = round(g_temp_mean['temperature'], 1)  # 保留一位小数
    g_temp_mean.columns = ['grid_point_id', 'day', 'temperature_mean']  # 重命名列名
    g_temp_mean = g_temp_mean[['day', 'grid_point_id', 'temperature_mean']]  # 调整列顺序
    return g_temp_mean


def sexandage(conn):
    str = 'SELECT user_id,gender,age from 人员信息表'
    sex_age = pd.read_sql(str, conn).replace({'男': 2, '女': 1, '未知': 0})
    return sex_age


def when_temp(conn):
    str = 'SELECT user_id,temperature,create_time from 场所码扫码信息表'
    temp = pd.read_sql(str, conn)
    temp['day'] = temp['create_time'].dt.strftime('%Y%m%d')
    # print(temp)
    return temp


def all_temp_mean(conn):
    str = 'SELECT temperature from 场所码扫码信息表'
    temp = pd.read_sql(str, conn)
    return temp['temperature'].mean()


def all_age_mean(conn):
    str = 'SELECT age from 人员信息表'
    temp = pd.read_sql(str, conn)
    return temp['age'].mean()


# 定义加权平均函数
def weighted_average(group):
    weights = group['create_time'].rank(ascending=False)
    return (group['index'] * weights).sum() / weights.sum()


def yimiao(conn):
    sqlstr = "SELECT user_id,inject_times from 疫苗接种信息表"
    result5 = pd.read_sql(sqlstr, conn)
    result5 = result5.applymap(lambda x: x.encode('latin1').decode('gbk') if isinstance(x, str) else x)
    result5 = result5.replace({'第一针': 1, '第二针': 2, '第三针': 3, '加强针': 4})
    result5 = result5.drop_duplicates()
    return result5


def distance(conn):
    str2 = "SELECT x_coordinate,y_coordinate " \
           "from 场所信息表,场所码扫码信息表,阳性人员 " \
           "where 场所信息表.grid_point_id = 场所码扫码信息表.grid_point_id " \
           "and 场所码扫码信息表.user_id = 阳性人员.user_id"
    result2 = pd.read_sql(str2, conn)
    # print(result2)

    mean_x = np.mean(result2['x_coordinate'])
    mean_y = np.mean(result2['y_coordinate'])
    radius = np.mean(np.sqrt((result2['x_coordinate'] - mean_x) ** 2 + (result2['y_coordinate'] - mean_y) ** 2))
    # print(radius)
    return radius


def temp_threshold(conn):
    str1 = "SELECT temperature " \
           "from 场所码扫码信息表 "
    result1 = pd.read_sql(str1, conn)
    temp1 = result1['temperature'].mean()
    biaozun_temp1 = result1['temperature'].std()
    temp1 += biaozun_temp1/30
    # print(temp1)
    # print(biaozun_temp1)
    str2 = "SELECT temperature " \
           "from 场所码扫码信息表,阳性人员 " \
           "where 场所码扫码信息表.user_id = 阳性人员.user_id"
    result2 = pd.read_sql(str2, conn)
    temp2 = result2['temperature'].mean()
    biaozun_temp2 = result2['temperature'].std()
    temp2 += biaozun_temp2/30
    # print(biaozun_temp2)
    # print(temp2)
    temp = min(temp1, temp2)
    # print(temp)
    return temp


# 自定义百分数格式
def to_percent(x, pos):
    return '%1.0f%%' % x
