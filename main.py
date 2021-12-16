from flask import Flask, request, jsonify
import psycopg2
import utils

conn = psycopg2.connect(  # connection object
    host="localhost", database="cars_api", user='jay', password="password")

cur = conn.cursor()

app = Flask(__name__)


# You can handle multiple http methods (GET, POST, PUT) in one function
# or you can do it separatly

@app.route("/cars")
def retrive_all_cars():
    result = []
    # You get back a list of tuples but tuples are not valid json values so we have to convert to a dict
    cur.execute("SELECT * FROM cars")
    records = cur.fetchall()
    for car in records:
        obj = {"id": car[0], "brand": car[1], "model": car[2]}
        result.append(obj)

    return jsonify(result)


@app.route("/cars/<int:id>", methods=["GET"])
def retrive_car(id):
    car = utils.get(cur, id)
    if car == None:
        return (jsonify({"error": "resource not found"}), 404)

    return jsonify(car)


@app.route("/cars", methods=["POST"])
def create_car():
    brand = request.json["brand"]
    model = request.json["model"]
    cur.execute(
        f"INSERT INTO cars(brand, model) VALUES('{brand}', '{model}')")
    cur.execute(
        f"SELECT * FROM cars WHERE brand='{brand}' AND model='{model}'")
    records = cur.fetchall()
    if len(records) != 0:
        obj = {"id": records[0][0], "brand": records[0]
               [1], "model": records[0][2]}
        conn.commit()
        return jsonify(obj)

    return (jsonify({"error": "resource not found"}), 404)


@app.route("/cars/<int:id>", methods=["DELETE"])
def delete_car(id):
    car = utils.get(cur, id)
    if car == None:
        return (jsonify({"error": "resource not found"}), 404)

    cur.execute(f"DELETE FROM cars WHERE id = {id}")
    conn.commit()
    return jsonify(car)


@app.route("/cars/<int:id>", methods=["PUT"])
def update_car(id):
    car = utils.get(cur, id)

    if car == None:
        return (jsonify({"error": "resource not found"}), 404)

    brand = request.json["brand"]
    model = request.json["model"]
    cur.execute(
        f"UPDATE cars set brand='{brand}', model='{model}' WHERE id = {id}")

    car = utils.get(cur, id)
    conn.commit()
    return jsonify(car)


app.run("localhost", 3000, debug=True)

# API is a web server that returns json data and mos API's follow
# the REST API standarts(rules)
