import pandas as pd
import pymssql
import pandas as pd
import use_way
from datetime import datetime, timedelta

f1 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\result\result1.csv')
# f1['密接场所ID'] = round(f1['密接场所ID'].astype(int))
# f1.drop(['序号'], axis=1, inplace=True)
# f1.index = f1.index + 1
# f1.index.name = '序号'
# print(f1)
# f1.to_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\result\result1.csv', encoding='utf_8_sig')

f2 = pd.read_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\result\result2.csv')
f2['次密接场所ID'] = round(f2['次密接场所ID'].astype(int))
f2.drop(['序号'], axis=1, inplace=True)
# list1 = f1['密接者ID'].tolist()
# f2 = f2[~f2['次密接者ID'].isin(list1)]
f2 = f2.reset_index(drop=True)
f2.index = f2.index + 1
f2.index.name = '序号'

print(f2)

f2.to_csv(r'D:\Operation\学科竞赛\2023泰迪杯\code\result\result2.csv')
