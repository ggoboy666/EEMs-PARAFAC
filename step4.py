# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:42:36 2024

@author: 都诚
"""
import os
import pickle
os.chdir(r'D:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月') 
"""
5. 去除异常样本后，重新进行不同组分数的PARAFAC计算，此处为简化过程，只去除了部分
异常样本，主要为看起来显著不同的样本。实际进行操作时建议去除异常样本后重新建立模
型查看异常样本测试图，反复记录异常样本编号再去除，直到其leverage基本不大于0.3，
这样后续分析成功率更高，无论去除了多少样本，冒号前面的样本编号不会发生变化，每次
记录后添加到最开始去除异常样本的位置即可
"""
with open('eem_data.pickle', 'rb') as f:
    data = pickle.load(f)
data.sub_dataset([9 ])
data.multi_non_parafac_cal([2, 6])
for i in range(2, 6 + 1):
    data.plot_outlier_test(i)
"""
6. 后续步骤只有一个目的，确定组分数。首先进行分半分析，这会在窗口中打印出每个组
分的因子相似度及是否经过相似度检验。也可以画图查看不同组分数的因子相似度，在0.95
之上可认为是一致的。再综合考虑核一致性（不总是可靠）、不同组分数的模型残差，选择
相对较好的组分数（因子相似度高、核一致性高、残差为随机分布，不存在明显的峰），
事实上在这一步一般就会选择满足相似度的最大组分数，而在drEEM中，满足此条件的模型
可认为是经过验证的，可以结束此过程得到结果了
"""
data.split_analysis([2, 6])
data.plot_factor_similarity()
data.plot_core_consistency_and_explanation()
# for i in range(2, 6 + 1):
#     data.plot_residual_error(i)
"""
因为要分析完前面的结果才能确定组分数，重复跑模型还是很花时间的，所以将跑完的模型
先保存
"""
with open('result.pickle', 'wb') as f:
    pickle.dump(data, f)