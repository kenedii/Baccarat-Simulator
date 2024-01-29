from deck_of_cards import deck_of_cards

decks = 8  # Number of Decks to use in the shoe



def cbaccarat_rules(card):  # Takes a card object and returns its value in Baccarat.
    if card.rank >= 10:
        value = 0  # 10 or above cards are worth zero
        return value
    else:
        return card.rank  # Aces are one and 2-9 cards are their own rank in deck-of-cards.py.

def baccarat_rules(value):  # Takes a number and returns its value in Baccarat.
    if value == 10:
        return 0
    elif value > 10:
        return int(str(value)[1])
    elif value < 10:
        return value


def game():
    deck = deck_of_cards.DeckOfCards() #Initialize the deck
    for i in range(decks):
        deck.add_deck()  # Adds a new deck to the initial deck object
        deck.shuffle_deck()

    player = cbaccarat_rules(deck.give_random_card()) + cbaccarat_rules(deck.give_random_card())
    banker = cbaccarat_rules(deck.give_random_card()) + cbaccarat_rules(deck.give_random_card())

    if 0 <= player <= 5:  # Player draws one more card 0-5
        player += cbaccarat_rules(deck.give_random_card())
        if 0 <= banker <= 2:  # Banker draws one more card 0-2
            banker += cbaccarat_rules(deck.give_random_card())
        elif (banker == 3) & (player != 8):
            banker += cbaccarat_rules(deck.give_random_card())
        elif (banker == 4) & (2 <= player <= 7):
            banker += cbaccarat_rules(deck.give_random_card())
        elif (banker == 5) & (4 <= player <= 7):
            banker += cbaccarat_rules(deck.give_random_card())
        elif (banker == 6) & (6 <= player <= 7):
            banker += cbaccarat_rules(deck.give_random_card())

    elif (player == 6) or (player == 7):  # Player stands
        if 0 < banker <= 5:  # Banker draws one more card 0-5
            banker += cbaccarat_rules(deck.give_random_card())

    player = baccarat_rules(player)
    banker = baccarat_rules(banker)

    if banker > player:  # If the banker's score is greater
        return ['Banker', player, banker]

    elif player > banker:  # If the players score is greater
        return ['Player', player, banker]

    elif banker == player:  # If the player and the banker tie
        return ['Tie', player, banker]


def simulate_games(games=2):  # Simulate multiple Baccarat games
    banker = 0
    player = 0
    tie = 0
    for i in range(games):
        rungame = game()
        if rungame[0] == 'Banker':
            player += 1
        elif rungame[0] == 'Player':
            banker += 1
        if rungame[0] == 'Tie':
            tie += 1

    return [player, banker, tie]

