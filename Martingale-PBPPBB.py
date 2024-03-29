import Baccarat as bg
import statistics
import numpy

# Simulation of the Baccarat strategy seen in this video: https://www.youtube.com/watch?v=g1JpoE2UyF8

class Player():  # A player. Can play rounds of the martingale strategy
    class Player():
        def __init__(self, starting_money=100, starting_bet=1):
            self.starting_bet = starting_bet
            self.starting_money = starting_money


def cancelIfNegative(money):  # Stops gambling if player is broke
    if money <= 0:
        return 0
    else:
        return 1


def subtractifLose(player, current_bet, win_on, game):  # The logic to subtract money if the player lost
    if game[0] == 'Tie' and win_on == 'Tie':
        # Tie pays 9 to 1
        player.starting_money = player.starting_money + 9 * current_bet
        return [player, 1]
    elif game[0] == win_on and game[0] == 'Player':  # Player winning
        player.starting_money = player.starting_money + (2 * current_bet)
        return [player, 1]
    elif game[0] == win_on and game[0] == 'Banker':  # Banker winning
        player.starting_money = player.starting_money + (1.95 * current_bet)
        return [player, 1]
    elif (game[0] != 'Tie') and (game[0] != win_on):  # Player losing
        return [player, 0]
    else:  # Player and banker tie and tie was not bet on
        player.starting_money = player.starting_money + current_bet
        return [player, 2]


def dontBetOverMoney(current_bet, money):  # Dont place a bet that will send player into negative
    if current_bet >= money:
        return money
    else:
        return current_bet


def PBPPBB(player):  # The logic for the strategy. Bets on PBPPBB doubling up each loss.
    current_bet = dontBetOverMoney(player.starting_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet

    if cancelIfNegative(player.starting_money) == 0:
        return [player.starting_money, player.starting_bet]

    while True:
        game_result = subtractifLose(player, current_bet, 'Player', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            current_bet = dontBetOverMoney(current_bet, player.starting_money)
            break

    current_bet = dontBetOverMoney(current_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet
    while True:
        game_result = subtractifLose(player, current_bet, 'Banker', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            current_bet = dontBetOverMoney(current_bet, player.starting_money)
            break

    current_bet = dontBetOverMoney(current_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet
    while True:
        game_result = subtractifLose(player, current_bet, 'Player', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            current_bet = dontBetOverMoney(current_bet, player.starting_money)
            break

    current_bet = dontBetOverMoney(current_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet
    while True:
        game_result = subtractifLose(player, current_bet, 'Player', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            current_bet = dontBetOverMoney(current_bet, player.starting_money)
            break

    current_bet = dontBetOverMoney(current_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet
    while True:
        game_result = subtractifLose(player, current_bet, 'Banker', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            current_bet = dontBetOverMoney(current_bet, player.starting_money)
            break

    current_bet = dontBetOverMoney(current_bet, player.starting_money)
    if current_bet > player.starting_money:
        current_bet = player.starting_money  # Adjust the bet to match available money
    player.starting_money -= current_bet
    while True:
        game_result = subtractifLose(player, current_bet, 'Banker', bg.game())  # Fetch the entire result
        player = game_result[0]
        if game_result[1] == 1:
            return [player.starting_money, player.starting_bet]
        elif game_result[1] == 2:  # If it's a tie and the player didn't bet on it
            continue
        else:
            current_bet *= 2
            if cancelIfNegative(player.starting_money) == 0:
                return [player.starting_money, player.starting_bet]
            player.starting_bet == current_bet
            break

    # Restart the sequence recursively
    return PBPPBB(player)


def createPlayer(starting_money, starting_bet):  # Create a custom player
    player = Player()
    player.starting_money = starting_money
    player.starting_bet = starting_bet
    return player


def PlayerSimulation(startingmoney, startingbet, time):
    player = createPlayer(startingmoney, startingbet)
    for i in range(time):  # Runs one iteration of the strategy for every time increment
        PBPPBB(player)
    return player.starting_money


def MultiplePlayerSimulation(players, startingmoney, startingbet, time):
    balances = []
    for u in range(players):
        balances.append(PlayerSimulation(startingmoney, startingbet, time))
    average = sum(balances) / len(balances)  # Mean balance out of every player
    median = statistics.median(balances)
    stdev = statistics.stdev(balances)
    variance = statistics.variance(balances)

    ratio_zeros = (players-numpy.count_nonzero(balances)) / players # Number of players who went bust

    if players >= 2:
        return [average, median, stdev, variance, balances, ratio_zeros]
    else: # Cannot calculate the standard deviation with 1 player.
        return [average, median, variance, balances, ratio_zeros]


def __main__():
    players = 10000
    startingmoney = 1000
    startingbet = 20
    time = 30
    results = MultiplePlayerSimulation(players, startingmoney, startingbet, time)
    print(results[4])  # Print the balance of every player at the end of the simulation
    print('Average Player Money:', results[0], 'Median player money', results[1])
    print('Standard deviation:', results[2], '  Variance:', results[3])
    print(f'Number of players who went broke: {results[5]}')


__main__()
