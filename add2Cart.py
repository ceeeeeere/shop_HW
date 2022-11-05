import cgi
import onlineshop as osh
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
''''''
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

#查詢
form = cgi.FieldStorage()
id=form.getvalue('id')
buyNum=form.getvalue('num')
osh.add2Cart(id,buyNum)

''''''
print("商品已上架!")
print("<br><a href='index_client.py'>回商店街</a>")
print("</body></html>")