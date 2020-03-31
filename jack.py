from random import shuffle


suits = ("Hearts", "Diamonds", "Spades", "Club")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "King", "Queen", "Jack", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "King": 10, "Jack": 10, "Queen": 10, "Ace": 11}
playing = True


class card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has : " + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def loss_bet(self):
        self.total -= self.bet


def take_bets(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet to be placed : "))
        except:
            print("Please enter a integer value")
        else:
            if chips.bet > chips.total:
                print(
                    f"You did not have sufficient balance you have only {chips.total}")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Do you want to hit or stand ?(h or s)")
        if x.lower() == 'h':
            hit(deck, hand)
        elif x.lower() == 's':
            print("Player stands dealer turns")
            playing = False
        else:
            print("Enter h or s only")
            continue
        break


def show_some(player, dealer):
    print("Dealer's Hand : ")
    print("one card is hidden!")
    print(dealer.cards[1])
    print("\n")
    print("Player's Hand :")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("Dealer's Hand : ")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's Hand :")
    for card in player.cards:
        print(card)


def player_bust(player, dealer, chips):
    print("Player busts")
    chips.loss_bet()


def player_win(player, dealer, chips):
    print("Player Wins")
    chips.win_bet()


def dealer_bust(player, dealer, chips):
    print("Dealer busts player wins")
    chips.win_bet()


def dealer_win(player, dealer, chips):
    print("Dealer wins")
    chips.loss_bet()


def push(player, dealer):
    print("Tie")


while True:
    print("Welcome to BlackJAck")
    deck = deck()
    deck.shuffle()

    player_hand = hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = chips()

    take_bets(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_win(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

        new_game = input("Do you want to play again ?(y or n) :")
        if new_game.lower() == 'y':
            playing = True
            continue
        else:
            print("THANK YOU")
            break
