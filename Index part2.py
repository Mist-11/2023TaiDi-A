import use_way
from sklearn.linear_model import Ridge
import pandas as pd
import pymssql
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# 设置画图中文
plt.rcParams['font.sans-serif'] = ['SimHei']

# 连接数据库
conn = connect = pymssql.connect(host='localhost', port='1433', user='sa', password='123456',
                                 database='covid-19control')
# 获取数据
result1 = use_way.people(conn)
# print(result1)
print('完成数据1获取')
result2 = use_way.place_temp_mean(conn)
print('完成数据2获取')
result3 = use_way.sexandage(conn)
print('完成数据3获取')
result4 = use_way.when_temp(conn)
print('完成数据4获取')
# 处理数据集
all_data = pd.merge(result1, result2, on=['grid_point_id', 'day'], how="left")
all_data = pd.merge(all_data, result3, on=['user_id'], how="left")
# print(all_data)
# print(result4)
all_data = pd.merge(all_data, result4, on=['user_id', 'day'], how="left")
test_data = all_data.drop(columns=['grid_point_id', 'day', 'all_counts', 'user_id', 'temperature_mean', 'create_time'])
print(all_data)
print(all_data.columns)
print('完成数据处理')
# 设置训练集
x = test_data.drop('p_counts', axis=1).values
y = test_data['p_counts'].values

# 训练
model = Ridge(alpha=0.1)  # 创建模型对象
model.fit(x, y)  # 拟合模型
# 设置各类系数和截距
beta1 = model.coef_[0]
beta2 = model.coef_[1]
beta3 = model.coef_[2]
s0 = 1
t0 = use_way.all_temp_mean(conn)
a0 = use_way.all_age_mean(conn)
# print(t0, a0)
# print(all_data)
print('完成系数计算')
print("beta1=%s,beta2=%s,beta3=%s,s0=%s,t0=%s,a0=%s" % (str(beta1), str(beta2), str(beta3), str(s0), str(t0), str(a0)))
Index = []
for index, row in all_data.iterrows():
    if row['all_counts'] == 0:
        a = 0
    else:
        a = (row['p_counts'] / row['all_counts']) * \
            (1 + beta1 * (row['age'] - a0) + beta2 * (row['temperature'] - t0) + beta3 * (row['gender'] - s0))
    Index.append(a)
all_data["index"] = Index
all_data = all_data.drop(columns=['all_counts', 'p_counts', 'age', 'temperature_mean', 'gender', 'temperature'])

# 按照user_id分组，然后对每个组应用加权平均函数
result = all_data.groupby('user_id').apply(use_way.weighted_average)
all_data = all_data.drop(columns=['grid_point_id', 'day', 'index']).drop_duplicates()
# 合并汇总
fin_data = all_data.drop_duplicates('user_id')
fin_data['w_index'] = result.values
fin_data.to_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\bingduindex.csv')
print("完成病毒系数计算")
# 查找疫苗信息
result5 = use_way.yimiao(conn)
# 将result5和result两个dataframe进行合并
result5 = pd.merge(all_data, result5, on='user_id', how='left')
# 根据user_id进行分组，求出每个人最大的inject_times
result5 = result5.groupby('user_id')['inject_times'].max().reset_index()
# 将结果和result再次进行合并，得到最终结果
all_data = pd.merge(fin_data, result5, on='user_id', how='left')
all_data.fillna(0, inplace=True)
print(all_data)
all_data.to_csv(r'C:\Users\Mist\Desktop\2023泰迪杯\code\middle\bingduindex.csv')
all_data['w_index'] = round(all_data['w_index'], 2)
print('得到结果')
list1 = all_data['w_index'].drop_duplicates().tolist()
print(list1)
grouped = all_data.groupby(['w_index', 'inject_times'])['user_id'].count()
percentages = (grouped / grouped.groupby(level=0).sum()) * 100
print(percentages)


def choosecolor(a):
    a = round(a)
    if a == 0:
        return 'grey'
    if a == 1:
        return 'brown'
    if a == 2:
        return 'red'
    if a == 3:
        return 'yellow'
    if a == 4:
        return 'green'


# 绘制柱状图
fig, ax = plt.subplots(figsize=(10, 6))
for w_index, group in percentages.groupby(level=0):
    bottom = None  # 记录下方柱子的高度
    for inject_times, percentage in group.iteritems():
        # print(inject_times[1])
        ax.bar(w_index, percentage, bottom=bottom, color=choosecolor(inject_times[1]), width=0.005)
        if bottom is None:
            bottom = 0
        bottom += percentage  # 更新下方柱子的高度

gray_patch = Patch(color='gray', label='0')
brown_patch = Patch(color='brown', label='1')
red_patch = Patch(color='red', label='2')
yellow_patch = Patch(color='yellow', label='3')
green_patch = Patch(color='green', label='4')
ax = plt.gca()
ax.legend(handles=[gray_patch, brown_patch, red_patch, yellow_patch, green_patch],
          labels=['未接种疫苗群众', '接种一针群众', '接种两针群众', '接种三针群众', '接种三针和加强针群众'],
          title='疫苗接种情况',bbox_to_anchor=(1.05, 1), loc='upper left')

# 设置图表标题、坐标轴标签和图例
ax.set_title('不同病毒感染率下疫苗人数占比')
ax.set_xlabel('病毒感染率')
ax.set_ylabel('占比')
plt.xticks(list1, list1)
plt.tight_layout()
plt.savefig(r'./image/不同病毒感染率下疫苗人数占比.png')
plt.show()

conn.close()
