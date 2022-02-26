class atm():
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def cash_withdral(self):
        print('cash_withdral')
    def bank_enquiry(self):
        print('bank_enquiry')

hdfc = atm(4584981800344185,436)