class User:
    def __init__(self,name,money):
        self.__name = name
        self.__money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,money):
        self.__money = money

