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
id=form.getvalue('outID')
outNum=form.getvalue('outNum')#id,outNum = 2,60 
prodMsg = osh.get1ShopList(id)
cartMsg = osh.getCart1BuyNum(id)
cartNum = 0
for (i,) in cartMsg:#購物車內的數量
    if i != None:
        cartNum = i

outNum = int(outNum)
id = int(id)
'''
print(type(outNum))
print(type(cartNum))'''
for (id,name,intro,seller,price,invenNum) in prodMsg:#如果退貨數<=購車數 => 給退
    if outNum <= cartNum:#True
        if outNum == cartNum:#全退貨，刪除購買欄
            osh.del2Cart(id)
        else:#只減購買數
            osh.out2BuyNum_Cart(id,outNum);
        osh.plusProdInvenNum(id,outNum);#加回商品架
        print("<h1>商品已退貨!</h1>")
    else:
        print("<h1>退貨超過上限!</h1>")
    print("<div> 目前購物車的 %s 已有 %d</div>" %(name,cartNum-outNum))

#print(prodMsg)print(cartNum)
print("<br><a href='index_client.py'>回主選單</a>")
print("</body></html>")

