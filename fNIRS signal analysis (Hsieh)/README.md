# fNIRS Signal Analysis (**BOIL**)
> From raw data to accuracy
---
* Data : 使用的是**清彥學長的資料**，從最原始血氧濾波到model出結果
* 日期 : 20220501 (202306翻新)
* 工具 : Python、scikit-learn
* 特色 : 在特徵選取的方面，**結合三位學長姐使用過的特徵萃取方法**，使特徵變得很多，且根據看過的[一篇paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449551/)使用了**傅立葉轉換**來取特徵，達到更好的結果
* 簡介 : 主要是拿來練習machine learning的技巧，因為網路上的練習資料多半是處理過，或是結果會很漂亮，才會被大家拿來當教學用，所以我想說趁這個難得有野生Data的機會，好好的練習一下
* 結果比較 : 學長碩論僅放最好的結果(CBI2)，故不知其他的成績，然後意外的發現，學長與我的最好的部分**都是CBI2**

|分數|學長(Train/Test Acc)|我的(Train/Test Acc)|備註|
---|:---|:----|:---:
|CBI1| - | 92.8/88.8 |  |
|CBI2| 91.3/90.0 | **92.5/90.0** | Best!|
|A-Score| - | 92.5/88.8 | |
|D-Score| - | 92.5/88.8 | |

* Tag: filter、feature extracion、feature selection、built model、plot boundry、confusion metrix、AUC、Statistic

------
## Python file name explain 🔰

**1_Filter.ipynb**  →  from origin data to filtered data, use **four stage butterworth**, cutoff frequency is **0.12**, and output to .csv 

**2_Get_Feature.ipynb** → Get Feature from all people, and output to excel 

**feature_extraction_function** → A ipynb contain extraction function,and Get_Feature will use it. It is about ten feature extraction methods

**3_Model_and_Train.ipynb** → Use two pair of **feature selection and model**，and calculate the accuracy and ROC 


## Other file name explain 🔰

**label.xlsx** → contain label

**VFT (folder)** → contain **origin blood oxygen concentration data**

**fNIRS from raw data to  accuracy.pptx** → The ppt that I reported before. (In Chainese)

**Filtered (folder)** → Data after filtering

**Feature.xlsx** → Data after feature extraction(2_Get_Feature.ipynb)

---

# Referance
[1] [Fernandez Rojas R, Huang X, Ou KL. A Machine Learning Approach for the Identification of a Biomarker of Human Pain using fNIRS. Sci Rep. 2019;9(1):5645. Published 2019 Apr 4. doi:10.1038/s41598-019-42098-w](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449551/)

[2] [功能性近紅外光光譜特徵與哥本哈根過勞量表之關聯性分析: 以警察人員為實驗對象之研究](https://hdl.handle.net/11296/e7qn5s)

[3] [智慧型功能近紅外光光譜術應用於周邊動脈阻塞疾病之預後研究](https://hdl.handle.net/11296/256553)

