# Complete-Project
as the name --> Complete Project
---
## 1. fNIRS signal analysis (**Hsieh, Cing­Yan**)♈
* Data : 使用的是**清彥學長的資料**，從最原始血氧濾波到model出結果
* 日期 : 20220501
* 工具 : Python、scikit-learn
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

<!--
心得:
首先先感謝aicup給我機會可以參加到這個segmentation的比賽，但是這比賽有**很多**需改進的地方，且全部都在那20%報告處，對，最後成績報告佔了20%，一堆不認識的衝上榜。我就說一句，你主辦單位有Google強?有蝦皮強?人家google總獎金15萬**美金**的比賽，也是看private給名次，誰她媽還會看報告阿，google只要你交的model確定能在該方的環境跑，就會給錢了，這個啦嘰aicup報告還20%，報告這種就最主觀了，主辦單位給誰就給誰，重點是報告中還有一些分數是比較**創新性**，創你阿嬤，標新立異很猛???，最好她用的方法是自己想的，或是2022年才剛發paper的，妳妹阿，新方法一定強那世界就很美好了，Swin Transfom是真的帥，但他打輸EfficientNet阿，sudo label很強對，但我Voting Ensemble的Accuracy就他媽比你高，今天這個是肺腺癌切割比賽，假設我說假設，我們的model被實際用於醫療(我知道當然不可能)，**我多你1%代表我100個人可以多救1人ㄟ**，會寫報告有啥用啦，幫患者寫遺產書????`，一直愛新的東西難怪台灣起不來，我就問你為啥一堆人愛聽老歌或說10年前的歌，明明現在國內外抖音每月歌都出那麼多!?
-->

## 2. NSPO - 2022年第二屆AI智能雲端運算應用競賽♉

- 隊名 : SuperNormal
- 主題方向 : Fintech
- 簡介 : 使用python中之第三方DTW函數庫，計算多種商品、大盤和加密貨幣的「時間序列相似度」，以觀察宏觀的現況。此外我們也計算大盤與個股間的時間序列相似度，來觀察大盤走勢向下時，走勢逆向上升的個股。
詳情請見[連結](https://github.com/JulianLee310514065/Complete-Project/tree/main/fintech_NSPO)。

 |Final Rank|
|--|
|第一|

## 3. fNIRS signal analysis (**Zheng, Yu-Han**)♊
* Data : 使用的是**宇翰學長的資料**，從最原始血氧濾波到模型分類結果，但因為資料帶有病歷號等個人隱私，故沒有放上github，此外葉克膜患者有分VA、VV，但因為程式差異不大，所以就使用VV做示範，VA再稍作改即可使用。
* 日期 : 202306
* 工具 : Python、scikit-learn
* 特色 : 此資料為下肢葉克膜的資料，其資料特點是**時間特長**一個人有長達50分鐘以上的資料，第二點是**有很多個階段**，這個在做階段相關的處理時會又有很大的差異，如階段平均差等。此外還用了[TDDR](https://www.sciencedirect.com/science/article/abs/pii/S1053811918308103?via%3Dihub)演算法來將peak雜訊消除。
