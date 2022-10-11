from deck import Deck

class Dealer:
    def __init__(self,deck):
        self.__deck = deck
        self.__current_deck = deck

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self,deck):
        self.__deck = deck

    def next_card(self):
        card = self.__current_deck.next()
        return card

    def new_deck(self):
        self.__current_deck = self.__deck
        self.__current_deck.init_deck()
