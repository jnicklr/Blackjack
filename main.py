# Bibliotecas:
from logo import logo
from blackjack import Blackjack

# Jogo BlackHack:
bj = Blackjack()
while_condition = 'y'
points = 0

while True:
    if bj.continue_playing(while_condition) == False:
        print("Thanks for playing <3")
        break
    else:
        print(logo)
        user_deck = bj.user_cards()
        computer_deck = bj.computer_cards()
        print(f"Your cards: {user_deck}")
        print(f"Computer's first card: {computer_deck[0]}")
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        user_deck = bj.get_another_card(get_card)
        if bj.verify_if_over21() == False:
            print(f"Your final hand: {user_deck}")
            print("You Lose. Your points exceed 21.")
            while_condition = 'n'
            break
        else:
            print(f"Your final hand: {user_deck}")
            print(f"Computer's final hand: {computer_deck}")
            stats = bj.verify_victory()
            if stats == True:
                print("You Won")
            elif stats == False:
                print("You Lose")
            else:
                print("It's a Drawn ")
        bj.user = []
        bj.computer = []
        while_condition = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")