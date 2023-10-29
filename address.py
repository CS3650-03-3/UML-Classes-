
class Address:

    def __init__(self, street_address, city, state, postal_code):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__postal_code = postal_code

    def get_street_address(self):
        return self.__street_address
    
    def set_street_address(self, street_address):
        self.__street_address = street_address

    def get_city(self):
        return self.__city
    
    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state

    def get_postal_code(self):
        return self.__postal_code
    
    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def is_valid_address(self):
        return True