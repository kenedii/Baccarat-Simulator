import Baccarat as bg

def Player(self): # A player. Can play rounds of the martingale strategy
    starting_money = 100
    starting_bet = 1

def cancelIfNegative(money): # Stops gambling if player is broke
    if money <= 0:
        return 0
    else: return 1

def dontBetOverMoney(current_bet, money):  # Dont place a bet that will send player into negative
    if current_bet >= money:
        return money
    else:
        return current_bet
def PBPPBB(starting_money, starting_bet): # The logic for the strategy. Bets on PBPPBB doubling up each loss.
    if bg.game()[0] == 'Player':
        starting_money += starting_bet
    else:
        current_bet = 2 * starting_bet
        starting_money -= starting_bet
        if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
        current_bet = dontBetOverMoney(current_bet, starting_money)
        if bg.game()[0] == 'Banker':
            starting_money += current_bet
        else:
            starting_money -= current_bet
            current_bet = 2 *2* starting_bet
            current_bet = dontBetOverMoney(current_bet,starting_money)
            if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
            current_bet = dontBetOverMoney(current_bet, starting_money)
            if bg.game()[0] == 'Player':
                starting_money += current_bet
            else:
                starting_money -= current_bet
                current_bet = 2 *2*2* starting_bet
                if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
                current_bet = dontBetOverMoney(current_bet, starting_money)
                if bg.game()[0] == 'Player':
                    starting_money += current_bet
                else:
                    starting_money -= current_bet
                    current_bet = 2 *2*2*2* starting_bet
                    if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
                    current_bet = dontBetOverMoney(current_bet, starting_money)
                    if bg.game()[0] == 'Banker':
                        starting_money += current_bet
                    else:
                        starting_money -= current_bet
                        current_bet = 2 *2*2*2*2* starting_bet
                        if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
                        current_bet = dontBetOverMoney(current_bet, starting_money)
                        if bg.game()[0] == 'Banker':
                            starting_money += current_bet
                        else:
                            starting_money -= current_bet
                            if (cancelIfNegative(starting_money) == 0): return [starting_money, starting_bet]
                            current_bet = dontBetOverMoney(current_bet, starting_money)
                            PBPPBB(starting_money,(current_bet))
    return [starting_money, starting_bet]


def createPlayer(starting_money, starting_bet): # Create a custom player
    player = Player()
    player.starting_money = starting_money
    player.starting_bet = starting_bet
    return player

def PlayerSimulation(startingmoney, startingbet, time):
    player = createPlayer(startingmoney, startingbet)
    for i in range(time): # Runs one iteration of the strategy for every time increment
        PBPPBB(player.starting_money, player.starting_bet)
    return player

def MultiplePlayerSimulation(players, startingmoney, startingbet, time):
    