# fNIRS signal analysis

------
## .ipynb file name explain 💹

1. Filter.ipynb  -> from origin data to filtered data，使用**四階butterworth**，截止頻率為**0.12**，output存成.csv
2. Extraction.ipynb -> Write extraction function，讓Get_Feature使用，使用了**約十種**特徵萃取方法
3. Get_Feature.ipynb -> Get Feature from all people， and output to excel
4. Model_and_Train -> Use three(four) pair of **feature selection and model**，and calculate the accuracy and ROC


## data file name explain 🔰

1. label.xlsx -> content label
2. VFT folder -> content **origin blood oxygen concentration data**


---
---
# Referance
[1] [Fernandez Rojas R, Huang X, Ou KL. A Machine Learning Approach for the Identification of a Biomarker of Human Pain using fNIRS. Sci Rep. 2019;9(1):5645. Published 2019 Apr 4. doi:10.1038/s41598-019-42098-w](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6449551/)

[2] [功能性近紅外光光譜特徵與哥本哈根過勞量表之關聯性分析: 以警察人員為實驗對象之研究](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=4a2sQ0/record?r1=3&h1=1)

[3] [智慧型功能近紅外光光譜術應用於周邊動脈阻塞疾病之預後研究](https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=4a2sQ0/record?r1=5&h1=1)

