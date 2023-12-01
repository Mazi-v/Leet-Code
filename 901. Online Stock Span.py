"""Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price."""
class StockSpanner:
    def __init__(self):
        self.daily_prices = []  # List to store the daily prices and their spans

    def next(self, price: int) -> int:
        span = 1  # Initializing the span of the current day
        while self.daily_prices and self.daily_prices[-1][0] <= price:
            # If the last price in the stack is less than or equal to today's price
            prev_price, prev_span = self.daily_prices.pop()
            span += prev_span  # Incrementing the span by the previous span

        self.daily_prices.append((price, span))  # Adding current price and its span to the stack
        return span
