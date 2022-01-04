from .Event import *

event_cards = [
    StopActionEvent("衛生局稽查不合格，暫時停業觀察", "停止行動一回合"),
    AddTableEvent("獲得米其林美食報導，遊客蜂擁而至", "可在自已的攤位添加一張桌子"),
    EveryOneAlterMoneyIfOwnEvent("麵粉原物料上漲", "麵食類攤位的老闆損失 450 元（當歸麵線、切仔麵、牛肉麵、鱔魚麵）", [4, 8, 22, 31], 450),
    IdleKitchenEvent("被發現販賣隔夜商品，評價下滑", "下次經過自己的中央廚房時不得領取金錢或研發技術"),
    AlterMoneyNearestEvent("台北市舉行一年一度牛肉麵大賽", "最靠近牛肉麵攤位的玩家獲利 1200 元", 4, 1200),
    AlterMoneyNearestEvent("國外觀光客指定要喝珍珠奶茶", "最靠近珍珠奶茶的玩家獲利 750 元", 1, 750),
    AlterMoneyNearestEvent("毒奶風暴影響，人心惶恐", "最靠近木瓜牛奶的玩家損失 400 元", 16, 750),
    AlterMoneyEvent("低價促銷，生意大好", "獲利 1000 元", 1000),
    TransferMoneyToNextEvent("工讀生缺班，人手不足", "付 500 元給你的下一位玩家請他代班", 500),
    RandomAlterMoneyEvent("衝刺營業額，在人行道上擺攤", "隨機被警察抓罰 750 元或獲得額外收入 750 元", 750),
    AlterMoneyIfOwnEvent("魚類養殖技術突破", "如果你有鱔魚麵或蚵仔煎攤位獲利 1500 元，否則獲利 300 元", [8, 26], 1500, 300),
    AlterMoneyEvent("客人稱讚商品好吃，好康道相報", "獲利 600 元", 600),
    AlterMoneyEvent("媒體採訪報導，增加曝光度，知名度大增", "獲利 750 元", 750),
    AlterMoneyEvent("推出新菜色，大受好評", "獲利 1200 元", 1200),
    EveryOneAlterMoneyIfOwnEvent("適逢冬至，補冬商品熱賣", "薑母鴨和羊肉爐攤位的老闆獲得 500 元", [32, 35], 500),
    RaceGainOrRemoveTableEvent("都市更新提案發展，是否拆除違建", "和上一位玩家比，擁有較多攤位的人損失一張桌子，較少攤位的人獲利 700 元（平手則各獲得一半）", 700),
    FreeTableEvent("消費券效益，攤位座無虛席", "下次添加桌子時不用付建造費用"),
    RandomBuyStandEvent("金主投資，店面規模擴張", "可以隨機購買一個還沒有人購買的攤位"),
    EveryoneAlterMoneyEvent("經濟不景氣，營業額少三成", "所有玩家損失 500 元", -500),
    RandomBuyOthersStandEvent("經營連鎖通路", "可以隨機向別人購買一個沒有桌子或店面的攤位"),
    RemoveTableEvent("大廚被挖腳，老闆煩惱得憂鬱症", "隨機拆除一張自己的桌子"),
    AlterMoneyEvent("看錯食譜，味道嚴重走位", "損失 600 元", -600),
    AlterMoneyEvent("出國美食比賽榮獲優勝，新台灣之光", "獲利 1500 元", 1500),
    EveryoneTransferMoneyEvent("生意興隆，人們拿著大把鈔票要求加盟", "所有玩家給你 300 元", 300),
    AlterMoneyEvent("菜裡面有蟑螂屍體，顧客投訴", "損失 700 元", -700),
]


def make_event_cards():
    return event_cards
