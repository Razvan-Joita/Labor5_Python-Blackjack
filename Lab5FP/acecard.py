from card import Card
class Acecard(Card):
    def __init__(self,picture,rang,suit):
        super(Acecard, self).__init__(picture,rang,suit)
        self.soft =1
        self.hard = 11

