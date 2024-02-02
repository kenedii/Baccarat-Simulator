A baccarat game in Python. Draws from 8 decks in shoe and decks get shuffled every game for randomness.

Dependencies: pip install deck-of-cards
https://pypi.org/project/deck-of-cards/

Functions:

def cbaccarat_rules(card):  # Takes a card object (deck-of-cards.py) and returns its value in Baccarat.

def baccarat_rules(value):  # Takes a number and returns its value in Baccarat.

def game(): # Simulates a game of baccarat
Returns: ["Winner", player, banker] ["Player", 8, 0] ["Tie", 2, 2]

def simulate_games(games=2):  # Simulate multiple Baccarat games
Returns: [Player, Banker, Tie]

In 100,000 simulations:
Player 42,640 Banker 47,487 Tie 9,873

PBPPBB tests the strategy of Player Banker Player Player Banker Banker
This allows you to create a "player" who plays baccarat with this strategy with their money at a specified bet value.
Functions:

MultiplePlayerSimulation(players, startingmoney, startingbet, time)
players(int): Number of players to run in the strategy.
startingmoney(int): How much money each player starts out with.
startingbet(int): The value of the first bet the player will make
time(int): Number of iterations to run the strategy for. In an iteration, a player either profits the startingbet value or they go broke.
Returns: [average(float), median(float), balances[arr]]

def PBPPBB(player): # The logic for the strategy. Bets on PBPPBB doubling up each loss.
def PlayerSimulation(startingmoney, startingbet, time):
def createPlayer(starting_money, starting_bet): # Create a custom player
