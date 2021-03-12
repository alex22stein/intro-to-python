#create the essencial lists and variable to be used
items = []
prices = []
bigger = ""
#possible actions presentation
print()
print("Welcome to the shopping cart program!")
print()
print("Please select one of the following: ")
print("1.Add item")
print("2.View cart")
print("3.Remove item")
print("4.Compute total")
print("5.Quit")
action = str(input("Please enter an action number: "))

while action != "5":
    #add item
    if action == "1":
        add = "yes"
        while add == "yes" or add == "y":
            item = str(input("What item would you like to add? "))
            items.append(item)
            price = float(input(f"What is the price of the '{item}'? "))
            prices.append(price)
            print(f"{item} has been added to your cart.")
            add = str(input("Do you want to add more item to your cart? Yes/No ")).lower()
            print()

    #view cart
    if action == "2":
        count = -1
        print()
        if items:
            print("The content of the shopping cart are: ")
            for item in items:
                if len(item) > len(bigger):
                    bigger = item
            for item in items:
                count = count + 1
                price = "{:.2f}".format(prices[count])
                show_item = items[count].capitalize()
                i = len(bigger) 
                index = str(count+1)+"."
                show_price = "$"+str(price)
                #print(f"{count+1}. {show_item:<5s} - {price:>1}")
                print(f"{index} {show_item:{i}}  -  {show_price:{i}}")
        else:
            print("The cart is empty")
        print()

    #remove item
    if action == "3":
        delete_more = "yes"
        while delete_more.lower() == "yes" or delete_more.lower() == "y":
            item_to_del = int(input("What item number do you want to remove? ")) -1
            if len(items) > item_to_del and item_to_del > -1:
                items.pop(item_to_del)
                del prices[item_to_del]
                print("Item removed.")
                print()
                delete_more = str(input("Do you want to remove more items? Yes/No "))
            else:
                print("Do not exist this item")
                delete_more = str(input("Do you still want to remove an item? Yes/No "))

        print()

    #compute total
    if action == "4":
        print()
        summ = 0
        for price in prices:
            summ = summ + price
        total = "{:.2f}".format(summ)
        print(f"The total price is: ${summ}")
        print()

    #in the case you select a not possible action
    if action != "1" and action != "2" and action != "3" and action != "4" and action != "5":
        print()
        print("Not possible action")
        print()

    #next action to looping works
    print("Please select one of the following: ")
    print("1.Add item")
    print("2.View cart")
    print("3.Remove item")
    print("4.Compute total")
    print("5.Quit")
    action = str(input("Please enter an action: "))

    

print()
print("Thank you! See you!")
print()