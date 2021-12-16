from flask import Flask
from flask import request, jsonify  # Jsonfy converts python data into json data

app = Flask(__name__)


@app.route("/me.html")
def me():
    handler = open("me.html", "r")
    return handler.read()


@app.route("/user/<string:user_name>")
def user(user_name):
    print("Hello " + user_name)
    return "Hello " + user_name + "\n"


@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    sum = num1 + num2
    return str(sum) + "\n"


@app.route("/search")
def search():
    cars = [
        {"brand": "audi", "model": "A4"},
        {"brand": "mercedes", "model": "S-class"},
        {"brand": "mercedes", "model": "E-class"},
        {"brand": "mercedes", "model": "A-class"},
        {"brand": "bmw", "model": "x-5"},
        {"brand": "bmw", "model": "x-7"}
    ]

    if "car_brand" in request.args:
        car = request.args["car_brand"]
        requested_brand = []
        for i in cars:
            if i["brand"] == car:
                requested_brand.append(i)
        return jsonify(requested_brand)
    else:
        return jsonify(cars)

    # for i in request.args:
    #     print(i, request.args[i])
    # return str(cars)


app.run("localhost", 3000, debug=True)
