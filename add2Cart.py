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
form = cgi.FieldStorage()
id=form.getvalue('buyID')
buyNum=form.getvalue('buyNum')#id,buyNum = 2,20
prodMsg = osh.get1ShopList(id)
cartMsg = osh.getCart1BuyNum(id)
cartNum = 0
for (i,) in cartMsg:#購物車內的數量
    if i != None:
        cartNum = i

buyNum = int(buyNum)
id = int(id)
''''''
for (id,name,intro,seller,price,invenNum) in prodMsg:#如果購買數+購車數<=庫存數 => 給買
    if buyNum <= invenNum:#購買數<=庫存
        if cartNum > 0:#修改購買數量
            osh.add2BuyNum_Cart(id,buyNum)
        else:
            osh.add2Cart(id,buyNum)
        osh.minusProdInvenNum(id,buyNum)
        print("<h1>已購買商品!</h1>")#數量 : %d %(buyNum)
    else:
        print("<h1>購買超過上限!</h1>")
    print("<div> 目前購物車 %s 已有 %d</div>" %(name,cartNum+buyNum))

print("<br><a href='index_client.py'>回主選單</a>")
print("</body></html>")

