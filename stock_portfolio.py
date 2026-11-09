portfolio = []

while True:
    print("\n--- Stock Portfolio Tracker ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Total Investment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter purchase price: "))

        stock = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        portfolio.append(stock)
        print("Stock added successfully!")

    elif choice == "2":
        for stock in portfolio:
            print(stock["name"], stock["quantity"],
                  stock["price"])

    elif choice == "3":
        total = 0

        for stock in portfolio:
            total += stock["quantity"] * stock["price"]

        print("Total Investment:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")