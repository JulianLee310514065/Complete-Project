# 題目： 如何用 DTW 在市場趨勢下時逆向獲利

> 本Jupyter Notebook分兩部分，前半部為市場指標的研究與分析，後半部是英雄股的研究與分析

---
- 隊名 : SuperNormal
- 主題方向 : Fintech
- 簡介 : 使用python中之第三方DTW函數庫，計算多種商品、大盤和加密貨幣的「時間序列相似度」，以觀察宏觀的現況。此外我們也計算大盤與個股間的時間序列相似度，來觀察大盤走勢向下時，走勢逆向上升的個股。
---
# Leaderboard
|Rank|
|-|
1

### 1. 市場指標 - DTW熱力圖、不同時長周期的DTW值、DTW趨勢圖
```
<市場指標> 假設 一天交易時數 6小時

時間軸：

一年(2days)    5*52/2=130 

半年(1day)     22*6=132

三個月(3hrs)   2*22*3=132

一個月(1hrs)   6*22=132

一週（15mins)  4*6*5=120
```
### 2. 英雄股
```
<英雄股> 假設 一天交易時數 6小時

時間軸：

一天 (3mins)  （120） 

三天 (10mins) （108）

一週 (15mins) （120）
```

### 3. 名次 - 第一名
![第一](https://raw.githubusercontent.com/JulianLee310514065/Complete-Project/main/fintech_NSPO/photo1665678525.jpeg)


### 4. 完整文檔
[文檔連結](http://18.178.46.40/info/detail.php?pid=11)

