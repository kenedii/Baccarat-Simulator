import Baccarat as bg

def Player(self):
    starting_money = 100
    starting_bet = 1
    time = 1000 # Number of times to run the martingale strategy. Players will stop if broke
    number_of_players = 1

def PBPPBB(starting_money, starting_bet):
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

def cancelIfNegative(money):
    if money <= 0:
        return 0
    else: return 1

def dontBetOverMoney(current_bet, money):
    if current_bet >= money:
        return money
    else:
        return current_bet

def PlayerSimulation():
