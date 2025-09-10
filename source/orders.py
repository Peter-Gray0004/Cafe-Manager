from data import *
from funcs import * 

def createOrder():
    while True:
        #Asks for the details of the order
        Clear()

        c_name = input("Please input the customers name: ")
        Clear()
        
        c_address = input("Please input the customers address: ")
        Clear()

    
        c_phone = phone()

        #Menu to decide what products are to the order
        order=[]
        while True:
        
            Clear()
            print ("_____________________\nDrinks Menu")
            printList("drinks")
            print("_____________________\nFood Menu\n_____________________")
            printList("food")
            print("1: Add a Drink\n"\
            "2: Add a Food\n"\
            "3: Remove from current order\n"\
            "4: Finish Order\n")

            #Checks if the order has contents and decides what to do from there
            if len(order) == 0:
                print("Order is empty")
            else: 
                print("Current Order")
                for i, l in enumerate(order, 1):
                    print(f"{i}: {l}")

            #Menu to ask 
            menu_nav = IntInput("Please select an option: ")
            if menu_nav!= None:
                if menu_nav == 1:
                    
                    Clear()
                    print ("_____________________\nDrinks Menu")
                    while True:
                        print ("_____________________")
                        printList("drinks")
                        prod_ID = IntInput("Please select an option: ")
                        
                        if prod_ID == None:
                            time.sleep(4)
                            Clear()
                            print("Please ensure a number was entered!")
                        else:
                            try:
                                order.append(drink_products[prod_ID - 1].get("product"))
                                break

                            except IndexError:
                                print("Please ensure a valid product ID was selected")
                                time.sleep(4)
                                Clear()
                        
                elif menu_nav ==2:
                    Clear()

                    while True:
                        
                        print ("_____________________\nFood Menu")
                        printList("food")
                        prod_ID = IntInput("Please select an option: ")
                        
                        if prod_ID == None:
                            time.sleep(4)
                            Clear()
                            print("Please ensure a number was entered!")
        
                        else:
                            try:
                                order.append(food_products[prod_ID - 1].get("product"))
                                break

                            except IndexError:
                                print("Please ensure a valid product ID was selected")
                                time.sleep(4)
                                Clear()

                elif menu_nav == 3:
                    while True:
                        Clear()     
                        for y, l in enumerate(order, 1):
                            print(y, l)
                            
                        order_index = IntInput("Please select the option to be deleted: ")

                        if order_index != None:
                            if order_index < 0 or order_index > len(order):
                                print("Please ensure that the correct item was selected!")
                                time.sleep(4)
                                Clear()
                                
                            else:
                                order.pop(order_index -1)
                                break
                        else:
                            print("Please ensure that you inputted an item!")
                            time.sleep(4)
                            Clear()

                    
                elif menu_nav == 4:
                    while True:
                        menu_nav = IntInput("Please enter 1 to confirm or 2 to cancel the order: ")
                        if menu_nav == 1:
                            new_ID = len(order_ID) +1
                            order.sort()
                            order_ID.update({new_ID : {
                                "customer_name" : c_name,
                                "customer_address" : c_address,
                                "customer_phone" : c_phone,
                                "status" : "Received",
                                "order_contents": order
                            }})
                            break
                        
                        elif menu_nav == 2: 
                            break
        
                        else: 
                            print("Please ensure that you inputted an item!")
                            time.sleep(4)
                            Clear()  
                    break
        break

def updateOrder():
    while True:
        Clear()
        print(
            "1: Update Order Details\n"\
            "2: Status Update\n"\
            "3: Return"
        )


        #Menu to specify if its a general 
        menu_nav = IntInput("Input a corresponding Menu Item: ")

        if menu_nav == 1:

            while True:
                while True:
                    Clear()
                    print("______________")
                    printList("order_list")
                    print("______________")

                    c_ID = IntInput("Please input your selected customer")
                    if c_ID > len(order_ID):
                        print("Please ensure that the selected items are within range!")
                    else:
                        break
                
                menu_nav = IntInput("1: Name\n"\
                "2: Address\n" \
                "3: Phone Number\n"\
                "What item would you like to update: ")
                if menu_nav != None:
                    break
            Clear()
            if menu_nav == 1:

                c_name = input("Please input the customers name: ")
                
                order_ID[c_ID].update({"customer_name" : c_name})

            elif menu_nav == 2: 

                c_address = input("Please input the customers address: ")

                order_ID[c_ID].update({"customer_address" : c_address})

            elif menu_nav == 3:
                while True:
                    c_phone = IntInput("Please input the phone number: ")
                    if c_phone == None:
                        print("Please ensure that the input is all numbers")
                    else:    
                        #UK phone numbers are either 10 (landlines) or 11 (mobile) digits long, this check ensure that the phone number is valid
                        #note: the reason it evaluates 9 and 10 is because the int strips leading zero's, its re-added as a string
                        if len(str(c_phone)) ==9 or len(str(c_phone)) == 10:
                            c_phone = f"0{c_phone}"
                            break
                        else:
                            print("Please ensure that a valid UK phone number was entered!")

                order_ID[c_ID].update({"customer_phone" : c_phone})
            elif menu_nav == 4:
                break
            else:
                print("Please ensure a valid item was entered!")
            break

        elif menu_nav == 2:
            while True:
                Clear()
                print("______________")
                printList("order_list")
                print("______________")

                c_ID = IntInput("Please input your selected customer: ")
                if c_ID > len(order_ID):
                    print("Please ensure that the selected items are within range!")
                    time.sleep(4)
                else:
                    break
            #Menu to select the new status of 
            while True:
                Clear()
                menu_nav = IntInput("1: Received\n" \
                "2: Preparing\n" \
                "3: Out For delivery \n" \
                "4: Delivered \n" \
                "5: Canceled\n"
                "Please input you selection here: ")

                if menu_nav !=None:
                    if menu_nav == 1:
                        order_ID[c_ID].update({"status" : "Received"})
                        break
                    elif menu_nav == 2:
                        order_ID[c_ID].update({"status" : "Preparing"})
                        break
                    elif menu_nav == 3:
                        order_ID[c_ID].update({"status" : "Out For Delivery"})
                        break
                    elif menu_nav == 4:
                        order_ID[c_ID].update({"status" : "Delivered"})
                        break
                    elif menu_nav == 5:
                        order_ID[c_ID].update({"status" : "Canceled"})
                        break
                    else:
                        print("Please ensure that the input was within range!")
                        time.sleep(4)
                else:
                    print("Please ensure a number was inputted!")
                    time.sleep(4)
                break
            break 
        elif menu_nav == 3:
            Clear(
                
            )
            break

        else:
            print("Please ensure you are within the menu range!")

def order():

    while True:

        #Menu for dealing with orders
        print("Main Menu\n\n" \
        "1: Create Order\n" \
        "2: Edit Order\n" \
        "3: Return\n"\
        "_____________________\n") 
        #Prints out all orders
        printList("order_list")

        #Asks for input (function to auto check if its a valid int)
        menu_nav = IntInput("Input a corresponding Menu Item: ")

        #Logic for nav menu
        if menu_nav != None:
            if menu_nav == 1:
                createOrder()
                        

            elif menu_nav == 2:
                updateOrder()
        
            elif menu_nav == 3:
                #writes to file
                with open("..//data//orders.csv", 'w', newline='') as file:
                    order_file = csv.writer(file, delimiter= ",")
                    for ID in order_ID:

                        #List for "Write row to function correctly"
                        insert = [ID,
                               order_ID[ID].get("customer_name"),
                               order_ID[ID].get("customer_address"),
                               order_ID[ID].get("customer_phone"),
                               order_ID[ID].get("status"),
                               order_ID[ID].get("order_contents")]
                        
                        order_file.writerow(insert)


                break
            
            else:
                #I am a dumb dumb
                print("Please ensure that a valid menu item has been selected!")
                time.sleep(4)
                Clear()


 