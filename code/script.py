import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
coll = db["companies"]


def print_value_key(collection, field, key, value):  # funcion que ayuda a imprimir el valor de una field con una condicion de key
    base = collection.find({})
    for d in base:
        if d[field] == key:
            valor = str(d[value])
            print("El valor de " + value + " es " + valor)


# EJERCICIO 1

# coll.update_many({"name": 'MeetMoi'}, {"$inc": {"number_of_employees": 1}})
# print_value_key(coll, "name", "MeetMoi", "number_of_employees")

# EJERCICIO 2

# count = str(coll.count_documents({"founded_year" : 2000}))
# print("El número de compañias fundado el año 2000 es de "+count)

# EJERCICIO 3

# count = str(len(coll.distinct("category_code")))
# print("Existen "+count+" valores distintos en el campo category_code")

# EJERCICIO 4
coll.aggregate([{"$addFields": {"tag_list": {"$concat": ["$tag_list", ", ", "phone"]}}}])

# EJERCICIO 5


client.close()
