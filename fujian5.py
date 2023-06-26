import os
import pandas as pd
import pymssql
from sqlalchemy import create_engine
conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')
db = conn.cursor()  # 获取游标
engine = create_engine('mssql+pymssql://sa:123456@127.0.0.1/covid-19control')
path = r'D:\Operation\学科竞赛\2023泰迪杯\code\data\附件5'
for filename in os.listdir(path):
    filepath = path + '/' + filename
    print('完成%s文件' % filepath)
    f1 = pd.read_csv(filepath)
    f1.to_sql('场所码扫码信息表', engine, if_exists='append', index=False)
conn.commit()  # 提交数据
conn.close()  # 关闭数据库
