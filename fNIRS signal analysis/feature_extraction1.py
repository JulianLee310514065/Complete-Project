#%%
# 使用.py 才能直接import 

import os
import glob

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Feature Extraction (From Lowpass filter)
### 清彥
# 1. 階段起始斜率 (8s) $\checkmark$
#     * Task
#     * Recovery
# >   
# 2. 階段平均的差     $\checkmark$
#     * Task mean – Rest mean
#     * Recovery mean – Rest mean
#     * Task mean – Recovery mean   
# 
# 3. 階段峰值     $\checkmark$
#     * Task
# 
# 4. 階段標準差    $\checkmark$
#     * 三個
# 
### 品妤
# 
# 5. 階段平均  $\checkmark$
#    * 三個
# >
# 6. 階段起始斜率 的差   $\checkmark$
#     * Task - Recovery
### 我 
# 1. AUC
# 
### 杰勳 bandpass
# 1. Stage skewness
# 2. Stage kurtosis

# 階段斜率
def stage_begin_slope(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, slope_period = 8, stage_end = 160):
    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of slope
    #         Tuple[1] : List of index
    #=======================




    # 第二階段起始斜率
    slope_df = dataframe.loc[stage2_start:stage2_start + slope_period] # 水平的取起來
    slope12_index = [col + "_Task_begin_slope" for col in  slope_df.columns]

    slope12 = []
    for i in range(len(slope_df.columns)):
        a = (slope_df.iloc[-1, i] - slope_df.iloc[0, i])/slope_period  # n秒
        slope12.append(a)
    

    # 第三階段起始斜率
    slope_df34 = dataframe.loc[stage3_start:stage3_start + slope_period] # 水平的取起來
    slope34_index = [col + "_Recovery_begin_slope" for col in  slope_df34.columns]
    
    slope34 = []
    for i in range(len(slope_df.columns)):
        a = (slope_df34.iloc[-1, i] - slope_df34.iloc[0, i])/slope_period  #n秒
        slope34.append(a)
    


    if plot == True:
        # -------plot-------
        plt.figure(figsize= figsize)

        stage1 = stage2_start
        stage2 = stage3_start
        stage3 = stage_end
        text_size = 25

        xp1 = np.arange(stage1, stage1 + slope_period, 0.1)
        x1 = np.arange(0, slope_period, 0.1)
        y1 = x1*slope12[use_col] + slope_df.iloc[0, use_col]

        xp2 = np.arange(stage2, stage2 + slope_period, 0.1)
        x2 = np.arange(0, slope_period, 0.1)
        y2 = x2*slope34[use_col] + slope_df34.iloc[0, use_col]
        
        plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
        plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
        plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.vlines(stage1 + slope_period, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第二階段
        plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
        plt.plot(xp1, y1, linewidth=5.0, c= 'r')
        plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
        plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.vlines(stage2 + slope_period, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第三階段
        plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
        plt.plot(xp2, y2, linewidth=5.0, c= 'r')
        plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
        plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        plt.title(dataframe.columns[use_col] + "_stage_begin_slope", fontdict={'fontsize': 24})

        plt.show()


    return slope12 + slope34, slope12_index + slope34_index

#%%

def stage_begin_slope_diff(dataframe, stage2_start = 30, stage3_start = 90, slope_period = 8, stage_end = 160):

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of slope diff
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    slope_df = dataframe.loc[stage1:stage1 + slope_period]
    slope12 = []
    for i in range(len(slope_df.columns)):
        a = (slope_df.iloc[-1, i] - slope_df.iloc[0, i])/slope_period  #八秒
        slope12.append(a)
    
    slope_df34 = dataframe.loc[stage2:stage2 + slope_period]
    slope34 = []
    for i in range(len(slope_df.columns)):
        a = (slope_df34.iloc[-1, i] - slope_df34.iloc[0, i])/slope_period  #八秒
        slope34.append(a)


    colset = []
    for col in dataframe.columns:
        colset.append(col + "_Task_Recovery_begin_slope_diff")

    slope_diff = np.array(slope12) - np.array(slope34)

    return list(slope_diff), colset    



# %%
def stage_mean(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):
    # 階段平均
    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of mean
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    Rest = []
    Task = []
    Recovery = []

    Rest_c = []
    Task_c = []
    Recovery_c = []

    for col in dataframe.columns:

        Rest.append(dataframe.loc[:stage1, col].mean())  #pandas 有 .mean() 可以用
        Rest_c.append(col + '_Rest_mean')

        Task.append(dataframe.loc[stage1:stage2, col].mean())
        Task_c.append(col + '_Task_mean')


        Recovery.append(dataframe.loc[stage2:stage3, col].mean())
        Recovery_c.append(col + '_Recovery_mean')



    if plot == True:
        #-------plot
        plt.figure(figsize= figsize)
        text_size = 25

        xp1 = np.arange(0, stage1, 0.1)
        y1 = np.full(xp1.shape, Rest[use_col])
        

        xp2 = np.arange(stage1, stage2, 0.1)
        y2 = np.full(xp2.shape, Task[use_col])

        xp3 = np.arange(stage2, stage3, 0.1)
        y3 = np.full(xp3.shape, Recovery[use_col])
        
        plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
        plt.plot(xp1, y1, linewidth=5.0, c= 'r')
        plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
        plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第二階段
        plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
        
        plt.plot(xp2, y2, linewidth=5.0, c= 'r')
        plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
        plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第三階段
        plt.plot(xp3, y3, linewidth=5.0, c= 'r')
        plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
        
        plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
        plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        plt.title(dataframe.columns[use_col] + "_stage_mean", fontdict={'fontsize': 24})

        plt.show()

    return Rest + Task + Recovery, Rest_c + Task_c + Recovery_c

# %%
# 階段平均差
def stage_mean_diff(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of mean diff or activation
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    Task_Rest = []
    Recovery_Rest = []
    Task_recovery = []
    

    Task_Rest_c = []
    Recovery_Rest_c = []
    Task_recovery_c = []

    for col in dataframe.columns:
        # 階段平均差
        Task_Rest.append(dataframe.loc[stage1:stage2, col].mean() - dataframe.loc[:stage1, col].mean())
        Task_Rest_c.append(col + '_Task_m_Rest')

        Task_recovery.append(dataframe.loc[stage1:stage2, col].mean() - dataframe.loc[stage2:stage3, col].mean())
        Task_recovery_c.append(col + '_Task_m_Recovery')

        # 活化值
        Recovery_Rest.append(dataframe.loc[stage2:stage3, col].mean() - dataframe.loc[:stage1, col].mean())
        Recovery_Rest_c.append(col + '_Recovery_m_Rest')



    if plot == True:

        import matplotlib.patches as patches

        Rest = []
        Task = []
        Recovery = []

        for col in dataframe.columns:

            Rest.append(dataframe.loc[:stage1, col].mean())
            Task.append(dataframe.loc[stage1:stage2, col].mean())
            Recovery.append(dataframe.loc[stage2:stage3, col].mean())


        #-------plot
        plt.figure(figsize= figsize)
        text_size = 25

        xp1 = np.arange(0, stage1, 0.1)
        y1 = np.full(xp1.shape, Rest[use_col])
        

        xp2 = np.arange(stage1, stage2, 0.1)
        y2 = np.full(xp2.shape, Task[use_col])

        xp3 = np.arange(stage2, stage3, 0.1)
        y3 = np.full(xp3.shape, Recovery[use_col])
        
        plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
        plt.plot(xp1, y1, linewidth=3.0, c= 'r')
        plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
        plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=1.0)
        plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第二階段
        plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
        plt.plot(xp2, y2, linewidth=3.0, c= 'r')

        plt.annotate(s='', xy=(stage1 + 2, Task[use_col] - 0.03), xytext=(stage1 + 2, Rest[use_col] +0.03), arrowprops=dict(arrowstyle='<->', mutation_scale=10, color= 'k', linewidth= 5))

        plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
        plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=1.0)
        plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第三階段
        plt.plot(xp3, y3, linewidth=3.0, c= 'r')
        plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
        
        plt.annotate(s='', xy=(stage2 + 2, Recovery[use_col] - 0.03), xytext=(stage2 + 2, Task[use_col] +0.03),arrowprops=dict(arrowstyle='<->', mutation_scale=10, color= 'k', linewidth= 5))
        
        plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
        plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        plt.title(dataframe.columns[use_col] + "_stage_mean_diff", fontdict={'fontsize': 24})

        plt.show()
        
    
    return Task_Rest + Recovery_Rest + Task_recovery, Task_Rest_c + Recovery_Rest_c + Task_recovery_c




# %%
# 峰值

def stage_acivation(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of 峰值
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    diffs = []
    diffs_name = []

    for cols in dataframe.columns:

        diff = dataframe.loc[stage1:stage2, cols].max() - dataframe.loc[stage1:stage2, cols].min()
        diffs.append(diff)
        diffs_name.append(cols + "_stage_activation")


    if plot == True:
        #-------plot
        plt.figure(figsize= figsize)
        text_size = 25


        
        plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
        plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
        plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第二階段
        plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
        plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
        plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)

        plt.hlines(dataframe.loc[stage1:stage2, dataframe.columns[use_col]].min(), stage1, stage2, linestyles= '-', colors= 'black',  linewidth=5.0)
        plt.hlines(dataframe.loc[stage1:stage2, dataframe.columns[use_col]].max(), stage1, stage2, linestyles= '-', colors= 'black',  linewidth=5.0)
        plt.annotate(s='', xy=( (stage1 + stage2)/2, dataframe[dataframe.columns[use_col]].loc[stage1:stage2].min()), xytext=( (stage1 + stage2)/2, dataframe[dataframe.columns[use_col]].loc[stage1:stage2].max()),arrowprops=dict(arrowstyle='<->', mutation_scale=10, color= 'k', linewidth= 5))

        plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第三階段
        plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
        
        plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
        plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        plt.title(dataframe.columns[use_col] + "_stage_acivation", fontdict={'fontsize': 24})

        plt.show()

    return diffs, diffs_name
    
# %%
def stage_std(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of std
    #         Tuple[1] : List of index
    #=======================

    
    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    Rest_std = []
    Task_std = []
    Recovery_std = []

    Rest_std_c = []
    Task_std_c = []
    Recovery_std_c = []

    for col in dataframe.columns:

        Rest_std.append(dataframe.loc[:stage1, col].std())  # 簡單方便 .std
        Rest_std_c.append(col + '_Rest_std')

        Task_std.append(dataframe.loc[stage1:stage2, col].std())
        Task_std_c.append(col + '_Task_std')


        Recovery_std.append(dataframe.loc[stage2:stage3, col].std())
        Recovery_std_c.append(col + '_Recovery_std')



    if plot == True:

        Rest = []
        Task = []
        Recovery = []

        for col in dataframe.columns:

            Rest.append(dataframe.loc[:stage1, col].mean())
            Task.append(dataframe.loc[stage1:stage2, col].mean())
            Recovery.append(dataframe.loc[stage2:stage3, col].mean())

        #-------plot
        plt.figure(figsize= figsize)
        text_size = 25

        xp1 = np.arange(0, stage1, 0.1)
        y1 = np.full(xp1.shape, Rest[use_col])
        

        xp2 = np.arange(stage1, stage2, 0.1)
        y2 = np.full(xp2.shape, Task[use_col])

        xp3 = np.arange(stage2, stage3, 0.1)
        y3 = np.full(xp3.shape, Recovery[use_col])
        
        plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
        plt.plot(xp1, y1, linewidth=5.0, c= 'r')

        plt.errorbar((stage1)/2, Rest[use_col], Rest_std[use_col], linestyle='-', marker='^', elinewidth= 3, ecolor= 'k', capsize= 10)

        plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
        plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第二階段
        plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
        plt.plot(xp2, y2, linewidth=5.0, c= 'r')

        plt.errorbar((stage1 + stage2)/2, Task[use_col], Task_std[use_col], linestyle='-', marker='^', elinewidth= 3, ecolor= 'k', capsize= 10)
        plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
        plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
        plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        # 第三階段
        plt.plot(xp3, y3, linewidth=5.0, c= 'r')
        plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
        
        plt.errorbar((stage3 + stage2)/2, Recovery[use_col], Recovery_std[use_col], linestyle='-', marker='^', elinewidth= 3, ecolor= 'k', capsize= 10)
        plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
        plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

        plt.title(dataframe.columns[use_col] + "_stage_std", fontdict={'fontsize': 24})

        plt.show()

    return Rest_std + Task_std + Recovery_std, Rest_std_c + Task_std_c + Recovery_std_c
# %%
def stage_skew(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):
    from scipy.stats import skew

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of skew
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end
    
    text_size = 25

    rest_skew = []
    task_skew = []
    recovery_skew = []

    rest_skew_c = []
    task_skew_c = []
    recovery_skew_c = []

    for cols in dataframe.columns:

        rest_skew.append(skew(dataframe.loc[:stage1, cols]))
        rest_skew_c.append(cols + '_rest_skew')

        task_skew.append(skew(dataframe.loc[stage1:stage2, cols]))
        task_skew_c.append(cols + '_task_skew')

        recovery_skew.append(skew(dataframe.loc[stage2:stage3, cols]))
        recovery_skew_c.append(cols + '_recovery_skew')

    if plot == True:
            #-------plot
            plt.figure(figsize= figsize)
            
            plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
            plt.axvspan(0, stage1, facecolor=sns.color_palette('Paired')[0], alpha=0.5)
            plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
            plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

            # 第二階段
            plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
            plt.axvspan(stage1, stage2, facecolor=sns.color_palette('Paired')[1], alpha=0.5)
            
            
            
            plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
            plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

            # 第三階段
            plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
            plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
            plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))
            
            plt.title(dataframe.columns[use_col] + "_stage_skew", fontdict={'fontsize': 24})

            plt.axes([0.65, 0.2, 0.2, 0.2])
            sns.histplot(dataframe.loc[stage1:stage2, dataframe.columns[use_col]], bins= 30)
            plt.title("Task skew", fontdict={'fontsize': 13})


            

            plt.show()


    return rest_skew + task_skew + recovery_skew, rest_skew_c + task_skew_c + recovery_skew_c

# %%
def stage_kurtosis(dataframe, stage2_start = 30, stage3_start = 90, stage_end = 160):

    from scipy.stats import kurtosis

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of kurtosis
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end


    rest_skew = []
    task_skew = []
    recovery_skew = []

    rest_skew_c = []
    task_skew_c = []
    recovery_skew_c = []

    for cols in dataframe.columns:

        rest_skew.append(kurtosis(dataframe.loc[:stage1, cols]))
        rest_skew_c.append(cols + '_rest_kurtosis')

        task_skew.append(kurtosis(dataframe.loc[stage1:stage2, cols]))
        task_skew_c.append(cols + '_task_kurtosis')

        recovery_skew.append(kurtosis(dataframe.loc[stage2:stage3, cols]))
        recovery_skew_c.append(cols + '_recovery_kurtosis')

    return rest_skew + task_skew + recovery_skew, rest_skew_c + task_skew_c + recovery_skew_c

# %%

def stage_auc(dataframe, plot= False, figsize= (10, 6), use_col= 0, stage2_start = 30, stage3_start = 90, stage_end = 160):
    from sklearn.metrics import auc

    #============================
    # Parameter: 
    #     dataframe:  input dataframe
    #     plot : whether to plot
    #     figsize: plt.figure(figsize= figsize)
    # Return:
    #     Tuple: 
    #         Tuple[0] : List of auc
    #         Tuple[1] : List of index
    #=======================

    stage1 = stage2_start
    stage2 = stage3_start
    stage3 = stage_end

    text_size = 25

    rest_auc = []
    Task_auc = []
    recovery_auc = []

    rest_auc_c = []
    Task_auc_c = []
    recovery_auc_c = []

    for cols in dataframe.columns:    
        rest_auc.append(auc(dataframe.loc[:stage1, cols].index, dataframe.loc[:stage1, cols]))
        rest_auc_c.append(cols + '_rest_auc')

        Task_auc.append(auc(dataframe.loc[stage1:stage2, cols].index, dataframe.loc[stage1:stage2, cols]))
        Task_auc_c.append(cols + '_Task_auc')

        recovery_auc.append(auc(dataframe.loc[stage2:stage3, cols].index, dataframe.loc[stage2:stage3, cols]))
        recovery_auc_c.append(cols + '_recovery_auc')

    if plot == True:
            #-------plot
            plt.figure(figsize= figsize)
            
            plt.plot(dataframe.loc[:stage1].index, dataframe.loc[:stage1, dataframe.columns[use_col]], c= 'b',  linewidth=2.0, label= 'Rest')
            
            yy1 = dataframe.loc[0:stage1, dataframe.columns[use_col]]
            plt.fill_between(np.linspace(0, stage1, yy1.shape[0]), yy1, step="pre", facecolor=sns.color_palette('Paired')[0], y2=-0.1)
            plt.vlines(stage1, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
            plt.text(stage1/2, 1.2, "rest", size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

            # 第二階段
            plt.plot(dataframe.loc[stage1:stage2].index, dataframe.loc[stage1:stage2, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Task')
            yy2 = dataframe.loc[stage1:stage2, dataframe.columns[use_col]]
            plt.fill_between(np.linspace(stage1, stage2, yy2.shape[0]), yy2, step="pre", facecolor=sns.color_palette('Paired')[1], y2=-0.1)
            
            plt.vlines(stage2, -0.1, 1.3, linestyles= '--', colors= 'black',  linewidth=2.0)
            plt.text((stage2 + stage1)/2, 1.2, 'Task', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))

            # 第三階段
            plt.plot(dataframe.loc[stage2:stage3].index, dataframe.loc[stage2:stage3, dataframe.columns[use_col]], c= 'b', linewidth=2.0, label= 'Recovery')
            # plt.axvspan(stage2, stage3, facecolor=sns.color_palette('Paired')[2], alpha=0.75)
            plt.text((stage3 + stage2)/2, 1.2, 'Recovery', size= text_size, ha="center", va= 'center', bbox=dict(boxstyle="round",ec=(1., 0.5, 0.5),fc=(1., 0.8, 0.8),))
            
            yy3 = dataframe.loc[stage2:stage3, dataframe.columns[use_col]]
            plt.fill_between(np.linspace(stage2, stage3, yy3.shape[0]), yy3, step="pre", facecolor=sns.color_palette('Paired')[2], y2=-0.1)

            plt.title(dataframe.columns[use_col] + "_stage_auc", fontdict={'fontsize': 24})

            plt.show()


    return rest_auc + Task_auc + recovery_auc, rest_auc_c + Task_auc_c + recovery_auc_c
    