import random
import time


deck_copy = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
the_deck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
deck_values = {'A':11,'K':10,'Q':10,'J':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'a':1}
#lowercase 'a' represents an Ace with a value of 1, while uppercase 'A' represents a value of 11
#After each hand, the deck is "shuffled" and recompiled by copying the values of deck_copy to replace the exhausted list, the_deck

my_hand = []
dealers_hand = []
my_value = []
dealers_value = []
### the 'hand' lists are used to represent printable values to show a player what they have and are used to identify keys in the {deck_values} dictionary
### the value lists are used to hold the numeric value of each card, and are summed later in the program to identify proximity to 21



def start_game():
    print ('Welcome to BlackZach\'s Casino!\n'
           '-\n'
           'We\'ll start you with 500 coins.\n'
           '-\n'
           'You must bet 50 to play a round, and you have the option to double the bet after the first cards are dealt'
           'Accumulate 1,500 coins to win the game.')
    start_choice()
### initializes the game with simple description and then sends to start_choice

def start_choice():
    the_deck = deck_copy.copy()
    begin_game = input('\n\n'
          'Would you like to play? (y/n)\n')
    if begin_game == 'y':
        its_showtime()
    elif begin_game == 'n':
        print('Thanks for stopping by, see you next time!')
        quit()
    else:
        start_choice()
### allows users to quit or play





def grab_card():
    total_cards = len(the_deck)-1
    max_card = int(total_cards)
    draw = random.randint(0,max_card)
    card_name = the_deck[draw]
    the_deck.pop(draw)
    return(card_name)
### a function used often, that calculates the number of cards in the_deck and then randomly picks one
# (as if the deck were shuffled) and then removes the card from the list and returns card_name



def dealer_draw():
    card = grab_card()
    dealers_hand.append(card)
    dealers_value.append(deck_values.get(card))
    time.sleep(.5)
    print('Dealer drew a',card)
    time.sleep(1)

def player_draw():
    card = grab_card()
    my_hand.append(card)
    my_value.append(deck_values.get(card))
    time.sleep(.5)
    print('You drew a',card)
    time.sleep(1)
### used to call grab_card() and append the card name to your hand list and the card value to your value list
# then prints a message telling you what card you've drawn

def first_cards():
    player_draw()
    player_draw()
    dealer_draw()
    dealer_draw()
    on_the_table()
### gives the player their first two cards and gives the dealer their first two cards (potentially one face down, unsure on blackjack rules)

def on_the_table():
    print('\n\n\nYour Hand:',my_hand)
    print(sum(my_value))
    time.sleep(2)
    print('\nDealer\'s Hand:',dealers_hand)
    print(sum(dealers_value))
### function to show the player and dealer's hands during play (might need to remove the showing of one of the dealer's cards
    

def ace_check(list,dict):
    if 'A' in list:
        list.pop('A')
        list.append('a')
    else:
        pass
    if sum(dict) > 21:
        ace_check(list,dict)
    else:
        pass
### checks for aces when a player busts, if there is one, it replaces the value of 11 with the value of 1





def hit_stay():
    time.sleep(2)
    choice = input('\n\n--Hit (h) or Stay (s)?--\n')
    if choice == 'h':
        player_draw()
        on_the_table()
        value = sum(my_value)
        if value < 21:
            pass
        elif value > 21:
            ace_check(my_hand,my_value)
            if sum(my_value) < 22:
                hit_stay()
            elif sum(my_value) > 21:
                print('\nBUST\n')
                dealers_turn()
            return
        elif value == 21:
            print('BLACKJACK\n')
            time.sleep(2)
            print('Let\'s see what the Dealer has...')
            dealers_turn()
            return
        hit_stay()
    elif choice == 's':
        print('\nStayed.\n')
        time.sleep(1)
        print('Dealer\'s Turn...')
        time.sleep(2)
        dealers_turn()
    else:
        print('Invalid Input: Try again...\n')
        time.sleep(2)
        hit_stay()
### this function offers the player an opportunity to add new cards to their hand or stay.  This function also stops the player 
# when they bust or hit 21




def dealers_turn():
    if sum(dealers_value) < 17:
        dealer_draw()
        dealers_turn()
    elif sum(dealers_value) > 17 & sum(dealers_value) < 21:
        who_wins()
    elif sum(dealers_value) == 21:
        print('BLACKJACK')
        time.sleep(.5)
        print('BLACKJACK')
        time.sleep(.5)
        print('BLACKJACK')
        time.sleep(.5)
        who_wins()
    elif sum(dealers_value) > 21:
        ace_check(dealers_hand,dealers_value)
        if sum(dealers_value) < 22:
            dealers_turn()
        elif sum(dealers_value) > 21:
            who_wins()
### this function activates after the player busts, gets blackjack, or stays. forces the dealer to draw until the value of cards exceeds 17.
# apparently true blackjack would suggest that a dealer hand 17 or over with an ACE needs to continue drawing, might add that later.
          
            

def who_wins():
    p = sum(my_value)
    d = sum(dealers_value)
    if p < 22 & p > d:
        player_wins()
    elif d < 22 & d > p:
        dealer_wins()
    elif d > 21 & p > 21:
        dealer_wins()
    elif d == p:
        draw()
### determines the winner of the game, might need to add certain end game scenarios. Might also need to reflect rule that states
# 21 vs 21 is a draw, but getting dealt a 21 off rip is a win for the player.
        
        
def player_wins():
    print('\n***You Win!***\n')
    time.sleep(2)
    restart()

def dealer_wins():
    print('\n***Dealer Wins!***\n')
    time.sleep(2)
    restart()

def draw():
    print('***It\'s a Draw!***')
    time.sleep(2)
    restart()
### simple win conditions with restart




def its_showtime():
    first_cards()
    hit_stay()
### dictates order of events with larger functions

def restart():
    the_deck = deck_copy.copy()
    start_choice()
### resets the_deck list and restarts the function chain

start_game()
### calls the game start function
