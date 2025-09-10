from funcs import *
from data import courier_list 

def addCourier():
        #gets courier information
        cour_name = input("Please input the couriers name: ")

        phone_num = phone()

        #adds to list
        courier_list.append({
            "name": cour_name,
            "phone": phone_num 
        })
        courierInsert(cour_name, phone_num)

        Clear()

def updateCourier():
    #Checks if theres an element to update
    if len(courier_list) == 0:
        print("There are no entries to update!")
        time.sleep(4)
        Clear()
    
    #updates elements
    else:
        while True:
            Clear()

            printList("courier_list")
            index_nav = IntInput("Please input a courier ID you wish to update: ") 

            if index_nav != None:
                index_nav -= 1
                cour_id = int(courier_list[index_nav].get("id"))

                if index_nav < 0 or index_nav > len(courier_list) -1 :
                    Clear()
                    print("Error, input is out of range!") 
                    time.sleep(4) 
                    Clear() 
                    
                else:
                    #Menu to chose what item in the entry you'd like to update
                    while True:
                        Clear()
                        print(
                            "1: Update Name\n"\
                            "2: Update Phone Number\n"
                        )
                        menu_nav = IntInput("Please input a menu item: ")

                        #Selection to what option is being updated
                        if menu_nav == 1:

                            c_name = input("Please input the updated courier name: ")
                            courierUpdate(c_name, courier_list[index_nav].get("phone"), cour_id )
                            courier_list[index_nav].update({"name" : c_name}) 
                            Clear()
                            break
                            
                        elif menu_nav == 2:

                            phone_num = phone()
                            courierUpdate(courier_list[index_nav].get("name"), phone_num , cour_id )
                            courier_list[index_nav].update({"phone" : phone_num})


                        #Exits code block
                            print("Entry successfully updated!")
                            time.sleep(4)
                            Clear()
                            break

                        else:
                            print("Please ensure you have selected a valid menu item!")
            break

def delCourier():
    #Checks if theres actually an item to delete
    if len(courier_list) == 0:
        print("There are no entries to delete!")
        time.sleep(4)
        Clear()
    
    #Deletes item
    else:
        while True:
            Clear()
            printList("courier_list")

            index_nav = IntInput("Please input a product ID you wish to delete: ")
            
            if index_nav != None:
                index_nav -= 1
                cour_id = str(courier_list[index_nav].get("id"))
                if index_nav < 0 or index_nav > len(courier_list) -1:
                    Clear()
                    print("Error, input is out of range")
                    time.sleep(4)
                    Clear()
                else:
                    Clear()
                    courier_list.pop(index_nav)
                    courierDelete(cour_id)
                    print("Entry successfully deleted!")
                    time.sleep(4)
                    Clear()
                    break
    
    Clear()

def couriersFunc():
        #Input loop for input handling
    while True:
        #Menu for manipulating elements within the list
        print("Menu: \n\n" \
        "1: Add Courier " \
        "\n2: Update Courier" \
        "\n3: Remove Courier" \
        "\n4: Return"\
        "\n_____________________"\
        "\n Courier List\n" 
        )
        #Outputs the elements in the list of products
        printList("courier_list")

        menu_nav = IntInput("Input a corresponding Menu Item: ")

        if menu_nav != None:
        #Adds product to menu
            if menu_nav == 1:
                addCourier()

            elif menu_nav== 2:
                updateCourier()
    
            elif menu_nav == 3:
                delCourier()
            elif menu_nav == 4:
                #Overwrites file with whole list
                with open("../Data/courier.csv", "w",newline="") as courier_file:
                    fields = ["name", "phone"]
                    
                    writer = csv.DictWriter(courier_file, delimiter=",", fieldnames=fields)
                    for courierPerson in courier_list:
                        
                        writer.writerow({"name" : courierPerson.get("name"),
                                        "phone": courierPerson.get("phone")})
                    pass
            
                break
            else:
                #I am a dumb dumb
                print("Please ensure that a valid menu item has been selected!")
                time.sleep(4)
                Clear()
