# 🃏 Baccarat Game Simulator in Python

A simple yet powerful Baccarat game simulator written in Python. This program draws cards from a simulated deck (shoe), reshuffling for randomness before each game. You can play Baccarat directly in your console or simulate thousands of games to analyze strategies.

---

## 🎮 How to Play

Run the following script to play Baccarat in the console:

```bash
python PlayBaccaratInConsole.py
```

---

## 📦 Installation

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🧠 Game Mechanics

This implementation uses traditional Baccarat rules with a few helper functions to calculate card values and simulate gameplay outcomes.

### `cbaccarat_rules(card)`
- 📥 Input: `card` — a card object from `deck-of-cards.py`.
- 📤 Output: The Baccarat value of the card (0–9).

### `baccarat_rules(value)`
- 📥 Input: `value` — an integer.
- 📤 Output: The Baccarat-adjusted value of a hand.

### `game()`
- 🔁 Simulates a full round of Baccarat.
- 📤 Output: Game result in the format:
  ```
  ["Winner", player_total, banker_total]
  Example: ["Player", 8, 0]
  ```

### `simulate_games(games=2)`
- 🔁 Simulates multiple Baccarat rounds.
- 📥 Input: Number of games to simulate.
- 📤 Output: Tally of outcomes in `[Player, Banker, Tie]` format.

#### Example output from 100,000 simulations:
```
Player: 42,640
Banker: 47,487
Tie:    9,873
```

---

## 📊 Strategy Testing

Use this module to test the PBPPBB strategy — a predetermined pattern of bets: Player, Banker, Player, Player, Banker, Banker.

### `PBPPBB(player)`
- Implements the PBPPBB betting logic.
- Bets double after every loss, resets after a win.

### `PlayerSimulation(startingmoney, startingbet, time)`
- Simulates a single player's experience using the strategy.
- Tracks how long a player can last based on initial conditions.

### `MultiplePlayerSimulation(players, startingmoney, startingbet, time)`
- 🔁 Simulates multiple players executing the PBPPBB strategy.
- 📥 Parameters:
  - `players (int)` — Number of player agents.
  - `startingmoney (int)` — Initial money per player.
  - `startingbet (int)` — Initial bet amount.
  - `time (int)` — Number of iterations (rounds per player).
- 📤 Output:
  ```
  [
    average_balance (float),
    median_balance (float),
    all_balances (List[int])
  ]
  ```

### `createPlayer(starting_money, starting_bet)`
- 👤 Creates a custom player object with specified starting money and bet.

---

## 📁 File Structure

```
.
├── PlayBaccaratInConsole.py     # Console game script
├── deck-of-cards.py            # Deck and card logic
├── baccarat_simulation.py      # Game logic and simulation
├── strategy.py                 # Strategy testing tools
├── requirements.txt            # Python dependencies
```

---

## 💬 Example Strategy

```
PBPPBB:
  Round 1: Bet on Player
  Round 2: Bet on Banker
  Round 3: Bet on Player
  Round 4: Bet on Player
  Round 5: Bet on Banker
  Round 6: Bet on Banker
```

---

## 📈 Results Snapshot

After simulating 100,000 games using `simulate_games()`:

- **Player Wins:** 42,640  
- **Banker Wins:** 47,487  
- **Ties:** 9,873  


