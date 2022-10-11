class Card:
    def __init__(self,picture,rang,suit):
        self.__picture = picture
        self.__rang = rang
        self.__suit = suit
        self.__soft = rang.soft
        self.__hard = rang.hard

    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def picture(self,picture):
        self.__picture = picture

    @property
    def rang(self):
        return self.__rang

    @rang.setter
    def rang(self,rang):
        self.__rang = rang

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self,suit):
        self.__suit = suit

    def __str__(self):
        pic = ""
        if self.suit == "A" and self.picture == "Spades":
            pic ='🂡'
        if self.suit=="Two" and self.picture== "Spades":
            pic = '🂲'
        if self.suit=="Three" and self.picture=="Spades":
            pic = '🂳'
        if self.suit == "Four" and self.picture == "Spades":
            pic ='🂴'
        if self.suit == "Five" and self.picture == "Spades":
            pic = '🂵'
        if self.suit == "Six" and self.picture == "Spades":
            pic = '🂶'
        if self.suit == "Seven" and self.picture == "Spades":
            pic ='🂷'
        if self.suit == "Eight" and self.picture == "Spades":
            pic ='🂸'
        if self.suit == "Nine" and self.picture == "Spades":
            pic ='🂹'
        if self.suit == "Ten" and self.picture == "Spades":
            pic ='🂺'
        if self.suit == "K" and self.picture == "Spades":
            pic ='🂾'
        if self.suit == "J" and self.picture == "Spades":
            pic ='🂫'
        if self.suit == "Q" and self.picture == "Spades":
            pic ='🂭'
        if self.suit == "A" and self.picture == "Heart":
            pic ='🂱'
        if self.suit == "Two" and self.picture == "Heart":
            pic ='🂲'
        if self.suit == "Three" and self.picture == "Heart":
            pic ='🂳'
        if self.suit == "Four" and self.picture == "Heart":
            pic ='🂴'
        if self.suit == "Five" and self.picture == "Heart":
            pic ='🂵'
        if self.suit == "Six" and self.picture == "Heart":
            pic ='🂶'
        if self.suit == "Seven" and self.picture == "Heart":
            pic ='🂷'
        if self.suit == "Eight" and self.picture == "Heart":
            pic ='🂸'
        if self.suit == "Nine" and self.picture == "Heart":
            pic ='🂹'
        if self.suit == "Ten" and self.picture == "Heart":
            pic ='🂺'
        if self.suit == "K" and self.picture == "Heart":
            pic ='🂾'
        if self.suit == "J" and self.picture == "Heart":
            pic ='🂻'
        if self.suit == "Q" and self.picture == "Heart":
            pic ='🂽'
        if self.suit == "A" and self.picture == "Diamonds":
            pic ='🃁'
        if self.suit == "Two" and self.picture == "Diamonds":
            pic ='🃂'
        if self.suit == "Three" and self.picture == "Diamonds":
            pic ='🃃'
        if self.suit == "Four" and self.picture == "Diamonds":
            pic ='🃄'
        if self.suit == "Five" and self.picture == "Diamonds":
            pic ='🃅'
        if self.suit == "Six" and self.picture == "Diamonds":
            pic ='🃆'
        if self.suit == "Seven" and self.picture == "Diamonds":
            pic ='🃇'
        if self.suit == "Eight" and self.picture == "Diamonds":
            pic ='🃈'
        if self.suit == "Nine" and self.picture == "Diamonds":
            pic ='🃉'
        if self.suit == "Ten" and self.picture == "Diamonds":
            pic ='🃊'
        if self.suit == "K" and self.picture == "Diamonds":
            pic ='🃎'
        if self.suit == "J" and self.picture == "Diamonds":
            pic ='🃍'
        if self.suit == "Q" and self.picture == "Diamonds":
            pic ='🃋'
        if self.suit =="A" and self.picture =="Clubs":
            pic='🃑'
        if self.suit == "Two" and self.picture == "Clubs":
            pic ='🃒'
        if self.suit =="Three" and self.picture =="Clubs":
            pic='🃓'
        if self.suit =="Four" and self.picture =="Clubs":
            pic='🃔'
        if self.suit =="Five" and self.picture =="Clubs":
            pic='🃕'
        if self.suit =="Six" and self.picture =="Clubs":
            pic='🃖'
        if self.suit =="Seven" and self.picture =="Clubs":
            pic='🃗'
        if self.suit =="Eight" and self.picture =="Clubs":
            pic='🃘'
        if self.suit =="Nine" and self.picture =="Clubs":
            pic='🃙'
        if self.suit =="Ten" and self.picture =="Clubs":
            pic='🃚'
        if self.suit =="K" and self.picture =="Clubs":
            pic='🃞'
        if self.suit =="J" and self.picture =="Clubs":
            pic='🃝'
        if self.suit =="Q" and self.picture =="Clubs":
            pic='🃛'
        return f'{pic} | {self.suit} of {self.picture}'

    __repr__ = __str__



