import Baccarat as bg


starting_balance = 1000 # Set starting balance here
bal = starting_balance
wagered = 0

print(f'Welcome to Baccarat! Starting balance: {bal}')
print()
while bal > 0:
    print()

    while True: # An infinite loop to make sure the user enters a valid bet amount
        bet_amnt = int(input("Enter bet amount: "))
        if bet_amnt > bal:
            print("You do not have enough money for that bet.")
            continue
        else:
            break
    wagered += bet_amnt # Increment wagered by bet amount
    bal -= bet_amnt # Decrement balance by bet amount

    bet = input("Enter bet type (Player, Banker, Tie): ").lower()

    game = bg.game() # Simulate a Baccarat game
    print()

    if game[0] == bet and bet == "player":
        bal += bet_amnt * 2
        print(f'Player: {game[1]} Banker: {game[2]} Winner: {game[0]}')
        print("You win!")
        print(f'Balance: {bal} Total Wagered: {wagered}')
    
    if game[0] == bet and bet == "banker":
        bal += bet_amnt * 1.95
        print(f'Player: {game[1]} Banker: {game[2]} Winner: {game[0]}')
        print("You win!")
        print(f'Balance: {bal} Total Wagered: {wagered}')
    
    elif game[0] == bet and bet == "tie":
        bal += bet_amnt * 9 # Adjust tie payout here (9:1 now)
        print(f'Player: {game[1]} Banker: {game[2]} Winner: {game[0]}')
        print("You win!")
        print(f'Balance: {bal} Total Wagered: {wagered}')
    
    else:
        print(f'Player: {game[1]} Banker: {game[2]} Winner: {game[0]}')
        print("You lose!")
        print(f'Balance: {bal} Total Wagered: {wagered}')

print("You are out of money. Game over.")