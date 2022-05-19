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

def separate():
    print("_______________________________________________________________________")


# EJERCICIO 1
separate()
print("EJERCICIO 1")
print(" ")

coll.update_many({"name": 'MeetMoi'}, {"$inc": {"number_of_employees": 1}})
print_value_key(coll, "name", "MeetMoi", "number_of_employees")

print(" ")
separate()


# EJERCICIO 2
print("EJERCICIO 2")
print(" ")

count = str(coll.count_documents({"founded_year" : 2000}))
print("El número de compañias fundado el año 2000 es de "+count)

print(" ")
separate()


# EJERCICIO 3
print("EJERCICIO 3")
print(" ")

count = str(len(coll.distinct("category_code")))
print("Existen "+count+" valores distintos en el campo category_code")

print(" ")
separate()


# EJERCICIO 4
print("EJERCICIO 4")
print(" ")

coll.update_many({}, [{ "$set": { "tag_list": {"$concat": ["$tag_list", ", ", "phone"]} } }], upsert=True)
count = 1
print("Mostrando las 5 primeras empresas:")
for i in coll.find({}):
    print("name: " + i["name"] + " --- " + "tag_list: " + str(i["tag_list"]))
    if count == 5:
        break
    else:
        count = count + 1

print(" ")
separate()


# EJERCICIO 5
print("EJERCICIO 5")
print(" ")

filtered = coll.find({"founded_year": {"$gt": 2005}, "number_of_employees": {"$gt": 0}})
numCompanies = int(coll.count_documents({"founded_year": {"$gt": 2005}, "number_of_employees": {"$gt": 0}}))
sum = 0
for company in filtered:
    sum = sum + company["number_of_employees"]
average = sum / numCompanies

print("La mediana de trabajadores es de "+ str(average) + " trabajadores")

print(" ")
separate()

client.close()
