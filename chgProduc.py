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
    id=form.getvalue('id')
    name=form.getvalue('name')
    intro=form.getvalue('intro')
    seller=form.getvalue('seller')
    price=form.getvalue('price')
    invenNum=form.getvalue('invenNum')
    id, outID = int(id), int(outID)
    osh.updProd(id,name,intro,seller,price,invenNum)
    print("訊息已更新!")
except:
    print("<h1>請正當輸入!</h1>")

print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")

