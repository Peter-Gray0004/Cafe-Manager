import os
import csv
import time
from pathlib import Path
import psycopg2 as psycopg
from dotenv import load_dotenv


##creating vars referenced in all areas
drink_products = []
food_products = []
courier_list =[]
order_ID = {}


#DB Conn info
load_dotenv(dotenv_path="config.env")

host_name = os.environ.get("ip")
database_name = os.environ.get("db")
user_name = os.environ.get("user")
user_password = os.environ.get("password")


conn_info =     f"host='{os.getenv('ip')}'\
                dbname='{os.getenv('db')}' \
                user='{os.getenv('user')}' \
                password='{os.getenv('password')}' "

#connects to the DB and populates internal lists
def databaseInit():
    #establishes DB connection
    try:
        with psycopg.connect(conn_info) as conn: 

            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")
            cursor.execute("SELECT * FROM products;")

            rows = cursor.fetchall()

            for  each in rows:
                if each[3] == "Drink":
                    drink_products.append({"id": each[0], "product" : each[1],"price" : each[2] })
                elif each[3] == "Food":
                    food_products.append({"id": each[0], "product" : each[1],"price" : each[2] })
            
            cursor.execute("SELECT * FROM couriers;")
            rows = cursor.fetchall()
            for each in rows:
                courier_list.append({"id": each[0], "name" : each[1],"phone" : each[2] })


    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)



#Inserts updated entries into menu
def menuInsert(product, price, prodtype):
    try:
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''INSERT INTO products (product_name, product_price, product_type)
                            VALUES(%s,%s,%s)
                           RETURNING product_id;''',
                            (product, price, prodtype))

                          

            conn.commit()

    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

def menuUpdate(update, product, price):
    try: 
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''UPDATE products
                           SET product_name = %s, product_price = %s
                           WHERE product_id = %s''',
                           (product, price, update))

            conn.commit()
    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

def menuDelete(db_id):
    try: 
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''DELETE FROM products
                           WHERE product_id = %s''',
                           (db_id,))

            conn.commit()
    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

#Inserts updated entries into menu
def courierInsert(name, phone):
    try:
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''INSERT INTO couriers (courier_name, courier_phone)
                            VALUES(%s,%s);''',
                            (name, phone))

            conn.commit()

    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

def courierUpdate(name, phone, c_id):
    try: 
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''UPDATE couriers
                           SET courier_name = %s, courier_phone = %s
                           WHERE courier_id = %s''',
                           (name, phone, c_id))

            conn.commit()
    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

def courierDelete(db_id):
    try: 
        with psycopg.connect(conn_info) as conn: 
            
            cursor = conn.cursor()
            cursor.execute("SET search_path TO cafe;")

            cursor.execute('''DELETE FROM couriers
                           WHERE courier_id = %s''',
                           (db_id,))

            conn.commit()
    except Exception as oopsie:
        print(oopsie)
        time.sleep(5)

#ensures Dir and files Exists

def FileCheck():
    paths = ["../Data/courier.csv","../Data/orders.csv"]
    if os.path.exists("../Data") == False:
        os.mkdir("../Data")

    for each in paths:
        if os.path.exists(each) == False:
            with open(each, "w") as file:
                None

                


    #Populates lists with data stored in files
    try:
        with open ("../Data/orders.csv", "r") as order_file:
            csv_file = csv.reader(order_file, delimiter=",")

            for each in csv_file:
                try:
                    order_ID.update({int(each[0]) : {
                        "customer_name" : each[1],
                        "customer_address" : each[2],
                        "customer_phone" : each[3],
                        "status" : each[4],
                        "order_contents" : each[5]                      
                                            }})
                except Exception as oops:
                    print(oops)
    
    except Exception as oops:
        print(oops)
            
'''    try:
        with open("../Data/courier.csv", "r", ) as courier_file:
            csv_file = csv.reader(courier_file, delimiter=",")

            for x in csv_file:
                courier_list.append({"name" : x[0],"phone" : x[1] })
    except Exception as oops:
        print(oops)'''
            
        