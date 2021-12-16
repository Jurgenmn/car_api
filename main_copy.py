from flask import Flask, request, jsonify

app = Flask(__name__)

cars = [
    {"id": 1, "brand": "audi", "model": "A4"},
    {"id": 2, "brand": "mercedes", "model": "S-class"},
    {"id": 3, "brand": "mercedes", "model": "E-class"},
    {"id": 4, "brand": "mercedes", "model": "A-class"},
    {"id": 5, "brand": "bmw", "model": "x-5"},
    {"id": 6, "brand": "bmw", "model": "x-7"}
]

# You can handle multiple http methods (GET, POST, PUT) in one function
# or you can do it separatly


@app.route("/cars", methods=["GET", "POST"])
def handle_cars():
    if request.method == "GET":
        return jsonify(cars)
    elif request.method == "POST":
        id = len(cars) + 1
        car = {"id": id}
        car["brand"] = request.json["brand"]
        car["model"] = request.json["model"]
        cars.append(car)
        return jsonify(car)


# @app.route("/cars")
# def retrive_all_cars():
#     return jsonify(cars)


@app.route("/cars/<int:id>", methods=["GET"])
def retrive_car(id):
    for car in cars:
        if car["id"] == id:
            return jsonify(car)

    return (jsonify({"error": "resource not found"}), 404)


# @app.route("/cars", methods=["POST"])
# def create_car():
#     id = len(cars) + 1
#     car = {"id": id}
#     car["brand"] = request.json["brand"]
#     car["model"] = request.json["model"]
#     cars.append(car)
#     return jsonify(car)


@app.route("/cars/<int:id>", methods=["DELETE"])
def delete_car(id):
    car = None
    for i in range(len(cars)):
        if cars[i]["id"] == id:
            car = cars.pop(i)
            break
    if car == None:
        return (jsonify({"error": "resource not found"}), 404)
    return jsonify(car)


# @app.route("/cars/<int:id>", methods=["PUT"])
# def update_car(id):
#     for i in range(len(cars)):
#         if cars[i]["id"] == id:
#             cars[i]["brand"] = request.json["brand"]
#             cars[i]["model"] = request.json["model"]
#             return jsonify(cars(i))
#     return (jsonify({"error": "resource not found"}), 404)


@app.route("/cars/<int:id>", methods=["PUT"])
def update_car(id):
    for car in cars:
        if car["id"] == id:
            car["brand"] = request.json["brand"]
            car["model"] = request.json["model"]
            return jsonify(car)
    return (jsonify({"error": "resource not found"}), 404)


app.run("localhost", 3000, debug=True)

# API is a web server that returns json data and mos API's follow
# the REST API standarts(rules)
