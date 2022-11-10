#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import onlineshop as osh

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
sys.stdout.flush()
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")
#查詢
try:
    form = cgi.FieldStorage()#抓取資料
    id=form.getvalue('buyID')
    buyNum=form.getvalue('buyNum')#id,buyNum = 2,20
    buyNum, id= int(buyNum),int(id)#轉整數，方便判斷
    prodMsg = osh.get1ShopList(id)#查詢該商品資訊

    if buyNum > 0:#購買數恆正數
        if prodMsg:#如果找到商品
            cartMsg = osh.getCart1BuyNum(id)
            cartNum = 0
            for (i,) in cartMsg:#購物車內的數量
                if i != None:
                    cartNum = i
            for (id,name,intro,seller,price,invenNum) in prodMsg:
                if invenNum > 0:#商品還有存貨
                    if buyNum > invenNum:#超買，取庫存值，修改購買數量
                        buyNum = invenNum
                    if cartNum > 0:
                        osh.add2BuyNum_Cart(id,buyNum)
                    else:
                        osh.add2Cart(id,buyNum)#新商品加入購物車
                    osh.minusProdInvenNum(id,buyNum)#減掉商品存貨
                    print("<h1>已購買商品!</h1><div> 已購買 %d個%s </div>"%(buyNum,name))
                    print("<div> 目前購物車的「%s」已有 %d件</div>" %(name,cartNum+buyNum))
                else :#差買，直接報錯
                    print("<h1>商品已售罄!</h1>")
        else:
            print("<h1>商場內找不到該商品!</h1>")
    elif buyNum == 0:
        print("<h1>請確實購物!</h1>")
    else:
        print("<h1>請正確輸入!</h1>")
        print("<br>又不是不給你退換商品......")
except:#轉整數失敗等同「id和購買數」並非整數
    print("<h1>請正當輸入!</h1>")
#固定的回到主頁
print("<br><a href='index_client.py'>回主選單</a>")
print("</body></html>")

