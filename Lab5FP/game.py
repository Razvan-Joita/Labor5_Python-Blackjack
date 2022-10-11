from datetime import date
from scores import Score

class Game:
    def __init__(self,dealer,user):
        self.__dealer = dealer
        self.__user= user

    @property
    def dealer(self):
        return self.__dealer

    @dealer.setter
    def dealer(self,dealer):
        self.__dealer = dealer

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self,user):
        self.__user = user

    def play(self):
        f = open("history.txt","a")
        text = "New game for user " + self.__user.name + "\n"
        round = 1
        while round <=5:
            bet = int(input("Place your bet:"))
            while bet > self.__user.money:
                bet = int(input("Amount exceeded.Enter another bet"))
            user_score = 0
            text += "Bet for round " + str(round) + ": " +str(bet) + "\n"

            self.__dealer.new_deck()
            while user_score<=21:
                card = self.__dealer.next_card()
                print(card)
                if card.suit == "A":
                    value = int(input("Choose your preference:1 or 11"))
                else:
                    value = card.rang.soft
                user_score = user_score + value
                print(" Current score: "+ str(user_score))
                if user_score > 21:
                    break
                again = int(input("Do you want another card?(0 or 1)"))
                if again == 0:
                    break
            if user_score >21:
                print("You lost ")
                self.__user.money = self.__user.money - bet
                text += "Lost round " + str(round) + "New amount: " + str(self.user.money) + "\n"
                if self.__user.money == 0:
                    print("No money left!")
                    break
                again = int(input("Do you want another round?(0 or 1)"))
                if again == 0 :
                    break
                else:
                    round+=1
                    continue
            else:
                dealer_score = 0
                self.__dealer.new_deck()
                while user_score<=21:
                    card = self.__dealer.next_card()
                    if card.suit == "A":
                       if dealer_score <= 10:
                           value = 11
                       else:
                           value = 10
                    else:
                        value = card.rang.soft
                    dealer_score = dealer_score + value
                    if dealer_score >=16:
                        break
                print("Dealer score: " + str(dealer_score))

                if dealer_score >21 or user_score>dealer_score:
                    print("You win!")
                    self.__user.money +=bet
                    text += "Win round " + str(round) + "New amount: " + str(self.user.money) + "\n"
                elif user_score == dealer_score:
                    print("Draw")
                    text += "Draw round " + str(round) + "New amount: " + str(self.user.money) + "\n"
                elif user_score<dealer_score:
                    print("You lost!")
                    self.__user.money -=bet
                    text += "Lost round " + str(round) + "New amount: " + str(self.user.money) + "\n"
                if self.__user.money == 0:
                    print("No money left!")
                    break
                again = int(input("Do you want another round?(0 or 1)"))
                if again == 0:
                    break
                else:
                    round += 1
                    continue
        print("Final amount: " + str(self.__user.money))
        text += "Final amount: " + str(self.__user.money) + "\n"
        f.write(text)
        f.close()
        score = Score("scores.txt")
        if round ==6:
            round = 5
        score.add_score(round,self.__user.name,self.__user.money)

