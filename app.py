from flask import Flask, request    
from model.user_model import user_model
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello world"

@app.route("/home")
def home():
    return "this is home page"

@app.route("/sales")
def payment():
    return "this is a payment gateway"

@app.route("/user/get")
def user_get_controller():
    obj = user_model()
    return obj.user_get_model()

@app.route("/user/add", methods=["POST"])
def user_add_controller():
    obj = user_model()
    print(request.method)
    print(request.form)
    result = obj.user_add_model(request.form)
    print(result)
    return result

# PUT CALL
@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    obj = user_model()
    return obj.user_update_model(request.form)

# DELETE CALL
@app.route("/user/delete/<product_id>", methods=["DELETE"])
def user_delete_controller(product_id):
    obj = user_model()
    return obj.user_delete_model(product_id)
    

if __name__ == "__main__":
    app.run(debug=True)