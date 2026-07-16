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
