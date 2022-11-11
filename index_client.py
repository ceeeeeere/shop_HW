#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#main loader
import sys
import cgi
import onlineshop as osh

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

title="Client.buy"#title
#標頭和功能模組
headline = "<h1>這是商場的客戶端</h1><hr>"
headline += "<form method='post' action='add2Cart.py'>購買 : <input type='text' name='buyID' placeholder='在此輸入商品編號'>&nbsp&nbsp"
headline += "數量 : <input type='number' name='buyNum' placeholder='在此輸入購買數量'>&nbsp<input type='submit' value='確認'></form> <br>"
headline += "<form method='post' action='out2Cart.py'>退貨 : <input type='text' name='outID' placeholder='在此輸入商品編號'>&nbsp&nbsp"
headline += "數量 : <input type='number' name='outNum' placeholder='在此輸入退貨數量'>&nbsp<input type='submit' value='確認'></form> <br>"
headline += f"<input type='button' onclick = 'getCart()' value='購物車'> <br>"#
headline += "<hr>"


shopList=osh.getShopList()#show shop list
shopTbl="<table><tr><th>商品編號</th><td>商品名稱</td><td>商品介紹</td><td>賣家</td><td>價格</td><td>存貨</td></tr>"#<td  width='90px'>購買數量</td>
for (id,name,intro,seller,invenNum,price) in shopList:
    shopTbl += f"<tr><th>{id}</th><td>{name}</td><td>{intro}</td><td>{seller}</td><td>{price}</td><td>{invenNum}</td>"
    #shopTbl += f"<td><div><form method='post' action=''> <input type='text' name='i'  size='1'>&nbsp<input type='submit'></form></form></td>"
shopTbl+="</table>"

#建構購物車的 list
cartList=osh.getCartList()
ttlPrice = 0#總價
cartTbl="<form method='post' action='kickProd_Cart.py'>全部退貨<input type='text' name='inID' placeholder='在此輸入商品編號'>&nbsp<input type='submit' value='全部退貨'></form>"
cartTbl+="<table><tr><th>商品編號</th><td>商品名稱</td><td>商品介紹</td><td>賣家</td><td>價格</td><td>購買數量</td></tr>"#<td  width='90px'>購買數量</td>
for (id, name, intro, seller, price, buyNum) in cartList:
    cartTbl += f"<tr><th>{id}</th><td>{name}</td><td>{intro}</td><td>{seller}</td><td>{price}</td><td>{buyNum}</td></tr>"
    ttlPrice += price*buyNum
    #cartTbl += f"<td><div><form method='post' action=''> <input type='text' name='i'  size='1'>&nbsp<input type='submit'></form></form></td>"
cartTbl+=f"<tr ><td colspan=99><p align=right>共計：{ttlPrice}</p></td></tr></table>"#總價
cartTbl+="<div align=right><form method='post' action='chkOutCart.py'><input type='submit' value='結帳'></form></div>"
''''''


with open("mainUI.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"###title###",title.encode())#title
    st=st.replace(b"###headline###",headline.encode())#標頭和功能模組
    st=st.replace(b"###tag1###",shopTbl.encode())#商場詳細
    st=st.replace(b"###dialog###",cartTbl.encode())#購物車
    sys.stdout.buffer.write(st)
sys.stdout.flush()