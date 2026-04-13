class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:
    def __init__(self):
        self.beverages = [
            Beverage("Coke", 1.50),
            Beverage("Sprite", 1.25),
            Beverage("Water", 1.00),
            Beverage("Pepsi", 1.50),
            Beverage("Juice", 1.75),
            Beverage("Tea", 1.25)
        ]

    def display_menu(self):
        print("\n===== Vending Machine =====")
        for i in range(len(self.beverages)):
            print(f"{i + 1}. {self.beverages[i].name} - ${self.beverages[i].price:.2f}")

    def vend_beverage(self, choice):
        if choice < 1 or choice > len(self.beverages):
            print("Invalid selection.")
            return

        beverage = self.beverages[choice - 1]
        print(f"You selected {beverage.name}. Price: ${beverage.price:.2f}")

        money = 0.0

        while money < beverage.price:
            amount = float(input("Insert money: $"))
            money += amount

            if money < beverage.price:
                print(f"Not enough money. You still need ${beverage.price - money:.2f}")

        change = money - beverage.price
        print(f"Vending {beverage.name}...")

        if change > 0:
            print(f"Your change is ${change:.2f}")


def main():
    machine = VendingMachine()

    while True:
        machine.display_menu()
        choice = int(input("Select a beverage (1-6): "))
        machine.vend_beverage(choice)

main()