import pandas as pd
import pymssql
import os
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')
engine = create_engine('mssql+pymssql://sa:123456@127.0.0.1/covid-19control')

db = conn.cursor()  # 获取游标
data2 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件2.csv')
data2['gender'] = data2['gender'].fillna('未知')
data2 = data2.dropna(subset=["age"])  # 删除age列中的缺失数据
data2['age'] = data2['age'].astype(int)
plt.boxplot(data2['age'])
plt.title('年龄分布情况（处理前）')
plt.ylabel('age')
plt.savefig(r'./image/年龄分布情况（处理前）.png')
plt.show()

q1 = data2['age'].quantile(0.25)
q3 = data2['age'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
lower_bound = q1 - 1.5 * iqr

data2 = data2[(data2['age'] >= lower_bound) & (data2['age'] <= upper_bound)]
plt.boxplot(data2['age'])
plt.title('年龄分布情况（处理后）')
plt.ylabel('age')
plt.savefig(r'./image/年龄分布情况（处理后）.png')
plt.show()
data2 = data2.dropna(subset=["birthdate"])
people = data2['user_id'].tolist()
for index, row in data2.iterrows():  # 循环每一行数据
    # user_id,openid,gender,nation,age,birthdate,create_time
    sqlstr = "INSERT INTO 人员信息表  VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (
        str(row['user_id']), str(row['openid']), str(row['gender']), str(row['nation']), str(round(row['age'])),
        str(row['birthdate']), str(row['create_time']))
    print(sqlstr)
    db.execute(sqlstr)
print("完成附件2")
data3 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件3.csv')
for index, row in data3.iterrows():  # 循环每一行数据
    # grid_point_id,name,point_type,x_coordinate,y_coordinate,create_time
    sqlstr = "INSERT INTO 场所信息表  VALUES ('%s','%s','%s','%s','%s','%s')" % (
        str(row['grid_point_id']), str(row['name']), str(row['point_type']), str(row['x_coordinate']),
        str(row['y_coordinate']), str(row['create_time']))
    db.execute(sqlstr)
print("完成附件3")
data4 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件4.csv')
data4 = data4[data4['user_id'].isin(people)]
for index, row in data4.iterrows():  # 循环每一行数据
    # sno,user_id,x_coordinate,y_coordinate,symptom,nucleic_acid_result ,resident_flag,dump_time
    sqlstr = "INSERT INTO 个人自查上报信息表  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        str(row['sno']), str(row['user_id']), str(row['x_coordinate']), str(row['y_coordinate']),
        str(row['symptom']), str(row['nucleic_acid_result']), str(row['resident_flag']), str(row['dump_time']))
    print(sqlstr)
    db.execute(sqlstr)
print("完成附件4")
data6 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件6.csv')
data6 = data6[data6['user_id'].isin(people)]
for index, row in data6.iterrows():  # 循环每一行数据
    # sno,user_id,cysj,jcsj,jg,grid_point_id
    sqlstr = "INSERT INTO 核酸采样检测信息表  VALUES ('%s','%s','%s','%s','%s','%s')" % (
        str(row['sno']), str(row['user_id']), str(row['cysj']), str(row['jcsj']),
        str(row['jg']), str(row['grid_point_id']))
    print(sqlstr)
    db.execute(sqlstr)

print("完成附件6")
data7 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件7.csv')
data7 = data7[~data7.duplicated(['user_id', 'inject_times', 'inject_date', 'vaccine_type'], keep=False)]
data7['birthdate'] = data7['birthdate'].fillna(pd.to_datetime('2021-01-01 00:00:00'))
data7 = data7[data7['user_id'].isin(people)]
for index, row in data7.iterrows():  # 循环每一行数据
    # sno,inject_sn,user_id,age,gender,birthdate,inject_date,inject_times,vaccine_type
    sqlstr = "INSERT INTO 疫苗接种信息表  VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        str(row['sno']), str(row['inject_sn']), str(row['user_id']), str(row['age']),
        str(row['gender']), str(row['birthdate']), str(row['inject_date']), str(row['inject_times']),
        str(row['vaccine_type']))
    print(sqlstr)
    db.execute(sqlstr)
print("完成附件7")

# 获取目录下所有csv文件名

path = r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件5'
columns = [
    ('sno', 'int'),
    ('grid_point_id', 'int'),
    ('user_id', 'int'),
    ('temperature', 'decimal(18, 2)'),
    ('create_time', 'datetime'),
]

# 遍历目录下的csv文件
a = 0
for filename in os.listdir(path):
    if filename.endswith('.csv') and len(filename) == 12:
        # 读取csv文件
        date = filename[:-4]
        filepath = os.path.join(path, filename)
        df = pd.read_csv(filepath)

        # 创建表
        table_name = filename[:-4]
        sql_create = f'CREATE TABLE [{table_name}]('
        for column, data_type in columns:
            sql_create += f'{column} {data_type},'
        sql_create = sql_create[:-1] + ')'
        cursor = conn.cursor()
        print(sql_create)
        cursor.execute(sql_create)
        conn.commit()

        # 插入数据
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        conn.commit()
        a += 1
        print('完成第' + str(a) + '个文件读取')

conn.commit()  # 提交数据
conn.close()  # 关闭数据库
