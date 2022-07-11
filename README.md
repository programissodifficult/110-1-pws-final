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

![image](https://user-images.githubusercontent.com/94923725/178350819-7d051f3c-0a06-4f24-9b4b-58578643ecd0.png)


### 介面視覺

初始介面以玩家人數導向2P、3P、4P的介面，而主介面則有地圖與攤位、玩家欄的資訊

![image](https://user-images.githubusercontent.com/94923725/178351089-601c643b-7b06-4050-83d3-ea8212365fa1.png)
![image](https://user-images.githubusercontent.com/94923725/178351615-13f4544a-2b40-4b39-a87b-72c7974840b4.png)
### 使用套件

套件的部分，會用到**Pygame**和**tkinter**這兩個套件
Pygame用於遊戲的介面上，包含開始畫面、遊戲畫面、結算畫面; 而tkinter用於玩家資訊或是技能、狀態觸發的對話框顯示


### 程式架構

大架構參考MVC架構，但由於專案程式不會很大，透過頁面加以控制，因此我們將Controller合併到View之中
一共分為game、view、與util/(utility)三大部份

#### About game

game相當於MVC架構中的Model，儲存遊戲所有資料，其中有五種Class分別對應各自的物件 
例如Player對應玩家，grid對應到地圖的格子，tech對應角色抽到的技能，Event則是遊戲中事件，Character對應角色
若有跨Class的動作，例如A玩家(Player)抽到甲技能（tech）則會統一歸到game.py執行

#### About View

View相當於MVC架構中view，根據遊戲過程進行畫面呈現。由於Pygame提供的功能較侷限，因此另建Component-based-system與Scene system管理遊戲畫面

##### Component-based-system
將遊戲畫面分成不同小元件各自管理，其中函數包括init, update, render, handle_events
-init:建立每個元件會用到的基本元素
-update:畫面更新前執行，元件是否需根據遊戲資料調整
-render:控制元件如何顯示
-handle_events:控制是否需要根據玩家的動作而觸發特定反應
-舉例:
![image](https://user-images.githubusercontent.com/94923725/178355769-0a684cba-7b16-402f-9614-030838bb2cea.png)
右圖為一個攤位格子（元件）其中包含原本的框線，被玩家擁有後的框線、圖示、背景顏色、名稱文字等（基本元素）

##### Scene system
在主畫面中可以切面不同部份，例如擲骰按鈕、玩家欄、代表玩家的點點等
例如在Game Scene中即規劃背景、說明按鈕、玩家、計分板等
因此在設定畫面只需要決定有什麼樣的元件，關於元件本身的變化就不在此處處理
![image](https://user-images.githubusercontent.com/94923725/178357009-32d5d4d2-8a4a-475b-ae38-1a29328a26c4.png)

#### About Util/

Utility則是提供通用的工具，例如對話框、開啟說明書等

### 展望

未來希望加入遊戲存檔功能與動化上的優化








