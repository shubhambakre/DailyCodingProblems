# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

# Python3 program for the above approach
def max_profit(prices: list, days: int) -> int:

    profit = 0

    for i in range(1, days):

        # checks if elements are adjacent and in increasing order
        if prices[i] > prices[i-1]:

            # difference added to 'profit'
            profit += prices[i] - prices[i-1]

    return profit

# Driver Code
if __name__ == '__main__':

    # stock prices on consecutive days
    prices = [100, 180, 260, 310, 40, 535, 695]

    # function call
    profit = max_profit(prices, len(prices))
    print(profit)
