class Result:
    def __init__(self,
                 distributor: str,
                 manufacturer: str or None = None,
                 mon: str or None = None,
                 don: str or None = None,
                 quantity: float or None = None,
                 invoice: dict or None = None,
                 order_number: dict or None = None,
                 LOT: str or None = None,
                 date_code: str or None = None, ):
        if order_number is None:
            order_number = {}
        if invoice is None:
            invoice = {}
        self.distributor = distributor
        self.manufacturer = manufacturer
        self.mon = mon
        self.don = don
        self.quantity = quantity
        self.order_number = order_number
        self.invoice = invoice
        self.LOT = LOT
        self.date_code = date_code

    def __str__(self):
        result_str = f"Distributor: {self.distributor}\n" \
                     f"Manufacturer: {self.manufacturer}\n" \
                     f"Manufacturer Order Number: {self.mon}\n" \
                     f"Distributor Order Number: {self.don}\n" \
                     f"Quantity: {self.quantity}\n"

        if self.invoice:
            result_str += f"Invoice: {self.invoice['number']}, position: {self.invoice['position']}\n"

        result_str += f"LOT: {self.LOT}\n" \
                      f"Date Code: {self.date_code}\n"

        return result_str
