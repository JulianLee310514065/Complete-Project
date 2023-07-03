# Train 全過程 - Pytorch - Segmentation

###  1. train data list/ test list
放置資料於 list

###  2. split data to train and val
我是分 80%-20%

###  3. Transform (Use monai)⭐
本步驟難店在於，transform 必須同時運作於train_img and seg_img，且**transform有順序**，使用monai可以方便處理 \
有使用: `LoadImage`, `ScaleIntensity`, `As Channel First`, `AddChannel`, `Resize or RandomCrop`

###  4. Create dataset
dataset為torch特有資料型態，作用就如其名，且可以放在dataloader

###  5. Create dataloader
dataloader 可以批量的讀取資料，自動做成一包包，且為generator形式，可以省空間，需要時讀出來，dataloader用torch本身的即可

###  6. Build or Get Model(Use monai, timm, smp)⭐⭐⭐
build a amazion model

###  7. Define the loss function and optimizer (and also lr_schedule)⭐
loss: 評斷model好壞 \
optimizer : 優化模型，Learning Rate超級重要⭐⭐ \
lr_schedule : 讓lr有規律的上下移動

###  8. Train
`model.train`，用for 去train，要自己寫，重點在`loss.step` 與`lr_schedule.step`

###  9. val (test)
`model.val`，用for 去val，若train時候有resize，val時必須先resize成相同大小，predict完再resize回來 \
可使用 monai `monai.inferers.sliding_window_inference`

### 10. ensemble
將圖片 相加取平均，使用`np.round()`，使超過半數選的點為 1 ，反之為 0

---
### 放張人權圖

![第四](https://user-images.githubusercontent.com/101493861/171457796-97f6d0d4-d8d9-4a92-a25e-b645e2804d1d.png)

![team1015](https://user-images.githubusercontent.com/101493861/171458210-fccb2796-06d6-4fc8-ac99-04f8894f8848.png)



