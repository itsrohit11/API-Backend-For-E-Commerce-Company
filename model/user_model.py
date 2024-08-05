import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host='localhost', database='flask_tutorial', user='root', password="rohit6113")
            self.con.autocommit=True
            self.cur=self.con
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
        
    # def user_add_model(self,data):
    #     self.cur.execute(f"INSERT INTO users(id, name, email, phone, role, password) VALUES('{data['id']}','{data['name']}','{data['gmail']}','{data['phone']}','{data['role']}','{data['password']}')")
    #     return "Data Added Successfully"
    
    def user_add_model(self,data):
        self.cur=self.con.cursor()
        print((data['name'],data['email'],data['phone'],data['role'],data['password']))
        self.cur.execute("INSERT INTO users( name, email, phone, role, password) VALUES(%s,%s,%s,%s,%s)",(data['name'],data['email'],data['phone'],data['role'],data['password']))
        return "Data Added Successfully"

