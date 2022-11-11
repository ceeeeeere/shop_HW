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
    form = cgi.FieldStorage()#接取資料
    id=form.getvalue('id')
    name=form.getvalue('name')
    intro=form.getvalue('intro')
    seller=form.getvalue('seller')
    price=form.getvalue('price')
    invenNum=form.getvalue('invenNum')
    price, invenNum = int(price), int(invenNum)
    if price < 0 or invenNum < 0:#價格或庫存不小於0才可更改資料，不然要求重新填寫
        print("<h1>價格或存貨數必須不小於0!</h1>")
        print("<br><form method='post' action='chgProdForm.py'>")
        print(f"<input type='hidden' name='updID' value='{id}'>")
        print("<input type='submit' value='重新填寫'/></form></a>")
    else :#更改商品詳細資訊
        osh.updProd(id,name,intro,seller,invenNum,price)
        print("<h1>訊息已更新!</h1>")
        ''''''
except:#轉整數失敗等同「價格及存貨數」非整數
    print("<h1>請正當輸入!</h1>")
#固定的回到主頁
print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")