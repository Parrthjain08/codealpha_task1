# Stock Portfolio Tracker

#dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

total_investment = 0
portfolio = []

# User input
num_stocks = int(input("Enter the number of stocks you want to track: "))
for i in range(num_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio.append([stock_name, quantity, price, investment])

        print(f"{stock_name}: {quantity} shares × ${price} = ${investment}")
    else:
        print("Stock not found! Skipping...")

# Display total investment
print("\n------ Portfolio Summary ------")
for stock in portfolio:
    print(f"{stock[0]} - Quantity: {stock[1]}, Price: ${stock[2]}, Value: ${stock[3]}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save to file
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Save as (.txt or .csv): ").lower()

    if file_type == ".txt":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-----------------------\n")

            for stock in portfolio:
                file.write(
                    f"{stock[0]} - Quantity: {stock[1]}, "
                    f"Price: ${stock[2]}, Value: ${stock[3]}\n"
                )

            file.write(f"\nTotal Investment Value: ${total_investment}")

        print("Portfolio saved as portfolio.txt")

    elif file_type == ".csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")

            for stock in portfolio:
                file.write(
                    f"{stock[0]},{stock[1]},{stock[2]},{stock[3]}\n"
                )

            file.write(f"Total,,,${total_investment}")

        print("Portfolio saved as portfolio.csv")

    else:
        print("Invalid file type. Result not saved.")

else:
    print("Result not saved.")
