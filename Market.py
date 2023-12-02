class Market:
    def __init__(self, item_count, price):
        self.item_count = item_count
        self.item_price = price
        self.market_balance = 0

    def buy_item(self):
        if self.item_count > 0:
            self.market_balance += self.item_price
