# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:42:37 2024

@author: 都诚
"""
import os
import pickle
os.chdir(r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月')

"""
导入已经跑完的模型，下面开始生成结果
"""
with open('result.pickle', 'rb') as f:
    data = pickle.load(f)
"""
7. 确定组分数，后面的步骤只剩出图和数据导出（如果需要）：分半分析图、组分图、
载荷图、（FMax图）
"""
fac = 2
#  出图
data.plot_split_result(fac)
data.plot_fingers(fac)
data.plot_loadings(fac)
data.plot_fmax(fac)
#  导出数据
data.parafac_result_output(fac)
data.open_fluor(fac, output_path=r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\result')
data.eems_output(output_path=r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\result')
data.fri_result_output(output_path=r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\result')
data.fluorescence_indices_output(output_path=r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\result')




