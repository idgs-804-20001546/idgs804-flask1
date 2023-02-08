class SaleOrder:
    name = ''
    buyers = 0
    quantity = 0
    cardCinema = False
    unit_price = 0
    total = 0

    def __init__(self, name, buyers, quantity, unit_price, cardCinema):
        self.name = name
        self.buyers = buyers
        self.quantity = quantity
        self.unit_price = unit_price
        self.cardCinema = cardCinema
