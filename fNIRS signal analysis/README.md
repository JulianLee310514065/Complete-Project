# fNIRS signal analysis

------
# .ipynb file name explain 💹

1. Filter.ipynb  -> from origin data to filtered data，使用**四階butterworth**，截止頻率為**0.12**，output存成.csv
2. Extraction.ipynb -> Write extraction function，讓Get_Feature使用，使用了**約十種**特徵萃取方法
3. Get_Feature.ipynb -> Get Feature from all people， and output to excel
4. Model_and_Train -> Use three(four) pair of **feature selection and model**，and calculate the accuracy and ROC


# data file name explain 🔰

1. label.xlsx -> content label
2. VFT folder -> content **origin blood oxygen concentration data**
