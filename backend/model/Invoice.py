#TODO ?

class InvoiceModel:
    def __init__(self, data):
        self.invoice_id = data.get('invoice_id')
        self.invoice_code = data.get('invoice_code')
        self.date = data.get('date')
        self.prev_electric = data.get('prev_electric', 0)
        self.curr_electric = data.get('curr_electric', 0)
        self.prev_water = data.get('prev_water', 0)
        self.curr_water = data.get('curr_water', 0)
        self.room_price = data.get('room_price', 0)
        self.electric_price = data.get('electric_price', 0)
        self.water_price = data.get('water_price', 0)
        self.internet_fee = data.get('internet_fee', 0)
        self.another_fee = data.get('another_fee', 0)
        self.garbage_fee = data.get('garbage_fee', 0)
        self.discount = data.get('discount', 0)

'''


'''