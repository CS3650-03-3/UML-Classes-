class Bill:

    def __init__(self, bill_id, monthly_usage, 
                 rate, amount_due, due_date, 
                 penalty_amount, address):
        self.__bill_id = bill_id
        self.__monthly_usage = monthly_usage
        self.__rate = rate
        self.__amount_due = amount_due
        self.__due_date = due_date
        self.__penalty_amount = penalty_amount
        self.__address = address

    def get_bill_id(self):
        return self.__bill_id
    
    def set_bill_id(self, bill_id):
        self.__bill_id = bill_id

    def get_monthly_usage(self):
        return self.__monthly_usage
    
    def set_monthly_usage(self, monthly_usage):
        self.__monthly_usage = monthly_usage

    def get_rate(self):
        return self.__rate
    
    def set_rate(self, rate):
        self.__rate = rate

    def print_bill(self):
        """
        Make a PDF of all the stuff to have a good bill?
        """
        return True