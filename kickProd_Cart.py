#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import onlineshop as osh
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")
try:
    form = cgi.FieldStorage()#查詢
    id=form.getvalue('inID')
    inNum = 0;#購買數量初始化
    buyinMsg = osh.getCart1BuyNum(id)#查詢該商品在購物車的數量
    for(i,) in buyinMsg:#並用於此
        inNum = i;
    if i != None:
        osh.plusProdInvenNum(id,inNum)#加回商品
        osh.del2Cart(id)#全退貨，刪除購買欄
        print("<h1>商品已全數退回!</h1>")
    else:#購物車內找不到商品
        print("<h1>購物車內無此商品!</h1>")
except:#購物車內找不到商品
    print("<h1>購物車內找不到此商品!</h1>")
#固定的回到主頁
print("<br><a href='index_client.py'>回到主頁</a>")
print("</body></html>")