# remember to inherit from user class to get the user ID

class PaymentInfo: 
    transaction_count = 0

    def __init__(self, address_line_1, address_line_2, state, country, postal_code, remember): 
        self.__address_line_1 = address_line_1
        self.__address_line_2 = address_line_2
        self.__state = state
        self.__postal_code = postal_code
        self.__country = country 
        self.__remember = remember
        PaymentInfo.transaction_count += 1

    def get_address_line_1(self):
        return self.__address_line_1
    
    def get_address_line_2(self):
        return self.__address_line_2
    
    def get_state(self):
        return self.__state
    
    def get_postal_code(self):
        return self.__postal_code
    
    def get_country(self):
        return self.__state
    
    def get_country(self):
        return self.__country