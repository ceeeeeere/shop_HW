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
id=form.getvalue('updID')
msgList = osh.get1ShopList(id)
target=""
for (id,name,intro,seller,price,invenNum) in msgList:
    target += f"<form method='post' action='chgProduc.py'>"
    target += f"賣家 : <input type='text' readonly unselectable='off' name='seller' value={seller} /><br>"
    target += f"商品編號 : <input type='text readonly unselectable='on' name='id' value={id} /><br>"
    target += f"商品名稱 : <input type='text' name='name' value={name} /><br>"
    target += f"商品價格 : <input type='text' name='price' value={price} /><br>"
    target += f"商品存貨 : <input type='text' name='invenNum' value={invenNum} /><br>"
    target += f"商品介紹 : <textarea  name='intro' >{intro}</textarea><br>"
    target += f"<input type='submit' value='修改'/><br></form>"
#print(id)
#print(msgList)

print(f'''
<h1>正在更改 {name}({id}號)的商品資訊</h1>
<hr>
''')
print(target)
print('''''')
