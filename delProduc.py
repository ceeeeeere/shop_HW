#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import onlineshop as osh

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
    id=form.getvalue('delID')
    id = int(id)#轉整數，方便判斷
    if osh.get1ShopList(id) and id != None :#找到商品，刪掉
        osh.delProd(id)
        print(f"<h1>{id}號商品已刪除!</h1>")
    else:#查無此商品
        print("<h1>查無此商品!</h1>")
except:#轉整數失敗等同「id」並非整數
    print("<h1>請正當輸入!</h1>")
#固定的回到主頁
print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")

