# 110-1-pws-final

## Get started

In the root directory, run:

```bash
$ python src/main.py
```
# 程式與網路資料蒐集 期末專題—美食大富翁

## 組員

* 數學四 萬俊彥
* 工管四 林威呈
* 工管四 劉信堂
* 農經二 周煒澔

### 專案發想

做為本門程式課的期末專案，考量大家的能力程時間分配，別於其他以應用程式為導向，我們選擇撰寫一款多人單機遊戲，以復古視覺包裝創新玩法

### 遊戲玩法

雖然名叫大富翁，但我們的遊戲以**經營**為主，玩家最後比拼的是桌數、攤位數與技能的分值相加。

![image](https://user-images.githubusercontent.com/94923725/178326112-df40e350-5129-4348-8ae7-7dfc0d66c84c.png)

### 介面視覺

初始介面以玩家人數導向2P、3P、4P的介面，而主介面則有地圖與攤位、玩家欄的資訊

![image](https://user-images.githubusercontent.com/94923725/178327191-6985639d-547b-4a79-809f-162170f13e6c.png)

![image](https://user-images.githubusercontent.com/94923725/178329682-58417bce-650b-4282-922b-d4d670302895.png)

### 使用套件

套件的部分，會用到**Pygame**和**tkinter**這兩個套件
Pygame用於遊戲的介面上，包含開始畫面、遊戲畫面、結算畫面; 而tkinter用於玩家資訊或是技能、狀態觸發的對話框顯示


### 程式架構

大架構參考MVC架構，但由於專案程式不會很大，透過頁面加以控制，因此我們將Controller合併到View之中
一共分為game、view、與util/(utility)三大部份

#### About game

game相當於MVC架構中的Model，儲存遊戲所有資料









