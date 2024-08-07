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

# # PUT CALL
# @app.route("/product/update", methods=["PUT"])
# def product_update_controller():
#     obj = product_model()
#     return obj.product_update_model(request.form)

# # DELETE CALL
# @app.route("/product/delete/<id>", methods=["DELETE"])
# def product_delete_controller(id):
#     obj = product_model()
#     return obj.product_delete_model(id)
    

if __name__ == "__main__":
    app.run(debug=True)