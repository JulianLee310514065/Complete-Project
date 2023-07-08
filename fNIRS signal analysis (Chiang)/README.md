# fNIRS signal analysis (Chiang, Ting-Wei)

> form feature to accuracy

---
- Data : 會做這個是因為OPTIC與醫工年會需要投稿，但因為學姊並沒有留下原始資料，只有特徵萃取完的特徵跟label，所以我只做了建模跟畫圖分析的部分。
- 日期 : 202207
- 工具 : Python、scikit-learn
- 特色 : 雖然是下肢資料，但是是用我自己寫的程式去跑的，並沒有參考宇翰的程式，且學姊也沒留程式下來，所以就自己寫了一份，還有就是為了找到不要太好的結果去丟年會(以防paper發表時受阻)。所以使用mysql去存取多次實驗的結果並自動找出合適的結果。

---
## Python file name explain 🔰

**VA_svm.ipynb** → VA族群的SVM分析結果

**VV_svm.ipynb** → VV族群的SVM分析結果


## Other file name explain 🔰

**VA_after_norm.csv** → 學姊留下來的VA data
 
**VV_after_norm.csv** → 學姊留下來的VV data

**output.png** → 當初的結果

**CM.png** → 當初結果的confusion matrix

--- 
## Result
![output](https://github.com/JulianLee310514065/Complete-Project/blob/main/fNIRS%20signal%20analysis%20(Chiang)/output.png)

![CM](https://github.com/JulianLee310514065/Complete-Project/blob/main/fNIRS%20signal%20analysis%20(Chiang)/CM.png)

---
# Referance
[1] [葉克膜患者之疾病嚴重度量化研究：功能性近紅外光光譜特徵與急性生理評估系統之關聯性分析](https://hdl.handle.net/11296/v732tc)
