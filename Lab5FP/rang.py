class Rang:
    def __init__(self,soft,hard):
        self.__soft = soft
        self.__hard = hard

    @property
    def soft(self):
        return self.__soft

    @soft.setter
    def soft(self,soft):
        self.__soft = soft

    @property
    def hard(self):
        return self.__hard

    @hard.setter
    def hard(self,hard):
        self.__hard = hard
