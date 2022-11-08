#連線DB
from dbConfig import conn, cur
def getShopList():#查詢整個商品列表
    sql="SELECT id, name, intro, seller, price, invenNum FROM `onlineshop` WHERE 1 order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def get1ShopList(id):#查詢該商品資訊
    sql="SELECT id, name, intro, seller, price, invenNum FROM `onlineshop` WHERE id=%s "
    cur.execute(sql, (id,))
    records = cur.fetchall()
    return records

def addProd(name,intro,seller,invenNum,price):#加入新商品
    sql="INSERT INTO `onlineshop`(`name`,`intro`,`seller`,`invenNum`,`price`) VALUES (%s,%s,%s,%s,%s)"
    cur.execute(sql, (name,intro,seller,invenNum,price))
    conn.commit()
    return True

def delProd(id):#刪除商品
    sql="delete from `onlineshop` where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def updProd(id,name,intro,seller,price,invenNum):#更改商品詳細資訊
    sql="UPDATE onlineshop SET name=%s, intro=%s, seller=%s, invenNum=%s, price=%s WHERE id=%s"
    cur.execute(sql, (name,intro,seller,price,invenNum,id))
    conn.commit()
    return True

def plusProdInvenNum(id,inNum):#加回商品存貨
    sql="UPDATE onlineshop SET invenNum=invenNum+%s WHERE id=%s"
    cur.execute(sql, (inNum,id))
    conn.commit()
    return True

def minusProdInvenNum(id,outNum):#減掉商品存貨
    sql="UPDATE onlineshop SET invenNum=invenNum-%s WHERE id=%s"
    cur.execute(sql, (outNum,id))
    conn.commit()
    return True

def checkout():#結帳
    sql="DELETE FROM cart WHERE 1"
    cur.execute(sql, ())
    conn.commit()
    return True


###cart

def getCartList():#查詢整個購物車列表
    sql="SELECT onlineshop.id, onlineshop.name, onlineshop.intro, onlineshop.seller, onlineshop.price, cart.buyNum FROM onlineshop,cart WHERE cart.prodID = onlineshop.id order by id asc"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def getCart1BuyNum(id):#查詢該商品購買數量
    sql="SELECT buyNum FROM cart WHERE prodID=%s"
    cur.execute(sql, (id,))
    records = cur.fetchall()
    return records

def add2Cart(id,buyNum):#新商品加入購物車
    sql="INSERT INTO cart (prodID, buyNum) VALUES (%s,%s)"
    cur.execute(sql, (id, buyNum))
    conn.commit()
    return True

def add2BuyNum_Cart(id,buyNum):#原商品加入購物車
    sql="UPDATE cart SET buyNum=buyNum+%s WHERE prodID=%s"
    cur.execute(sql, (buyNum, id))
    conn.commit()
    return True

def out2BuyNum_Cart(id,outNum):#商品拿出購物車
    sql="UPDATE cart SET buyNum=buyNum-%s WHERE prodID=%s"
    cur.execute(sql, (outNum, id))
    conn.commit()
    return True

def del2Cart(id):#商品全拿出購物車(刪除購買欄)
    sql="DELETE FROM cart WHERE prodID=%s"
    cur.execute(sql, ( id,))
    conn.commit()
    return True

'''
def delProdBtyBtn(btn):
    idBtn = btn.id
    sql="delete from `onlineshop` where id=%s;"
    cur.execute(sql,(idBtn,))
    conn.commit()
    return True
'''





