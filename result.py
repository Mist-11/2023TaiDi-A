import pandas as pd

f1 = pd.read_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\result\result1.csv')
f2 = pd.read_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\result\result2.csv')
list1 = f1['密接者ID'].tolist()
f2 = f2[~f2['次密接者ID'].isin(list1)]
f2 = f2.drop(['序号'], axis=1)
f2 = f2.reset_index(drop=True)
f2.index = f2.index + 1
f2.index.name = '序号'
print(f2)
f2.to_csv(r'./result/result2.csv', encoding='utf_8_sig')
