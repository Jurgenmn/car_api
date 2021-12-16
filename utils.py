def get(cur, id):
    cur.execute(f"SELECT * FROM cars WHERE id = {id}")
    records = cur.fetchall()
    if len(records) != 0:
        obj = {"id": records[0][0], "brand": records[0]
               [1], "model": records[0][2]}
        return obj

    return None
