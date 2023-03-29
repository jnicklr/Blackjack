# Bibliotecas:
import random

# Classe:
class Blackjack:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.user = []
        self.computer = []

    def get_another_card(self, string):
        if string == 'y':
            user_deck = self.user
            user_deck.append(random.choice(self.cards))
            self.user = user_deck
            return user_deck
        else:
            user_deck = self.user
            return user_deck

    def user_cards(self):
        user_deck = []
        for i in range(0, 2):
            user_deck.append(random.choice(self.cards))
            self.user.append(user_deck[i])
        return user_deck
    
    def computer_cards(self):
        computer_deck = []
        for i in range(0, 2):
            computer_deck.append(random.choice(self.cards))
            self.computer.append(computer_deck[i])
        return computer_deck

    def verify_if_over21(self):
        user_deck = self.user
        user_points = 0
        for i in user_deck:
            user_points += i
        if user_points > 21:
            return False
        else:
            return True
    
    def verify_victory(self):
        user_deck = self.user
        computer_deck = self.computer
        user_points = 0
        computer_points = 0
        for i in user_deck:
            user_points += i
        for i in computer_deck:
            computer_points += i
        if user_points > computer_points:
            return True
        elif user_points == computer_points:
            return 2
        else:
            return False

    def continue_playing(self, string):
        if string == 'y':
            return True
        else:
            return False