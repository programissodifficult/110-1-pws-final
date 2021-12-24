from .Event import *

event_cards = [
    StopActionEvent("衛生局稽查不合格，暫時停業觀察", "停止行動一回合"),
    AddTableEvent("獲得米其林美食報導，遊客蜂擁而至", "可在自已的攤位免費添加一張桌子"),
    EveryOneLoseMoneyIfOwnEvent("麵粉原物料上漲", "麵食類攤位的老闆損失 450 元（當歸麵線、切仔麵、牛肉麵、鱔魚麵）", [4, 8, 22, 31], 450),
    IdleKitchenEvent("被發現販賣隔夜商品，評價下滑", "下次經過自己的中央廚房時不得領取金錢或研發技術"),
    GainMoneyNearestEvent("台北市舉行一年一度牛肉麵大賽", "最靠近牛肉麵攤位的玩家獲利 1200 元", 4, 1200)
]


def make_event_cards():
    return event_cards
