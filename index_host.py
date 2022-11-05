#!C:\Users\User\AppData\Local\Programs\Python\Python38\python.exe
#main loader
import sys
import cgi
import onlineshop as osh

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

headline = "<h1>這是商場的管理端</h1>新增商品：<a href='addProducForm.html'> 我要販售 </a>"
headline += "<hr><form method='post' action='delProduc.py'>輸入要刪除的號碼 : <input type='text' name='delID' required='required'>&nbsp<input type='submit' value='執行'></form> <br>"
headline += "<form method='post' action='chgProdForm.py'>輸入要變更詳細資料的號碼 : <input type='text' name='updID' required='required'>&nbsp<input type='submit' value='執行'></form>"
headline += "<form method='post' action='inProduc.py'>輸入要入庫的號碼 : <input type='text' name='inID' required='required'>入庫數量 : <input type='text' name='inNum' required='required'>&nbsp<input type='submit' value='執行'></form>"
headline += "<hr>"
dialog =""
msgList=osh.getShopList()

target="<table><tr><th>商品編號</th><td>商品名稱</td><td>商品介紹</td><td>賣家</td><td>價格</td><td>存貨</td> "
#<td>刪除ID</td><td>修改ID</td></tr>
for (id,name,intro,seller,price,invenNum) in msgList:
    target += f"<tr><th>{id}</th><td>{name}</td><td>{intro}</td><td>{seller}</td><td>{price}</td><td>{invenNum}</td>"
    #target += f"<td width='60px'><div><form method='post' action='delProduc.py'><input type='submit' name='i' value={id} /></form></td>"
    #target += f"<td width='60px'><input type='button' value='修改'/></div></td></tr>"
target+="</table>"

with open("mainUI.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"###title###",headline.encode())
    st=st.replace(b"###tag1###",target.encode())
    st=st.replace(b"###dialog###",dialog.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()