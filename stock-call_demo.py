# stock-call_demo.py

def covered_call_profit(stock_price, strike_price, premium):
    """
    Calculates the profit from a covered call strategy.

    Args:
        stock_price (float): The current price of the stock.
        strike_price (float): The strike price of the call option.
        premium (float): The premium received from selling the call.

    Returns:
        float: Total profit from the covered call strategy.
    """
    return min(stock_price, strike_price) - strike_price + premium

# Sample usage
print("Profit:", covered_call_profit(105, 100, 3))  # Expected: $3
