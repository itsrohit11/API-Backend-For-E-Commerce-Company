import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost', database='flask_tutorial', user='root', password="rohit6113")
            self.con.autocommit=True
            self.cur=self.con.cursor()
            print("connection successful")
        except:
            print("connection failed")
    def user_get_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            return json.dumps(result)
        else:
            return "no data available"
    
    def user_add_model(self,data):
        self.cur=self.con.cursor()
        print(data['product_name'],data['product_category'],data['product_description'],data['product_price'])
        self.cur.execute("INSERT INTO users( product_name, product_category, product_description, product_price) VALUES(%s,%s,%s,%s)",(data['product_name'],data['product_category'],data['product_description'],data['product_price']))
        return "Data Added Successfully"
    

    # # PUT QUERY
    # def product_update_model(self, data):
    #     self.cur.execute(f"UPDATE product SET product_product_name='{data['product_product_name']}',product_category='{data['product_category']}= product_description='{data['product_description']}',product_price='{data['product_price']}'' WHERE id ={data['id']} ")
    #     if self.cur.rowcount>0:
    #         return {"meassage":"Product Updated Successfully"}
    #     else:
    #         return {"meassage":"Product Not Found"}
        
    # # DELETE QUERY
    # def product_delete_model(self, id):
    #     self.cur.execute(f"DELETE FROM product WHERE id={id}")
    #     if self.cur.rowcount>0:
    #         return {"meassage":"Product Deleted Successfully"}
    #     else:
    #         return {"meassage":"Product Not Found"}

