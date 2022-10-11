import copy

from deck import Deck
from card import Card
from rang import Rang
from dealers import Dealer
from users import User
from  game import Game
from acecard import Acecard
from facecard import Facecard
from scores import Score

def test_unique(deck):
    deck.init_deck()
    card = deck.next()
    while True:
        card2 = deck.next()
        assert card!=card2,"Duplicate cards"
        if card2 == []:
            break

def test_draw(deck):
    cards = []
    cards2 = []
    print("First Draw")
    deck2=copy.deepcopy(deck)
    deck2.init_deck()
    while True:
        card = deck2.next()
        cards.append(card)
        if card == []:
            break
        else:
            print(card)
    print("Second Draw")
    deck2 = copy.deepcopy(deck)
    deck2.init_deck()
    while True:
        card = deck2.next()
        cards2.append(card)
        if card == []:
            break
        else:
            print(card)
    cnt = 0
    for x in range(len(cards)):
        if cards[x] != cards2[x]:
            cnt +=1
    assert cnt!=0,"The draws are identical"
    print("Number of different cards "+str(cnt))


def test_values():
    assert(Card("Heart",Rang(2,2),"Two").rang.soft==2)
    assert (Card("Heart", Rang(2,2), "Two").rang.hard == 2)
    assert (Card("Heart", Rang(3,3), "Three").rang.soft == 3)
    assert (Card("Heart", Rang(3,3), "Three").rang.hard == 3)
    assert (Card("Heart", Rang(4,4), "Four").rang.soft == 4)
    assert (Card("Heart", Rang(4,4), "Four").rang.hard== 4)
    assert (Card("Heart", Rang(5,5), "Five").rang.soft == 5)
    assert (Card("Heart", Rang(5,5), "Five").rang.hard == 5)
    assert (Card("Heart", Rang(6,6), "Six").rang.soft == 6)
    assert (Card("Heart", Rang(6,6), "Six").rang.hard == 6)
    assert (Card("Heart", Rang(7,7), "Seven").rang.soft == 7)
    assert (Card("Heart", Rang(7,7), "Seven").rang.hard == 7)
    assert (Card("Heart", Rang(8,8), "Eight").rang.soft == 8)
    assert (Card("Heart", Rang(8,8), "Eight").rang.hard == 8)
    assert (Card("Heart", Rang(9,9), "Nine").rang.soft == 9)
    assert (Card("Heart", Rang(9,9), "Nine").rang.hard == 9)
    assert (Card("Heart", Rang(10,10), "Ten").rang.soft == 10)
    assert (Card("Heart", Rang(10,10), "Ten").rang.hard == 10)
    assert (Facecard("Heart", Rang(10, 10), "J").rang.soft == 10)
    assert (Facecard("Heart", Rang(10, 10), "J").rang.hard == 10)
    assert (Facecard("Heart", Rang(10, 10), "Q").rang.soft == 10)
    assert (Facecard("Heart", Rang(10, 10), "Q").rang.hard == 10)
    assert (Facecard("Heart", Rang(10, 10), "K").rang.soft == 10)
    assert (Facecard("Heart", Rang(10, 10), "K").rang.hard == 10)
    assert (Acecard("Heart", Rang(1, 11), "Ten").rang.soft == 1)
    assert (Acecard("Heart", Rang(1,11), "Ten").rang.hard == 11)


    assert (Card("Clubs", Rang(2, 2), "Two").rang.soft == 2)
    assert (Card("Clubs", Rang(2, 2), "Two").rang.hard == 2)
    assert (Card("Clubs", Rang(3, 3), "Three").rang.soft == 3)
    assert (Card("Clubs", Rang(3, 3), "Three").rang.hard == 3)
    assert (Card("Clubs", Rang(4, 4), "Four").rang.soft == 4)
    assert (Card("Clubs", Rang(4, 4), "Four").rang.hard == 4)
    assert (Card("Clubs", Rang(5, 5), "Five").rang.soft == 5)
    assert (Card("Clubs", Rang(5, 5), "Five").rang.hard == 5)
    assert (Card("Clubs", Rang(6, 6), "Six").rang.soft == 6)
    assert (Card("Clubs", Rang(6, 6), "Six").rang.hard == 6)
    assert (Card("Clubs", Rang(7, 7), "Seven").rang.soft == 7)
    assert (Card("Clubs", Rang(7, 7), "Seven").rang.hard == 7)
    assert (Card("Clubs", Rang(8, 8), "Eight").rang.soft == 8)
    assert (Card("Clubs", Rang(8, 8), "Eight").rang.hard == 8)
    assert (Card("Clubs", Rang(9, 9), "Nine").rang.soft == 9)
    assert (Card("Clubs", Rang(9, 9), "Nine").rang.hard == 9)
    assert (Card("Clubs", Rang(10, 10), "Ten").rang.soft == 10)
    assert (Card("Clubs", Rang(10, 10), "Ten").rang.hard == 10)
    assert (Facecard("Clubs", Rang(10, 10), "J").rang.soft == 10)
    assert (Facecard("Clubs", Rang(10, 10), "J").rang.hard == 10)
    assert (Facecard("Clubs", Rang(10, 10), "Q").rang.soft == 10)
    assert (Facecard("Clubs", Rang(10, 10), "Q").rang.hard == 10)
    assert (Facecard("Clubs", Rang(10, 10), "K").rang.soft == 10)
    assert (Facecard("Clubs", Rang(10, 10), "K").rang.hard == 10)
    assert (Acecard("Clubs", Rang(1, 11), "Ten").rang.soft == 1)
    assert (Acecard("Clubs", Rang(1, 11), "Ten").rang.hard == 11)

    assert (Card("Diamonds", Rang(2, 2), "Two").rang.soft == 2)
    assert (Card("Diamonds", Rang(2, 2), "Two").rang.hard == 2)
    assert (Card("Diamonds", Rang(3, 3), "Three").rang.soft == 3)
    assert (Card("Diamonds", Rang(3, 3), "Three").rang.hard == 3)
    assert (Card("Diamonds", Rang(4, 4), "Four").rang.soft == 4)
    assert (Card("Diamonds", Rang(4, 4), "Four").rang.hard == 4)
    assert (Card("Diamonds", Rang(5, 5), "Five").rang.soft == 5)
    assert (Card("Diamonds", Rang(5, 5), "Five").rang.hard == 5)
    assert (Card("Diamonds", Rang(6, 6), "Six").rang.soft == 6)
    assert (Card("Diamonds", Rang(6, 6), "Six").rang.hard == 6)
    assert (Card("Diamonds", Rang(7, 7), "Seven").rang.soft == 7)
    assert (Card("Diamonds", Rang(7, 7), "Seven").rang.hard == 7)
    assert (Card("Diamonds", Rang(8, 8), "Eight").rang.soft == 8)
    assert (Card("Diamonds", Rang(8, 8), "Eight").rang.hard == 8)
    assert (Card("Diamonds", Rang(9, 9), "Nine").rang.soft == 9)
    assert (Card("Diamonds", Rang(9, 9), "Nine").rang.hard == 9)
    assert (Card("Diamonds", Rang(10, 10), "Ten").rang.soft == 10)
    assert (Card("Diamonds", Rang(10, 10), "Ten").rang.hard == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "J").rang.soft == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "J").rang.hard == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "Q").rang.soft == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "Q").rang.hard == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "K").rang.soft == 10)
    assert (Facecard("Diamonds", Rang(10, 10), "K").rang.hard == 10)
    assert (Acecard("Diamonds", Rang(1, 11), "Ten").rang.soft == 1)
    assert (Acecard("Diamonds", Rang(1, 11), "Ten").rang.hard == 11)

    assert (Card("Spades", Rang(2, 2), "Two").rang.soft == 2)
    assert (Card("Spades", Rang(2, 2), "Two").rang.hard == 2)
    assert (Card("Spades", Rang(3, 3), "Three").rang.soft == 3)
    assert (Card("Spades", Rang(3, 3), "Three").rang.hard == 3)
    assert (Card("Spades", Rang(4, 4), "Four").rang.soft == 4)
    assert (Card("Spades", Rang(4, 4), "Four").rang.hard == 4)
    assert (Card("Spades", Rang(5, 5), "Five").rang.soft == 5)
    assert (Card("Spades", Rang(5, 5), "Five").rang.hard == 5)
    assert (Card("Spades", Rang(6, 6), "Six").rang.soft == 6)
    assert (Card("Spades", Rang(6, 6), "Six").rang.hard == 6)
    assert (Card("Spades", Rang(7, 7), "Seven").rang.soft == 7)
    assert (Card("Spades", Rang(7, 7), "Seven").rang.hard == 7)
    assert (Card("Spades", Rang(8, 8), "Eight").rang.soft == 8)
    assert (Card("Spades", Rang(8, 8), "Eight").rang.hard == 8)
    assert (Card("Spades", Rang(9, 9), "Nine").rang.soft == 9)
    assert (Card("Spades", Rang(9, 9), "Nine").rang.hard == 9)
    assert (Card("Spades", Rang(10, 10), "Ten").rang.soft == 10)
    assert (Card("Spades", Rang(10, 10), "Ten").rang.hard == 10)
    assert (Facecard("Spades", Rang(10, 10), "J").rang.soft == 10)
    assert (Facecard("Spades", Rang(10, 10), "J").rang.hard == 10)
    assert (Facecard("Spades", Rang(10, 10), "Q").rang.soft == 10)
    assert (Facecard("Spades", Rang(10, 10), "Q").rang.hard == 10)
    assert (Facecard("Spades", Rang(10, 10), "K").rang.soft == 10)
    assert (Facecard("Spades", Rang(10, 10), "K").rang.hard == 10)
    assert (Acecard("Spades", Rang(1, 11), "Ten").rang.soft == 1)
    assert (Acecard("Spades", Rang(1, 11), "Ten").rang.hard == 11)


def main():
    cards = []
    cards.append(Card("Heart",Rang(2,2),"Two"))
    cards.append(Card("Heart", Rang(3,3), "Three"))
    cards.append(Card("Heart",Rang(4,4),"Four"))
    cards.append(Card("Heart", Rang(5, 5), "Five"))
    cards.append(Card("Heart", Rang(6,6), "Six"))
    cards.append(Card("Heart", Rang(7,7), "Seven"))
    cards.append(Card("Heart", Rang(8,8), "Eight"))
    cards.append(Card("Heart", Rang(9,9), "Nine"))
    cards.append(Card("Heart", Rang(10,10), "Ten"))
    cards.append(Facecard("Heart", Rang(10, 10), "J"))
    cards.append(Facecard("Heart", Rang(10, 10), "Q"))
    cards.append(Facecard("Heart", Rang(10, 10), "K"))
    cards.append(Acecard("Heart", Rang(1,11), "A"))

    cards.append(Card("Diamonds", Rang(2, 2), "Two"))
    cards.append(Card("Diamonds", Rang(3, 3), "Three"))
    cards.append(Card("Diamonds", Rang(4, 4), "Four"))
    cards.append(Card("Diamonds", Rang(5, 5), "Five"))
    cards.append(Card("Diamonds", Rang(6, 6), "Six"))
    cards.append(Card("Diamonds", Rang(7, 7), "Seven"))
    cards.append(Card("Diamonds", Rang(8, 8), "Eight"))
    cards.append(Card("Diamonds", Rang(9, 9), "Nine"))
    cards.append(Card("Diamonds", Rang(10, 10), "Ten"))
    cards.append(Facecard("Diamonds", Rang(10, 10), "J"))
    cards.append(Facecard("Diamonds", Rang(10, 10), "Q"))
    cards.append(Facecard("Diamonds", Rang(10, 10), "K"))
    cards.append(Acecard("Diamonds", Rang(1, 11), "A"))

    cards.append(Card("Spades", Rang(2, 2), "Two"))
    cards.append(Card("Spades", Rang(3, 3), "Three"))
    cards.append(Card("Spades", Rang(4, 4), "Four"))
    cards.append(Card("Spades", Rang(5, 5), "Five"))
    cards.append(Card("Spades", Rang(6, 6), "Six"))
    cards.append(Card("Spades", Rang(7, 7), "Seven"))
    cards.append(Card("Spades", Rang(8, 8), "Eight"))
    cards.append(Card("Spades", Rang(9, 9), "Nine"))
    cards.append(Card("Spades", Rang(10, 10), "Ten"))
    cards.append(Facecard("Spades", Rang(10, 10), "J"))
    cards.append(Facecard("Spades", Rang(10, 10), "Q"))
    cards.append(Facecard("Spades", Rang(10, 10), "K"))
    cards.append(Acecard("Spades", Rang(1, 11), "A"))

    cards.append(Card("Clubs", Rang(2, 2), "Two"))
    cards.append(Card("Clubs", Rang(3, 3), "Three"))
    cards.append(Card("Clubs", Rang(4, 4), "Four"))
    cards.append(Card("Clubs", Rang(5, 5), "Five"))
    cards.append(Card("Clubs", Rang(6, 6), "Six"))
    cards.append(Card("Clubs", Rang(7, 7), "Seven"))
    cards.append(Card("Clubs", Rang(8, 8), "Eight"))
    cards.append(Card("Clubs", Rang(9, 9), "Nine"))
    cards.append(Card("Clubs", Rang(10, 10), "Ten"))
    cards.append(Facecard("Clubs", Rang(10, 10), "J"))
    cards.append(Facecard("Clubs", Rang(10, 10), "Q"))
    cards.append(Facecard("Clubs", Rang(10, 10), "K"))
    cards.append(Acecard("Clubs", Rang(1, 11), "A"))

    deck = Deck(cards)
    dealer= Dealer(deck)
    deck2=copy.deepcopy(deck)
    test_unique(deck2)
    test_draw(deck)
    test_values()
    username = input("Enter your name:")
    user = User(username,100)
    game = Game(dealer,user)
    game.play()
    score=Score("scores.txt")
    score.write_scores()


main()



