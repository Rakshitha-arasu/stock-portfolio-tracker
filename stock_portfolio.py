

def stock_portfolio():

    stocks = {
        "TCS": 3500,
        "Infosys": 1800,
        "Wipro": 500,
        "HCL": 1500
    }

    total_investment = 0

    print("================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("================================")

    for stock, price in stocks.items():

        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = price * quantity

        print(f"{stock} Price: Rs.{price}")
        print(f"{stock} Investment: Rs.{investment}")
        print("--------------------------------")

        total_investment += investment

    print("================================")
    print(f"Total Investment: Rs.{total_investment}")
    print("================================")

    print("Thank you for using Stock Portfolio Tracker!")


stock_portfolio()
