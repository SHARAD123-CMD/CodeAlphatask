# STOCK PORTFOLIO TRACKER

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 160,
    "MSFT": 330
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", list(stock_prices.keys()))

n = int(input("Enter number of stocks you want to add: "))

for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Stock:", stock_name)
        print("Price per share:", stock_prices[stock_name])
        print("Investment Value:", investment)

    else:
        print("Stock not found!")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value =", total_investment)

# Optional: Save result in a file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Portfolio saved successfully in portfolio.txt")