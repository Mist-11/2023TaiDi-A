import pymssql
import pandas as pd
import use_way
from datetime import datetime, timedelta

positive_self = pd.DataFrame(columns=['user_id', 'positive_time'])  # 自查阳性
positive_hesuan = pd.DataFrame(columns=['user_id', 'positive_time'])  # 核酸阳性
positive = pd.DataFrame(columns=['user_id', 'positive_time'])  # 阳性患者汇总名单
positive_place = pd.DataFrame(columns=['user_id', 'grid_point_id', 'create_time'])  # 阳性患者途径地区
mijie = pd.DataFrame(columns=['user_id', 'grid_point_id', 'create_t   ime', 'positive_id'])  # 密接名单
cimijie = pd.DataFrame(columns=['user_id', 'grid_point_id', 'create_time', 'mijie'])  # 次密接名单
columns = ['user_id', 'positive_time']
# 充当查密接临时存储
temp_positive_place2 = pd.DataFrame(columns=['user_id', 'grid_point_id', 'create_time'])
# 充当次密接接临时存储
temp_positive_place3 = pd.DataFrame(columns=['user_id', 'grid_point_id', 'create_time'])

# 连接数据库
conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')
db = conn.cursor()  # 获取游标

# 错误数据库
err_data = [20221000, 20220999,  20221131, 20221200, 20221201, 20221202, 20221203]

# 查找阳性人员
# 以下是核酸结果
sql_positive_result = "SELECT user_id,jcsj,cysj,grid_point_id from 核酸采样检测信息表 where jg = '阳性'"
temp_positive_result = pd.read_sql(sql_positive_result, conn)
a = 0
for index, row in temp_positive_result.iterrows():
    a += 1
    print("查询核酸中第%s个可能阳性患者" % str(a))
    sqlstr = "SELECT user_id,cysj,jcsj,jg from 核酸采样检测信息表 where user_id = %s" % row['user_id']
    result = pd.read_sql(sqlstr, conn)
    result = result.applymap(lambda x: x.encode('latin1').decode('gbk') if isinstance(x, str) else x)
    result = result[(timedelta(hours=-12) <= result["jcsj"] - row['jcsj']) & (
            result["jcsj"] - row['jcsj'] <= timedelta(days=3))]
    # print(result)
    result = result[result['jg'] == '阴性']
    if result.empty:
        data = [[row['user_id'], row['cysj']]]
        df = pd.DataFrame(data, columns=columns)
        positive_hesuan = pd.concat([positive_hesuan, df])
    else:
        continue

# 以下是自查
sql_positive_self = "SELECT user_id,dump_time from 个人自查上报信息表 where nucleic_acid_result = '1'"
temp_positive_self = pd.read_sql(sql_positive_self, conn)

a = 0
for index, row in temp_positive_self.iterrows():
    a += 1
    print("查询自查中第%s个可能阳性患者" % str(a))
    sqlstr = "SELECT user_id,cysj,jcsj,jg from 核酸采样检测信息表 where user_id = %s" % row['user_id']
    result = pd.read_sql(sqlstr, conn)
    result = result.applymap(lambda x: x.encode('latin1').decode('gbk') if isinstance(x, str) else x)
    result = result[(timedelta(hours=-12) <= result["cysj"] - row['dump_time']) & (
            result["cysj"] - row['dump_time'] <= timedelta(days=3))]

    # print(result)
    result = result[result['jg'] == '阴性']
    if result.empty:
        # print(result)
        data = [[row['user_id'], row['dump_time']]]
        df = pd.DataFrame(data, columns=columns)
        positive_self = pd.concat([positive_self, df])
    else:
        continue

# 汇总到positive
positive = pd.concat([positive, positive_hesuan])
positive = pd.concat([positive, positive_self])
positive = positive.sort_values(by=['user_id', 'positive_time']).drop_duplicates(subset=['user_id'])

print("阳性查找完毕")
# print("阳性名单为:\n", positive)
for index, row in positive.iterrows():  # 循环每一行数据
    sqlstr = "INSERT INTO 阳性人员  VALUES ('%s','%s')" % (str(row['user_id']), str(row['positive_time']))
    # print(sqlstr)
    db.execute(sqlstr)
conn.commit()  # 提交数据
print("阳性名单已提交数据库")

# 查找阳性经过地方(2天内)
sqlstr = 'SELECT user_id,positive_time from 阳性人员 '
positive = pd.read_sql(sqlstr, conn)
positive['positive_time'] = pd.to_datetime(positive['positive_time'])
positive['day'] = positive['positive_time'].dt.strftime('%Y%m%d')
positive['day'] = positive['day'].astype(int)
# print(positive.head())
a = 0
for index, row in positive.iterrows():
    a += 1
    print("已经查找" + str(a) + "位阳性患者")
    time1 = [row['day'] + 1, row['day'], row['day'] - 1, row['day'] - 2]
    time2 = []
    # print(time1)
    for i in time1:
        if i == 20221032:
            time2.append(20221101)
            continue
        if i == 20221100:
            time2.append(20221031)
            continue
        if i == 20221099:
            time2.append(20221030)
            continue
        if i == 20221199:
            time2.append(20221130)
            continue
        if i in err_data:
            continue
        time2.append(i)
    time2 = list(set(time2))
    # print(time2)
    for i in time2:
        sqlstr = "SELECT user_id,grid_point_id,create_time from [%s] where user_id = %s" % (str(i), str(row['user_id']))
        # print(sqlstr)
        temp_positive_place1 = pd.read_sql(sqlstr, conn)  # 用temp_positive_place1临时储存sql查询结果
        temp_positive_place1.index = [use_way.tianchong(temp_positive_place1, i)]
        temp_positive_place2 = pd.concat([temp_positive_place1, temp_positive_place2])  # 汇总到temp_positive_place2
temp_positive_place2 = temp_positive_place2.reset_index()  # 把temp_positive_place2的索引改为列
positive_place = temp_positive_place2.rename(columns={'level_0': 'day'})  # 过度，改一下表头
positive_place.drop_duplicates(inplace=True)
positive_place["create_time"] = pd.to_datetime(positive_place["create_time"])
print("阳性去过地方已查找完毕")
# print(positive_place.head())

# 不算密接地点
sqlstr = 'SELECT grid_point_id,name,point_type from 场所信息表'
result1 = pd.read_sql(sqlstr, conn)
point_type1 = ['医疗', '其他', '住宿', '办公', '邮政', '住宅', '旅游', '工作']
point_type2 = ['交通', '购物']
low_place = result1[result1['point_type'].isin(point_type1)]['grid_point_id'].tolist()
list2 = result1[result1['point_type'].isin(point_type2)]
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
    else:
        continue

# 可判定密接的出行记录
positive_place = positive_place[~positive_place['grid_point_id'].isin(low_place)]
positive_place.to_csv('./middle/yangxingout.csv', encoding='utf_8_sig')  # 数据存入csv,存储位置及文件名称

# 查找密接
a = 0
for index, row in positive_place.iterrows():
    # print(row["create_time"])
    a += 1
    sqlstr = 'SELECT user_id,grid_point_id,create_time from [%s] where grid_point_id = %s' % (
        str(row['day']), str(row['grid_point_id']))
    print('已查找第%s行数据' % str(a))
    result1 = pd.read_sql(sqlstr, conn)
    # print(result1.head())
    result1["create_time"] = pd.to_datetime(result1["create_time"])
    result1 = result1[abs(result1["create_time"] - row['create_time']) <= timedelta(minutes=10)]
    result1['positive_id'] = row['user_id']
    # print(result1)
    mijie = pd.concat([mijie, result1])
mijie.to_csv('./middle/mijieout.csv', encoding='utf_8_sig')  # 数据存入csv,存储位置及文件名称
# 输出密接名单，csv格式
mijie = mijie.rename(columns={'user_id': '密接者ID', 'grid_point_id': '密接场所ID', 'create_time': '密接日期',
                              'positive_id': '阳性人员ID'})  # 改成符合输出题目要求的表头
mijie = mijie[['密接者ID', '密接日期', '密接场所ID', '阳性人员ID']]
mijie.index = use_way.default_index(mijie)
mijie = mijie.sort_values(by=['密接者ID', "密接日期"]).drop_duplicates(subset='密接者ID')
list1 = positive["user_id"].tolist()
mijie = mijie[~mijie['密接者ID'].isin(list1)]
mijie = mijie.reset_index(drop=True)
mijie.index = mijie.index + 1
mijie.index.name = '序号'
# print('密接名单为：\n', mijie)
print("密接查找完毕")
# ---------------------------------------------以下是输出文件点一-----------------------------------------------------------
mijie.to_csv('./result/result1.csv', encoding='utf_8_sig')  # 数据存入csv,存储位置及文件名称
# ---------------------------------------------以上是输出文件点一-----------------------------------------------------------
# 改回原数据流程的表头
mijie = mijie.rename(columns={'密接者ID': 'user_id', '密接场所ID': 'grid_point_id', '密接日期': 'create_time',
                              '阳性人员ID': 'positive_id'})  # 改成符合输出题目要求的表头
mijie.index.name = ''
positive = positive.rename(columns={'user_id': 'positive_id'})
mijie = pd.merge(mijie, positive, on='positive_id')
mijie['positive_time'] = pd.to_datetime(mijie['positive_time'])
mijie['create_time'] = pd.to_datetime(mijie['create_time'])
mijie = mijie[mijie['positive_time'] >= mijie['create_time']]

a = 0
# 查找次密接
for index, row in mijie.iterrows():
    a += 1
    print("已经查找" + str(a) + "位密接患者")
    dates = pd.date_range(start=row['create_time'].floor('D'), end=row['positive_time'].floor('D'), freq='D')
    date_strs = [d.strftime('%Y%m%d') for d in dates]
    date_strs2 = []
    for i in date_strs:
        if int(i) in err_data:
            continue
        else:
            # print(i)
            date_strs2.append(i)
    for i in date_strs2:
        sqlstr = "SELECT user_id,grid_point_id,create_time from [%s] where user_id = %s" % (str(i), str(row['user_id']))
        # print(sqlstr)
        temp_positive_place1 = pd.read_sql(sqlstr, conn)  # 用temp_positive_place1临时储存sql查询结果
        temp_positive_place1.index = [use_way.tianchong(temp_positive_place1, i)]
        temp_positive_place3 = pd.concat([temp_positive_place1, temp_positive_place3])  # 汇总到temp_positive_place3
temp_positive_place3 = temp_positive_place3.reset_index()  # 把temp_positive_place2的索引改为列
ci_positive_place = temp_positive_place3.rename(columns={'level_0': 'day'})  # 过度，改一下表头
ci_positive_place.drop_duplicates(inplace=True)
ci_positive_place["create_time"] = pd.to_datetime(ci_positive_place["create_time"])
print("密接去过地方已查找完毕")
# print(positive_place.head())

ci_positive_place = ci_positive_place[~ci_positive_place['grid_point_id'].isin(low_place)]
ci_positive_place.to_csv('./middle/result4.csv', encoding='utf_8_sig')  # 数据存入csv,存储位置及文件名称
print("次密接查找完毕")

a = 0
for index, row in ci_positive_place.iterrows():
    # print(row["create_time"])
    a += 1
    sqlstr = 'SELECT user_id,grid_point_id,create_time from [%s] where grid_point_id = %s' % (
        str(row['day']), str(row['grid_point_id']))
    print('已查找第%s行数据' % str(a))
    result1 = pd.read_sql(sqlstr, conn)
    result1['mijie'] = row['user_id']
    # print(result1.head())
    result1["create_time"] = pd.to_datetime(result1["create_time"])
    result1 = result1[abs(result1["create_time"] - row['create_time']) <= timedelta(minutes=2)]
    result1['positive_id'] = row['user_id']
    # print(result1)
    cimijie = pd.concat([cimijie, result1])
# 输出次密接名单，csv格式
cimijie = cimijie.rename(columns={'user_id': '次密接者ID', 'grid_point_id': '次密接场所ID', 'create_time': '次密接日期',
                                  'mijie': '密接者ID'})  # 改成符合输出题目要求的表头
cimijie = cimijie[['次密接者ID', '次密接日期', '次密接场所ID', '密接者ID']]
cimijie.index = use_way.default_index(cimijie)
cimijie = cimijie.sort_values(by=['次密接者ID', "次密接日期"]).drop_duplicates(subset='次密接者ID')
list1 = positive["positive_id"].tolist()
list2 = mijie['user_id'].tolist()
cimijie = cimijie[~cimijie['次密接者ID'].isin(list1)]
cimijie = cimijie[~cimijie['次密接者ID'].isin(list2)]
cimijie = cimijie.reset_index(drop=True)
cimijie.index = cimijie.index + 1
cimijie.index.name = '序号'
# print("次密接名单为：\n", cimijie)
# ---------------------------------------------以下是输出文件点一-----------------------------------------------------------
cimijie.to_csv(r'./result/result2.csv', encoding='utf_8_sig')  # 数据存入csv,存储位置及文件名称
# ---------------------------------------------以上是输出文件点一-----------------------------------------------------------

# 关闭数据库连接
conn.close()
