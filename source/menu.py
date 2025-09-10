from data import *
from funcs import * 


def foodAdd():
    while True:
        Clear()
        product = input("Please input a product to add: ")
        price = floatInput("Please input a price for this product: ")

        if price != None and product != None:
            food_products.append({
                "product": product,
                "price" : price
                })
            
            menuInsert(product, price, "Food")
            
            Clear()
            print("Product successfully added!")
            time.sleep(4)

            break

        Clear()

def foodUpdate():
    if len(food_products) == 0:
        print("There are no entries to update!")
        time.sleep(4)
        Clear()

    else:
        while True:
            Clear()

            printList("food")
            print(food_products)
            index_nav = IntInput("Please input a product ID you wish to update: ") 

            if index_nav != None:
                index_nav -= 1
                prod_id = int(food_products[index_nav].get("id"))

                if index_nav < 0 or index_nav > len(food_products) -1 :
                    Clear()
                    print("Error, input is out of range!") 
                    time.sleep(4) 
                    Clear() 
                    


                else:
                    while True:
                        Clear()
                        print("1: Product Name \n" \
                        "2: Product Price\n" \
                        "3: return ")
                        
                        menu_nav  = IntInput("Please select your update choice: ")
                        
                        #Updates name
                        if menu_nav == 1:
                                new = input("Please enter updated entry: ")
                                food_products[index_nav].update({"product": new})
                                menuUpdate(update = prod_id, product= new, price= food_products[index_nav].get("price"))
                                print("Entry successfully updated!")
                                time.sleep(4)
                                Clear()
                                break
                        
                        #Updates price
                        elif menu_nav == 2:
                            while True:
                                price = floatInput("Please input the new price: ")
                                if price != None:
                                    food_products[index_nav].update({"price": price})
                                    menuUpdate(update = prod_id, product= food_products[index_nav].get("product"), price= price)

                                    print("Entry successfully updated!")
                                    time.sleep(4)
                                    Clear()
                                    break
                            break
                            
                        elif menu_nav ==3:
                            break
                            
                        else:
                            print("Please ensure that a valid range was inputted!")
                break
                        
def foodDel():
    if len(food_products) == 0:
        print("There are no entries to delete!")
        time.sleep(4)
        Clear()

    else:
        while True:
            Clear()
            printList("food")

            index_nav = IntInput("Please input a product ID you wish to delete: ")
            
            if index_nav != None:
                index_nav -= 1
                datebase_id = str(food_products[index_nav].get("id"))

                if index_nav < 0 or index_nav > len(food_products) -1:
                    Clear()
                    print("Error, input is out of range")
                    time.sleep(4)
                    Clear()

                else:
                    Clear()

                    food_products.pop(index_nav)
                    menuDelete(db_id= datebase_id)
                    print("Entry successfully deleted!")
                    time.sleep(4)
                    Clear()
                    break
    
    Clear()

def foodProducts():
        #Input loop for input handling
    while True:
        #Menu for manipulating elements within the list
        print("Menu: \n\n" \
        "1: Add Product " \
        "\n2: Update Product" \
        "\n3: Remove Product" \
        "\n4: Return"\
        "\n_____________________"\
        "\n Product List\n" 
        )

        #Outputs the elements in the list of products
        printList("food")

        menu_nav = IntInput("Input a corresponding Menu Item: ")

        if menu_nav != None:
        #Adds product to menu
            if menu_nav == 1:
                foodAdd()

            elif menu_nav== 2:
                foodUpdate()
                
            elif menu_nav == 3:
                foodDel()

            elif menu_nav == 4:
                #Overwrites file with whole list
                with open("../Data/food.csv", "w",newline="") as food_file:
                    fields = ["product", "price"]
                    
                    writer = csv.DictWriter(food_file, delimiter=",", fieldnames=fields)
                    for food in food_products:
                        
                        writer.writerow({"product" : food.get("product"),
                                        "price": food.get("price")})
                    pass

                break
            else:
                #I am a dumb dumb
                print("Please ensure that a valid menu item has been selected!")
                time.sleep(4)
                Clear()



def drinkAdd():
    while True:
        Clear()
        product = input("Please input a product to add: ")
        price = floatInput("Please input a price for this product: ")

        if price != None and product != None:
            drink_products.append({
                "product": product,
                "price" : price
                })
            
            #Adds to DB
            menuInsert(product, price, "Drink")
            
            Clear()
            print("Product successfully added!")
            time.sleep(4)

            break

def drinkUpdate():
    if len(drink_products) == 0:
        print("There are no entries to update!")
        time.sleep(4)
        Clear()

    else:
        while True:
            Clear()

            printList("drinks")

            index_nav = IntInput("Please input a product ID you wish to update: ") 

            if index_nav != None:
                index_nav -= 1
                prod_id = int(drink_products[index_nav].get("id"))
            
                if index_nav < 0 or index_nav > len(drink_products) -1 :
                    Clear()
                    print("Error, input is out of range!") 
                    time.sleep(4) 
                    Clear() 
                    
                else:
                    while True:
                        Clear()
                        print("1: Product Name \n" \
                        "2: Product Price\n" \
                        "3: Return ")
                        
                        menu_nav  = IntInput("Please select your update choice: ")
 
                        #Updates name
                        if menu_nav == 1:
                                new = input("Please enter updated entry: ")
                                drink_products[index_nav].update({"product": new})
                                menuUpdate(update = prod_id, product= new, price= drink_products[index_nav].get("price"))
                                print("Entry successfully updated!")
                                time.sleep(4)
                                Clear()
                                break
                        
                        #Updates price
                        elif menu_nav == 2:
                            while True:
                                price = floatInput("Please input the new price: ")
                                if price != None:
                                    drink_products[index_nav].update({"price": price})
                                    menuUpdate(update = prod_id, product= drink_products[index_nav].get("product"), price= price)

                                    print("Entry successfully updated!")
                                    time.sleep(4)
                                    Clear()
                                    break
                            break
                            
                        elif menu_nav ==3:
                            break

                        else:
                            print("Please ensure that a valid range was inputted!")
                break
                        
def drinkDel():
    if len(drink_products) == 0:
        print("There are no entries to delete!")
        time.sleep(4)
        Clear()

    else:
        while True:
            Clear()
            printList("drink")

            index_nav = IntInput("Please input a product ID you wish to delete: ")
            
            if index_nav != None:
                index_nav -= 1
                datebase_id = str(drink_products[index_nav].get("id"))
                if index_nav < 0 or index_nav > len(drink_products) -1:
                    Clear()
                    print("Error, input is out of range")
                    time.sleep(4)
                    Clear()

                else:
                    Clear()
                    
                    drink_products.pop(index_nav)
                    menuDelete(db_id= datebase_id)
                    
                    print("Entry successfully deleted!")
                    time.sleep(4)
                    Clear()
                    break
    
    Clear()


def drinkProducts():
    #Input loop for input handling
    while True:

        #Menu for manipulating elements within the list
        print("Menu: \n\n" \
        "1: Add Product " \
        "\n2: Update Product" \
        "\n3: Remove Product" \
        "\n4: Return"\
        "\n_____________________"\
        "\n Product List\n" 
        )

        #Outputs the elements in the list of products
        printList("drinks")

        menu_nav = IntInput("Input a corresponding Menu Item: ")

        if menu_nav != None:
        #Adds product to menu
            if menu_nav == 1:
                drinkAdd()
                
            elif menu_nav== 2:
                drinkUpdate()

            elif menu_nav == 3:
                drinkDel()
            
            elif menu_nav == 4:
                #Overwrites file with whole list
                with open("../Data/drink.csv", "w",newline="") as drink_file:
                    fields = ["product", "price"]
                    
                    writer = csv.DictWriter(drink_file, delimiter=",", fieldnames=fields)
                    for drink in drink_products:
                        
                        writer.writerow({"product" : drink.get("product"),
                                        "price": drink.get("price")})
                    pass

                break
            else:
                #I am a dumb dumb
                print("Please ensure that a valid menu item has been selected!")
                time.sleep(4)
                Clear()
