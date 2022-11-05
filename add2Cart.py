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
''''''
print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()
'''
#查詢
form = cgi.FieldStorage()
id=form.getvalue('id')
buyNum=form.getvalue('num')
osh.add2Cart(id,buyNum)


print("商品已上架!")
print("<br><a href='index_client.py'>回商店街</a>")
print("</body></html>")
'''
with open("add2CartForm.html",'rb') as fp:
    st=fp.read()
    #st=st.replace(b"###tag1###",shopTbl.encode())
    #st=st.replace(b"###title###",headline.encode())
    #st=st.replace(b"###dialog###",cartTbl.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()