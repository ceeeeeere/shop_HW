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
    inNum=form.getvalue('inNum')
    id, inNum = int(id), int(inNum)
    if osh.get1ShopList(id):#查詢該商品資訊
        if inNum > 0:
            osh.plusProdInvenNum(id,inNum)
            print("<h1>商品已進貨!</h1>")
            print("<br>共進貨了%s 個 商品<br>"%(inNum))
        else:
            print("<h1>請正確輸入!</h1>")
            print("<br>又不是不給你用減貨功能......")
    else:
        print("<h1>找不到商品，是否創建?</h1>")
        print("<br><a href='addProducForm.html'>創建新商品</a>&nbsp&nbsp")
except:
    print("<h1>請正當輸入!</h1><br>")

print("<br><a href='index_host.py'>回到主頁</a>")
print("</body></html>")