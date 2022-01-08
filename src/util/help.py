import webbrowser

from .Dialog import confirm, yesno

def help():
    result = yesno('開啟網頁版說明書', '即將在瀏覽器開啟網頁版說明書，是否繼續?')
    if result:
        webbrowser.open('https://i.imgur.com/od97sfg.jpg')