# Taco Palace Ordering System

# Function to print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $5.00")
    print("3. Nachos - $4.00")
    print("4. Soft Drink - $1.75")
    print("5. Quit")

# Function to get the price
def get_price(choice):
    if choice == 1:
        return 2.50
    elif choice == 2:
        return 5.00
    elif choice == 3:
        return 4.00
    elif choice == 4:
        return 1.75
    else:
        return 0

# Function to get the item name
def get_item_name(choice):
    if choice == 1:
        return "Taco"
    elif choice == 2:
        return "Burrito"
    elif choice == 3:
        return "Nachos"
    elif choice == 4:
        return "Soft Drink"
    else:
        return ""

# Main program
def main():
    total = 0
    order_list = []

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    choice = 0

    while choice != 5:
        print_menu()
        choice = int(input("Enter your selection: "))

        if choice == 5:
            break
        elif choice >= 1 and choice <= 4:
            item_name = get_item_name(choice)
            price = get_price(choice)

            print("You have selected", item_name)

            order_list.append(item_name)
            total = total + price
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

    # Final summary
    if len(order_list) > 0:
        print("\nYou ordered:")
        for item in order_list:
            print("-", item)
        print("Your total is $" + format(total, ".2f"))
    else:
        print("\nYou did not order anything.")

# Run the program
main()