from card import Card
class Facecard(Card):
    def __init__(self,picture,rang,suit):
        super(Facecard, self).__init__(picture,rang,suit)
        self.soft = 10
        self.hard = 10

