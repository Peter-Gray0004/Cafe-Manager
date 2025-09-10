
#external libraries
import os
import time
from pathlib import Path

#Custom modules
from data import FileCheck, databaseInit
FileCheck()
databaseInit()
from funcs import *
from courier import couriersFunc
from menu import drinkProducts,foodProducts
from orders import order



def subMenu():
    while True:
        Clear()
        print("Menu: \n\n" \
        "1: Drinks Menu " \
        "\n2: Food Menu" \
        "\n3: Return")
        submenu_nav = int(input("Please select a menu item using a corresponding number: "))   
        if submenu_nav == 1:
            
            Clear()
            drinkProducts()

        elif submenu_nav == 2:
            Clear()
            foodProducts()

        elif submenu_nav == 3:
            Clear()
            break

        else:
            print("Please ensure you have inputted a valid menu item!")   

#Main loop ensuring application is running
x = True
while x == True: 
    Clear()
    #Main Menu
    
    print("Main Menu\n\n" \
    "1: Products\n" \
    "2: Orders\n" \
    "3: Couriers\n" \
    "4: Exit\n")       

    #Integer input for user numerical input with error and range checking
    main_menu_nav = IntInput("Input a corresponding Menu Item: ")

    #The code which handles the  menu, each one referring to a different function
    if main_menu_nav != None:
        if main_menu_nav == 1:
            #Submenu to decide if you want to view food or drinks
            subMenu()

        elif main_menu_nav ==2:
            Clear()
            order()
        elif main_menu_nav == 3:
            Clear()
            
            couriersFunc()
            
        elif main_menu_nav == 4:
            Clear()
            exit(0)
        else:
            Clear()
            #I am a dumb dumb
            print("Please ensure that a valid menu item has been selected!")
            time.sleep(4)
    else:
        print("Please enter a number")
            

