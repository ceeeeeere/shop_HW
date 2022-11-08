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
    id=form.getvalue('outID')
    outNum=form.getvalue('outNum')
    id, outID = int(id), int(outNum)
    if osh.get1ShopList(id):#查詢該商品資訊
        if outID > 0:
            osh.minusProdInvenNum(id,outNum)
            print("<h1>商品已搬回!</h1>")
            print("<br>共搬出了%s 個 商品<br>"%(outNum))
        else:
            print("<h1>請正確輸入!</h1>")
            print("<br>又不是不給你用進貨功能......")
except:
    print("<h1>請正當輸入!</h1>")

print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")