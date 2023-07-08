# fNIRS signal analysis (Zheng)
> From raw data to accuracy
--- 

* Data : 使用的是**宇翰學長的資料**，從最原始血氧濾波到模型分類結果，但因為資料帶有病歷號等個人隱私，故沒有放上github，此外葉克膜患者有分VA、VV，但因為程式差異不大，所以就使用VV做示範，VA再稍作改即可使用。
* 日期 : 202306
* 工具 : Python、scikit-learn
* 特色 : 此資料為下肢葉克膜的資料，其資料特點是**時間特長**一個人有長達50分鐘以上的資料，第二點是**有很多個階段**，這個在做階段相關的處理時會又有很大的差異，如階段平均差等。此外還用了[TDDR](https://www.sciencedirect.com/science/article/abs/pii/S1053811918308103?via%3Dihub)演算法來將peak雜訊消除。

---
## Python file name explain 🔰

**I_Clean.ipynb**  → Cleaned data by filling in missing values, separated by stages, filtered the data using a **fourth-order Butterworth filter** with a cutoff frequency of **0.12**, and outputted the results to a .csv file. 

**II_Feature_extraction.ipynb** → Get Feature from all people, and output to csv 

**III_Statisitic_svm.ipynb** → Model, plot, statisitic

**TDDR.py** → TDDR function, use `import TDDR` to import python file

---
# Referance
[1] [以光譜特徵智慧預測葉克膜患者器官衰竭評估](https://hdl.handle.net/11296/a57r6k)
