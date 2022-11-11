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
    name=form.getvalue('name')
    intro=form.getvalue('intro')
    seller=form.getvalue('seller')
    price=form.getvalue('price')
    invenNum=form.getvalue('invenNum')
    price, invenNum = int(price),int(invenNum)#轉整數，方便判斷
    if price < 0 and invenNum < 0:#價格不小於0才可更改資料，不然要求重新填寫
        print("<h1>價格和存貨數必須不小於於0!</h1>")
        print("<br><a href='addProducForm.html'>重新填寫</a>")
    else :#加入新商品
        osh.addProd(name,intro,seller,invenNum,price)
        print("<h1>商品已上架!</h1>")

except:#轉整數失敗等同 價格及存貨數 非整數
    print("<h1>請正當輸入!</h1>")
    print("<br><a href='addProducForm.html'>重新填寫</a>")
#固定的回到主頁
print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")
