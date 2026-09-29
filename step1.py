import os
import numpy as np
import pickle
import EEMs_toolkit

os.chdir(r'd:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月')  # 将工作目录设置为您的项目文件夹

sample_log = EEMs_toolkit.read_sample_log(r'd:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\SampleLog.xlsx')
Abs, Abs_wave = EEMs_toolkit.read_abs(sample_log, r'd:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\UV')
blank = EEMs_toolkit.read_blank(sample_log, r'd:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\BlankEEMs')
c, fl = EEMs_toolkit.read_eems(sample_log, r'd:\博士论文\中国南水北调中线干渠藻类协同下的溶解有机质的变化趋势和作用机理\数据处理\PARAFAC\EEMs\winter_python -12月\EEMs')

Data = EEMs_toolkit.EEMs_Dataset(*c, file_list=fl)

# Data.dilute(sample_log['dilution'])

Data.minus_the_blank(blank)
Data.raman_areal(blank)
#Data.sub_dataset([], Data.ex < 250, Data.em > 600)
Data.inner_effect_correct(Abs_wave, Abs)
Data.cut_ray_scatter([15, 15], [20, 15])
Data.cut_ram_scatter([15, 15], [10, 10])
#Data.plot_eem_by1()
Data.miss_value_interpolation()
#Data.plot_eem_by1()
# 插值后处理NaN值
Data.x[np.isnan(Data.x)] = 0
#Data.plot_eem_by1()
with open('eem_data.pickle', 'wb') as f:
    pickle.dump(Data, f)

