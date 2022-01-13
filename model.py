import pymysql
from views import *

class EarthJoyModel:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.connection=None
        try:
            self.connection=pymysql.connect(host=self.host, user=self.user,password=self.password,database=self.database)
        except Exception as e:
            print("There is error in connection",str(e))

    def __del__(self):
        if self.connection!=None:
            self.connection.close()
            
            
    def getSellers(self, status):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select seller.*, admin.adminName from seller, admin where AppStatus = %s and seller.adminId = admin.adminId"
                args = (status)
                cursor.execute(query, args)
                check = cursor.fetchall()
                return check
        except Exception as e:
            print("Error in getSellers()", e)


    def getProducts(self, status):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select pName, pImages, pType, pCategory, pDescription, pPrice, pStock, pMainTag, seller.sellerName, seller.sellerCategory, seller.sellerEmail, seller.sellerPic from products, seller where seller.sellerId = products.sellerId and pAppStatus = %s"
                args = (status)
                cursor.execute(query, args)
                check = cursor.fetchall()
                return check
        except Exception as e:
            print("Error in getProducts()", e)
