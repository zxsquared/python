import random
# Global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


# Card class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card passed in from Deck.deal --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        # Track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            print(chips.total)
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print('Sorry! Please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have {chips.total}')
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    #global playing

    while True:
        x = input('Hit or stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower == 's':
            print('Player Stand. Dealers turn')
            playing == False
        else:
            print('please enter h or s!')
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH')


while True:
    # Make an opening statment
    print('Welcome to blackjack!!')
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up player chips
    player_chips = Chips()
    # Prompt player for bet
    take_bet(player_chips)
    # Show cards (but one of the dealer's cards is hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for player to hit or stand
        hit_or_stand(deck, player_hand)
        # Show cards (but one of the dealer's cards is hidden)
        show_some(player_hand, dealer_hand)
        # If player exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        # If player hasn't busted, play Dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning senarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        # Inform player of their chips total
        print(f'\nPlayer total chips are at: {player_chips.total}')
        # Ask to play again
        new_game = input('Would you like to play another hand? y/n')

        if new_game[0].lower == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing')
            break
# That's the game code
