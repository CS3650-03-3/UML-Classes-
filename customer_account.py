from address import Address
from credit_card import CreditCard

class Customer(Address, CreditCard):

    def __init__(self, street_address, city, 
                 state, postal_code, name, 
                 number, code, expiration_date, 
                 email):
        Address.__init__(street_address, city, state, postal_code)
        CreditCard.__init__(name, number, code, expiration_date)
        self.__email = email

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    