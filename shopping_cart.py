#create the essencial lists to be used.
items = []
prices = []

#possible actions presentation
print("Welcome to the shopping cart program!")
print()
print("Please select one of the following: ")
print("1.Add item")
print("2.View cart")
print("3.Remove item")
print("4.Compute total")
print("5.Quit")
action = int(input("Please enter an action: "))

while action != 5:
    #add item
    if action == 1:
        add = "yes"
        while add == "yes":
            item = str(input("What item would you like to add? "))
            items.append(item)
            price = float(input(f"What is the price of the '{item}'? "))
            prices.append(price)
            print(f"{item} has been added to your cart.")
            add = str(input("Do you want to add more item to your cart? Yes/No ")).lower()
            print()

    #view cart
    if action == 2:
        count = -1
        print()
        if items:
            print("The content of the shopping cart are: ")
            for item in items:
                count = count + 1
                print(f"{count+1}. {items[count].capitalize()} - ${prices[count]}")
        else:
            print("The cart is empty")
        print()

    #remove item
    if action == 3:
        delete_more = "yes"
        while delete_more.lower() == "yes":
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
    if action == 4:
        print()
        summ = 0
        for price in prices:
            summ = summ + price
        print(f"The total price is: ${summ}")
        print()
    
    #next action to looping works
    print("Please select one of the following: ")
    print("1.Add item")
    print("2.View cart")
    print("3.Remove item")
    print("4.Compute total")
    print("5.Quit")
    action = int(input("Please enter an action: "))

print()
print("Thank you! See you")
print()