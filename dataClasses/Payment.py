# remember to inherit from user class to get the user ID

class PaymentInfo: 
    transaction_count = 0

    def __init__(self, address_line_1, address_line_2, state, country, postal_code, remember, expiry_date_year, cvv, credit_card_number, card_holder_name, expiry_date_month): 
        self.__address_line_1 = address_line_1
        self.__address_line_2 = address_line_2
        self.__state = state
        self.__postal_code = postal_code
        self.__country = country 
        self.__cvv = cvv
        self.__expiry_date_year = expiry_date_year
        self.__expiry_date_month = expiry_date_month
        self.__card_holder_name = card_holder_name
        self.__credit_card_number = credit_card_number
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
    
    def get_cvv(self):
        return self.__cvv
    
    def get_expiry_date_year(self):
        return self.__expiry_date_year
    
    def get_expiry_date_month(self):
        return self.__expiry_date_month
    
    def get_card_holder_name(self):
        return self.__card_holder_name
    
    def get_credit_card_number(self):
        return self.__credit_card_number
    
    def get_remember(self):
        return self.__remember

    def set_address_line_1(self, address_line_1):
        self.__address_line_1 = address_line_1
    
    def set_address_line_2(self, address_line_2):
        self.__address_line_2 = address_line_2
    
    def set_state(self, state):
        self.__state = state
    
    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code
    
    def set_country(self, state):
        self.__state = state
    
    def set_country(self, country):
        self.__country = country
    
    def set_cvv(self, cvv):
        self.__cvv = cvv
    
    def set_expiry_date_year(self, expiry_date_year):
        self.__expiry_date_year = expiry_date_year
    
    def set_expiry_date_month(self, expiry_date_month):
        self.__expiry_date_month = expiry_date_month
    
    def set_card_holder_name(self, card_holder_name):
        self.__card_holder_name = card_holder_name
    
    def set_credit_card_number(self, credit_card_number):
        self.__credit_card_number = credit_card_number

    def set_remember(self, remember):
        self.__remember = remember