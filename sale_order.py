class SaleOrder:
    def __init__(self, name, buyers, quantity, unit_price, cardCinema):
        self.name = name
        self.buyers = buyers
        self.quantity = quantity
        self.unit_price = unit_price
        self.cardCinema = cardCinema or False
