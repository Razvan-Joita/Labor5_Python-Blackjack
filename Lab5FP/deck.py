import random


class Deck:

    def __init__(self,card_list):
        self.__card_list = card_list

    @property
    def card_list(self):
        return self.__card_list

    @card_list.setter
    def card_list(self,card_list):
        self.__card_list = card_list

    def next(self):
        if len(self.__card_list) == 0:
            return []
        card = self.card_list[0]
        self.card_list = self.__card_list[1:]
        return card

    def shuffle(self):
        new_list = []
        while len(self.__card_list)>0:
            poz = random.choice(range(0,len(self.__card_list)))
            new_list.append(self.__card_list[poz])
            del self.__card_list[poz]

        self.__card_list = new_list
        return self.__card_list

    def init_deck(self):
        self.shuffle()

