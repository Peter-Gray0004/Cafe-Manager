import os
import time
from data import *

#A function for inputting a integer
def IntInput(console_output = "Please configure your input"):
    try:
        return int(input(console_output))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please ensure a number has been inputted!")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        return None

#A function for inputting a float
def floatInput(console_output = "Please configure your input"):
    try:
        return float(input(console_output))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please ensure a number has been inputted!")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        return None

#Clears the console
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Gets a phone number
def phone():
    while True:
        phone = input("Please input a valid UK phone number: ")
        if phone == None:
            print("Please ensure that the input is all numbers")
        else:    
            #UK phone numbers are either 10 (landlines) or 11 (mobile) digits long, this check ensure that the phone number is valid
            
            if len(str(phone)) ==10 or len(phone) == 11:
                if phone.isdigit():
                    return phone
                    
                else:
                    print("Please ensure that the phone number consists of numbers")
            else:
                print("Please ensure that the phone number is the correct length")


#Outputs a list of items to the console
def printList(input):

    if input == "drinks":
        if len(drink_products) == 0:
            print("No products have been entered!")
        else:
            for t, d_prod in enumerate(drink_products): 
                print(f"ID: {t + 1} | Product: {drink_products[t].get("product")} | Price: £{drink_products[t].get("price")}")

        print("_____________________\n")

    elif input == "food":
        if len(food_products) == 0:
            print("No products have been entered!")
        else:
            for t, f_prod in enumerate(food_products): 
                print(f"ID: {t + 1} | Product: {food_products[t].get("product")} | Price: £{food_products[t].get("price")}")

        print("_____________________\n")  

    elif input == "order_list":
        for ID in order_ID:
            print ( f"ID: {ID}\
                Name: {order_ID[ID].get("customer_name")} |\
                Address: {order_ID[ID].get("customer_address")} |\
                Phone Number: {order_ID[ID].get("customer_phone")} |\
                status: { order_ID[ID].get("status")} |\
                Order: {str(order_ID[ID].get("order_contents")).strip("[]")}")

    elif input == "courier_list":
        if len(courier_list) == 0:
            print("No courier has been entered!")
        else:
            for t, cour in enumerate(courier_list): 
                
                print(f"ID: {t + 1} | Name: {courier_list[t].get("name")} | Phone: {courier_list[t].get("phone")}")
        print("_____________________\n")        
