# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:41:42 2024

@author: 都诚
"""
import os
import pickle
from joblib import parallel_backend
# 若包含非ACSII字符则运行该代码
# 修改临时文件夹路径
os.chdir(r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月')  # 将工作目录设置为您的项目文件夹
os.environ['JOBLIB_TEMP_FOLDER'] = r'd:\Temp\joblib_temp'

# 加载预处理数据
with open('eem_data.pickle', 'rb') as f:
    data = pickle.load(f)

# 确保路径只包含ASCII字符
if not os.path.exists(r'd:\Temp\joblib_temp'):
    os.makedirs(r'd:\Temp\joblib_temp')

# 使用修改后的路径进行计算
with parallel_backend('loky', inner_max_num_threads=1):
    data.multi_non_parafac_cal([2, 6])

for i in range(2, 6 + 1):
    data.plot_outlier_test(i)

