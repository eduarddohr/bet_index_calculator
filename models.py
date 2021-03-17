class Company:
    no_shares = 0
    new_weight = 0

    def __init__(self, name, symbol, price, weight):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.weight = weight
