# from flask import jsonify
from itertools import product
import mysql.connector
import json
class user_model():
    # DATABASE CONNECTIVITY
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost', database='flask_tutorial', user='root', password="rohit6113")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("connection failed")
    
    # GET CALL 
    def user_get_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            print(result)
            # return json.dumps(result)
            return{"payload":result}
        else:
            return "no data available"
        
    # GET CALL FOR SPECIFIC ID
    def user_getid_model(self,product_id):
        self.cur.execute("SELECT * FROM users WHERE product_id = " + str(product_id))
        result = self.cur.fetchall()
        if len(result) > 0:
            print(result)
            # return json.dumps(result)
            return{"payload":result}
        else:
            return "no data available"
    
    # POST CALL
    def user_add_model(self,data):
        self.cur=self.con.cursor()
        print(data['product_name'],data['product_category'],data['product_description'],data['product_price'])
        self.cur.execute("INSERT INTO users( product_name, product_category, product_description, product_price) VALUES(%s,%s,%s,%s)",(data['product_name'],data['product_category'],data['product_description'],data['product_price']))
        return "Data Added Successfully"
    

    # PUT QUERY
    def user_update_model(self,data):
        self.cur=self.con.cursor()
        self.cur.execute(f"UPDATE users SET product_name='{data['product_name']}',product_category='{data['product_category']}',product_description='{data['product_description']}', product_price='{data['product_price']}' WHERE product_id={data['product_id']}" ) 
        if self.cur.rowcount>0:
            return "Data Updated Successfully"
        else:
            return "Invalid Updation"
        
    # DELETE QUERY
    def user_delete_model(self,id):
        self.cur=self.con.cursor()
        self.cur.execute(f"DELETE FROM users WHERE product_id={id}") 
        if self.cur.rowcount>0:
            return "Data Deleted Successfully"
        else:
            return "No Data available"

        
    
    

