from .Tech import *

def make_tech_cards():
    return [
        DoubleTableTech(4, "建立中央廚房SOP流程，確保食物品質", "每次添加桌子時可以一次添加兩張"),
        # 400 重新擲骰
        SameSpotFeeTech(6, "併購垂直廠商，直接掌握食材來源", "和你站在同一格的玩家要付你 400 元", 400),
        ExtraIncomeTech(6, "請公關公司打造食品形象，傳統美食全新感受", "經過自家起點時可以多領 500 元", 500),
        # 500 多前進一步
        # 停在他人起點時自己添加桌子
        ReverseVisitKitchenTech(5, "受媒體採訪聲名遠播", "參觀他人中央廚房時免參觀費，還可以收取 200 元宣傳費"),
        # 450 少前進一步
        # 可重抽經營卡
        ExtraStandFeeTech(5, "開發生機市場，使用環保材質提升價值", "每次收取攤位餐飲費可多收 200 元", 200),
        SameSpotFeeTech(5, "主廚受邀上電視，開闢美食帶狀節目", "和你站在同一格的玩家要付你 600 元", 600),
        StandFeeDiscountTech(5, "國民票選榮獲台灣代表小吃殊榮", "走到他人攤位時對方餐飲費少收 200 元", 200),
        TableDiscountTech(4, "開放加盟體系", "每次添加桌子可少付 200 元", 200)
    ]
