class SaleOrderUtil:
    error = ''

    def __init__(self, saleOrder):
        self.saleOrder = saleOrder 
 

    def validate(self):
        self.error = ''
        if self.saleOrder.quantity > self.saleOrder.buyers * 7:
            self.error = 'No puede comprar más de 7 boletos por persona'

    def calculateDiscount(self):
        total = 0
        quantity = self.saleOrder.quantity
        unit_price = self.saleOrder.unit_price

        if quantity > 5:
            total = float(quantity * unit_price) * 0.85
        elif quantity > 2:
            total = float(quantity * unit_price) * 0.90
        else:
            total = float(quantity * unit_price)

        if self.saleOrder.cardCinema:
            total = total * .90


        self.saleOrder.total = round(total, 2)
