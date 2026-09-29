import pickle

"""
1. 导入刚才预处理好并保存的数据，加载变量
"""
with open('eem_data.pickle', 'rb') as f:
    data = pickle.load(f)
"""
2. （浏览所有样本，记录明显存在异常，即与其他样本显著不同或存在测试问题的样本编号）
"""
# data.plot_eem_by1()
"""
3. 进行不同组分数（2到6，可修改）的PARAFAC计算
"""
data.multi_non_parafac_cal([2, 6])
"""
4. 查看异常样本测试图，尝试不同的组分数，观察其异常样本
（即位于图右方和上方的样本，冒号前为样本编号），记录其样本编号
"""
for i in range(2, 6 + 1):
    data.plot_outlier_test(i)

