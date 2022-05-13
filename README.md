# Complete-Project
as the name --> Complete Project
---
## 1. fNIRS signal analysis (**BOIL**)♈
* Data : 使用的是**清彥學長的資料**，從最原始血氧濾波到model出結果，為小弟的第一份project，如有不周多多見諒
* 日期 : 20220501
* 語言 : Python、scikit-learn
* 特色 : 在特徵選取的方面，**結合三位學長姐使用過的特徵萃取方法**，使特徵變得很多，且根據看過的[一篇paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449551/)使用了**傅立葉轉換**來取特徵，達到更好的結果
* 簡介 : 主要是拿來練習machine learning的技巧，因為網路上的練習資料多半是處理過，或是結果會很漂亮，才會被大家拿來當教學用，所以我想說趁這個難得有野生Data的機會，好好的練習一下
* 結果比較 : *學長碩論僅放最好的結果(CBI2)，故不知其他的成績*，然後意外的發現，學長與我的最好的部分**都是CBI2**

|分數|學長(Train/Test Acc)|我的(Train/Test Acc)|備註|
---|:---|:----|:---:
|CBI1| - | 92.8/88.8 |  |
|CBI2| 91.3/90.0 | **92.5/90.0** | Best!|
|A-Score| - | 92.5/88.8 | |
|D-Score| - | 92.5/88.8 | |

* Tag: filter、feature extracion、feature selection、built model、plot boundry、confusion metrix、AUC、Statistic
    
   
