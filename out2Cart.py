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

try:
    form = cgi.FieldStorage()#查詢
    id=form.getvalue('outID')
    outNum=form.getvalue('outNum')#id,outNum = 2,60 
    outNum, id = int(outNum), int(id)#轉成整數，方便控制
    cartMsg = osh.getCart1BuyNum(id)

    if outNum > 0:#避免負數
        if cartMsg:#有找到該商品
            prodMsg = osh.get1ShopList(id)
            for (i,) in cartMsg:#購物車內的數量
                cartNum = i
            for (id,name,intro,seller,price,invenNum) in prodMsg:
                if outNum >= cartNum:#全退貨(超退(取購物車值)視為全退貨)
                    outNum = cartNum
                    osh.del2Cart(id)#刪除購買欄
                else:#部分退貨，只減購買數
                    osh.out2BuyNum_Cart(id,outNum);
                osh.plusProdInvenNum(id,outNum);#加回商品架
                print("<h1>商品已退貨!</h1><div>  已退了 %d個%s </div>"%(outNum,name))
                print("<div> 目前購物車的 %s 已有 %d 個</div>" %(name,cartNum-outNum))
        else:
            print("<h1>購物車沒有此商品!</h1>")
    elif outNum == 0:
        print("<h1>請確實退貨</h1>")
    else:
        print("<h1>請正確輸入!</h1>")
        print("<br>又不是不讓你用消費買賣......")
except:
    print("<h1>請正當輸入!</h1>")

print("<br><a href='index_client.py'>回主選單</a>")
print("</body></html>")