#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#main loader
import sys
import cgi
import onlineshop as osh

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()


headline = "<h1>這是商場的客戶端</h1>"
headline += "<hr><form method='post' action='add2Cart.py'>輸入要購買的商品編號: <input type='text' name='buyID'><br>"
headline += "輸入要購買的數量: <input type='text' name='buyNum'>&nbsp<input type='submit' value='確認'></form> <br>"
headline += f"<input type='button' onclick = 'getCart()' value='購物車'> <br>"#
headline += "<hr>"


shopList=osh.getShopList()#show shop list
shopTbl="<table><tr><th>商品編號</th><td>商品名稱</td><td>商品介紹</td><td>賣家</td><td>價格</td><td>存貨</td></tr>"#<td  width='90px'>購買數量</td>
for (id,name,intro,seller,price,invenNum) in shopList:
    shopTbl += f"<tr><th>{id}</th><td>{name}</td><td>{intro}</td><td>{seller}</td><td>{price}</td><td>{invenNum}</td>"
    #shopTbl += f"<td><div><form method='post' action=''> <input type='text' name='i'  size='1'>&nbsp<input type='submit'></form></form></td>"
shopTbl+="</table>"


cartList=osh.getCartList()#show cart list
ttlPrice = 0#總價
cartTbl="<table><tr><th>商品編號</th><td>商品名稱</td><td>商品介紹</td><td>賣家</td><td>價格</td><td>購買數量</td></tr>"#<td  width='90px'>購買數量</td>
for (id, name, intro, seller, price, buyNum) in cartList:
    cartTbl += f"<tr><th>{id}</th><td>{name}</td><td>{intro}</td><td>{seller}</td><td>{price}</td><td>{buyNum}</td></tr>"
    ttlPrice += price*buyNum
    #cartTbl += f"<td><div><form method='post' action=''> <input type='text' name='i'  size='1'>&nbsp<input type='submit'></form></form></td>"
cartTbl+=f"<tr ><td colspan=99><p align=right>共計：{ttlPrice}</p></td></tr></table></dialog>"
''''''


with open("mainUI.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"###tag1###",shopTbl.encode())
    st=st.replace(b"###title###",headline.encode())
    st=st.replace(b"###dialog###",cartTbl.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()