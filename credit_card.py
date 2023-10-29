
class CreditCard:

    def __init__(self, name, number, code, expiration_date):
        self.__name = name
        self.__number = number
        self.__code = code
        self.__expiration_date = expiration_date

    def get_details(self):
        return (self.__name, self.__number, self.__code, self.__expiration_date)
    
    def set_details(self, name, number, code, expiration_date):
        self.__name = name
        self.__number = number
        self.__code = code
        self.__expiration_date = expiration_date

    def verity_details(self):
        return True