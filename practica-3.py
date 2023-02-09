from flask import Flask, render_template
from flask import request
from sale_order import SaleOrder
from sale_order_util import SaleOrderUtil

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("cinema.html")

@app.post("/")
def procces():
    saleOrder = SaleOrder(
            name=request.form.get('name'),
            buyers=int(request.form.get('buyers', "0")),
            quantity=int(request.form.get('tickets', "0")),
            unit_price=12.00,
            cardCinema=request.form.get('cardCinema', ""),
        )     
    saleOrderUtil = SaleOrderUtil(saleOrder)
    saleOrderUtil.validate()
        
    if saleOrderUtil.error != '':
        return render_template("cinema.html", error=saleOrderUtil.error)
    
    saleOrderUtil.calculateDiscount()
    return render_template("cinema.html", saleOrder=saleOrder)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
