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
