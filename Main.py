# ---------------------------------------------------------------------------- #
#                                   Main File                                  #
# ---------------------------------------------------------------------------- #

from Classes import Card, Deck, Player, Chips, Hand

# ----------------------------- Global Variables ----------------------------- #
game_on = True

# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #

def take_bet(chips):
    while True:
            try:
                chips.bet = int(input('How much money would you like to bet with?\n'))
            except:
                print('Please type a valid integer\n')
                continue
            if chips.bet < 0:
                print('You cannot bet negative money\n')
                continue
            elif chips.bet  == 0:
                print('Must bet at least $1.\n')
                continue
            elif chips.bet > chips.total:
                print("Your bet cannot exceed the amount of chips you own!\n")
            else:
                break

def hit(deck,hand):
    hand.add_cards(deck.deal_one())
    hand.ace_flip()

def hit_or_stand(deck,hand):
    global game_on
    while True:
        hs = input('Please type H for hit, and S for Stand.\n')

        if hs[0].upper() == 'H':
            hit(deck,hand)
        
        elif hs[0].upper() == 'S':
            game_on = False
        
        else:
            print('Incorrect Input.\n')
            continue
        break

def show_card(player,dealer):
    print("\nThe Dealer's Hand is:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nThe Player's Hand is:", *player.cards, sep='\n ')
    print("The Player's Hand is equal in value to: ", player.value)

def show_all_cards(player,dealer):
    print("\nThe Dealer's Hand is:", *dealer.cards, sep='\n ')
    print("The Dealer's Hand is equal in value to: ", dealer.value)
    print("\nThe Player's Hand is: ", *player.cards, sep = '\n ')
    print("The Player's Hand is equal in value to: ", player.value)



def player_win_turn(player,dealer,chips):
        print("The Player wins!")
        chips.win_turn() 

def player_bust(player,dealer,chips):
    print("The Player Busts!")
    chips.lose_turn()

def dealer_win_turn(player,dealer,chips):
    print("The Dealer Wins!")
    chips.lose_turn()

def dealer_bust(player,dealer,chips):
    print("The Dealer Busts!")
    chips.win_turn()

def push(player,dealer):
    print("Tie! game is a push!")

def starting_money():
    ask = 1
    while ask == 1:
            try:
                total = int(input('How much money are you here with today?\n'))
            except ValueError:
                print('Please type a valid integer\n')
                continue
            if total < 0:
                print('You cannot have negative money\n')
                continue
            elif total  == 0:
                print('Minimum playable amount is $1.\n')
                continue
            else:
                ask = 0
                return total


if __name__ == "__main__":
    print("Let's Play Some Blackjack!\n")
        
    ask = input("Would you like me to explain the rules of the game?\nPlease Enter Y / N:\n")

    if ask[0].upper() == 'Y':
        print("\nGoal of the game is for the player's hand to get as close to 21 without going over it, all the while having more points than the dealer.")
        print("Each numbered card is worth the same amount of points as its value (e.g. Four of Hearts is equal to 4 points, suits don't matter!).")
        print("Each face card is worth 10 points, aces are a special case in which they're worth either 11 or 1 points, depending on what benefits the player more!")
        print("At the start of each round, the player makes their bet and then may choose to hit or stand:\nHit means the dealer adds another card to the players hand, increasing in value, but be careful not to go over 21!\nStand means to stop adding cards and go through with the bet.")
        print("Enjoy the game!\n\n\n")

# ------------------------- setups the players chips, do outside the loop so doesn't reset chips counter ------------------------- #
        
    players_chips = Chips(total=starting_money())

    
    while True:
        # ----------------------------- opening statement ---------------------------- #
        
        
# ----------------------- creates deck and shuffles it ----------------------- #

        deck = Deck()
        deck.shuffle_cards()

# ---------------------- creates player and dealer hands --------------------- #

        players_hand = Hand()
        players_hand.add_cards(deck.deal_one())
        players_hand.add_cards(deck.deal_one())

        dealers_hand = Hand()
        dealers_hand.add_cards(deck.deal_one())
        dealers_hand.add_cards(deck.deal_one())

# ----------------------------- player makes bet ----------------------------- #

        take_bet(players_chips)

# -------------- show the player's card but hide one of dealers -------------- #
        
        show_card(players_hand,dealers_hand)

        while game_on:

            hit_or_stand(deck,players_hand)

            show_card(players_hand,dealers_hand)


            if players_hand.value > 21:
                player_bust(players_hand, dealers_hand, players_chips)
                break

# --------------- dealer has to hit if its hand is less than 17 -------------- #

        if players_hand.value <= 21:

            while dealers_hand.value < 17:
                hit(deck, dealers_hand)

# ------------ show all cards before calculating winning scenarios ----------- #

            show_all_cards(players_hand, dealers_hand)

            if dealers_hand.value > 21:
                dealer_bust(players_hand, dealers_hand, players_chips)

            elif dealers_hand.value > players_hand.value:
                dealer_win_turn(players_hand, dealers_hand, players_chips)

            elif dealers_hand.value < players_hand.value:
                player_win_turn(players_hand, dealers_hand, players_chips)

            else:
                push(players_hand, dealers_hand)

# ------------------ remind Player how many chips they have ------------------ #
        print("\nPlayer's current chips are: ", players_chips.total)
        
# -------------------------------- play again? ------------------------------- #

        another_round = input("Would you like to play again? Y or N?\n")

        if another_round[0].upper() == 'Y':
            if players_chips.total > 0:
                game_on = True
                continue
            else:
                print("You're broke, go home!")
                break
        else:
            print("Thanks for coming to play!")
            break 