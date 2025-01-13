menu = {                    #dictionary storing all the items
1000:["$5", "Cappuccino" ] , 
1001:["$4.50" , "Latte"] , 
1002:["$5" , "Mocha"] , 
1003:["$5" , "French Vanilla"] , 
1004:["$1.50" , "Black"] ,
1005:["$3" , "Machiato"] , 
1006:["$3" , "Americano"] , 
1007:["$2.50" , "Espresso"] , 
1008:["$4" , "Irish"] , 
1009:["$5" ,"Frappe"] , 
1010:["$2" , "Cold Brew"] , 
1011:["$4" ,"Iced Coffee"] , 
1012:["$5" ,"Frappe"] , 
1013:["$6.50" ,"Iced French Vanilla"] , 
1014:["$4" ,"Iced Macha"]
}
print(menu)
for list , info in menu.items(): #iterates through every item in the dictionary
    price , name = info
    print(f"code: ({list}), Item: {name} , Price: {price}")
user_input = int(input("Enter the code of the product you want to purchase: "))
selection = menu[user_input] #retrieving the user input
cost = float(selection[0][1:]) #changing the datatype of price from string to float
print(f"You selected {selection}")
user_suggestion = input("Would you like to have some cookies with your coffee? \n Y/n")
if user_suggestion == 'Y':
    new_cost = cost + 1.0
    print(f"Your total is ${new_cost}")
    cost = new_cost
else:
    print(f"Your total is ${cost}")
money = float(input("Please insert money!"))
change = money - cost
selection_2 = selection[1] #retrieving the name of the item and assigning it to a new variable to print it
if change == 0: #proofing the cost calculator in the following block of conditional statements
    print("Thank you for your purchase!")
elif change < 0:
    print("Insufficient amount!")
else:
    print(f"{selection_2} has been dispensed")
    print(f"Your change is ${change} \nThank you for your purchase!")
    