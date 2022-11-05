#連線DB
from dbConfig import conn, cur
def getShopList():
    #查詢
    sql="SELECT id, name, intro, seller, price, invenNum FROM `onlineshop` WHERE 1 order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def get1ShopList(id):
    #查詢
    sql="SELECT id, name, intro, seller, price, invenNum FROM `onlineshop` WHERE id=%s "
    cur.execute(sql, (id,))
    records = cur.fetchall()
    return records

def addProd(name,intro,seller,invenNum,price):
    sql="INSERT INTO `onlineshop`(`name`,`intro`,`seller`,`invenNum`,`price`) VALUES (%s,%s,%s,%s,%s)"
    cur.execute(sql, (name,intro,seller,invenNum,price))
    conn.commit()
    return False

def delProd(id):
    sql="delete from `onlineshop` where id=%s;"
    cur.execute(sql,(id,))
    conn.commit()
    return True

def updProd(id,name,intro,seller,price,invenNum):
    sql="UPDATE onlineshop SET name=%s, intro=%s, seller=%s, invenNum=%s, price=%s WHERE id=%s"
    cur.execute(sql, (name,intro,seller,price,invenNum,id))
    conn.commit()
    return False
    
def updProdInvenNum(id,inNum):
    sql="UPDATE onlineshop SET invenNum=invenNum+%s WHERE id=%s"
    cur.execute(sql, (inNum,id))
    conn.commit()
    return False


def getCartList():
    #查詢
    sql="SELECT onlineshop.id, onlineshop.name, onlineshop.intro, onlineshop.seller, onlineshop.price, cart.buyNum FROM onlineshop,cart WHERE cart.prodID = onlineshop.id order by id asc"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    

def add2Cart(id,buyNum):
    sql="INSERT INTO cart (id, buyNum) VALUES (%s,%s)"
    cur.execute(sql, (id, buyNum))
    conn.commit()
    return False

'''
def delProdBtyBtn(btn):
    idBtn = btn.id
    sql="delete from `onlineshop` where id=%s;"
    cur.execute(sql,(idBtn,))
    conn.commit()
    return True
'''





