total_price = 0
drink_count = 0

while True:
    name = input("Enter customer name or type 'done' to finish: ")

    if name == "done":
        break

    drink = input("Enter order for " + name + ": ")

    if drink == "latte":
        total_price += 3.50
        drink_count += 1
    elif drink == "americano":
        total_price += 3.00
        drink_count += 1
    elif drink == "espresso":
        total_price += 2.50
        drink_count += 1
    else:
        print(f"Sorry, {drink} is not on the menu.")
        continue

print("Order queue complete.")
print("Total drink ordered: ", drink_count)
print(f"Total price: ${total_price}")