# User class
class User:
    count_id = 0

    # initializer method
    def __init__(self,membership, remarks):
        User.count_id += 1
        self.__user_id = User.count_id

        self.__membership = membership
        self.__remarks = remarks

    # accessor methods
    def get_user_id(self):
        return self.__user_id



    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks

    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id


    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks