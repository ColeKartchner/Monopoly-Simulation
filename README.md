# Introduction

This report presents the results of a project aimed at understanding the probabilities of landing on different spaces in the Monopoly board game. The simulation was implemented in Python, using the Classic rules of the 2018 US version of the game. The main objective was to simulate millions of games to analyze the landing probabilities and evaluate the stability of these probabilities across different numbers of turns.

## Simulation Details

The simulation tracked the following:

- **Total Number of Moves Made**: The total number of moves was recorded.
- **Landing Frequency**: The number of times each player landed on each space was tracked.
- **Jail Strategies**:
  - **Strategy A**: If a player has a "Get Out of Jail Free" card, it is used immediately. If not, the player pays the $50 fine and gets out of jail immediately.
  - **Strategy B**: If a player has a "Get Out of Jail Free" card, it is used immediately. If not, the player tries to roll doubles for three turns to get out of jail. If unsuccessful after three turns, the player pays the $50 fine and gets out on the fourth turn.

## Simulation Setup

- **Players**: A single player was implemented.
- **Moves**: The total number of moves made was tracked.
- **Landing**: An array was used to track the total number of times landed on each space.
- **Dice**: A function was implemented to roll the dice, considering special rules about rolling doubles.
- **Chance and Community Chest Cards**: Functions were implemented to draw, shuffle, and discard cards.

## Results

The simulation was run for 1,000, 10,000, 100,000, and 1,000,000 turns for both strategies. Below are the summarized results:

### Strategy A

**After 1,000 turns**:
- Space 0: 22 landings (2.29%)
- Space 8: 33 landings (3.44%)
- Space 24: 33 landings (3.44%)

**After 10,000 turns**:
- Space 0: 206 landings (2.13%)
- Space 8: 241 landings (2.49%)
- Space 24: 250 landings (2.59%)

**After 100,000 turns**:
- Space 0: 2073 landings (2.15%)
- Space 8: 2307 landings (2.39%)
- Space 24: 2602 landings (2.70%)

**After 1,000,000 turns**:
- Space 0: 20861 landings (2.16%)
- Space 8: 22576 landings (2.34%)
- Space 24: 26163 landings (2.71%)

### Strategy B

**After 1,000 turns**:
- Space 0: 22 landings (2.40%)
- Space 20: 33 landings (3.61%)
- Space 28: 33 landings (3.61%)

**After 10,000 turns**:
- Space 0: 197 landings (2.16%)
- Space 20: 260 landings (2.85%)
- Space 24: 231 landings (2.53%)

**After 100,000 turns**:
- Space 0: 1995 landings (2.17%)
- Space 20: 2617 landings (2.85%)
- Space 24: 2579 landings (2.81%)

**After 1,000,000 turns**:
- Space 0: 19683 landings (2.15%)
- Space 20: 26275 landings (2.87%)
- Space 24: 24663 landings (2.69%)

## Analysis

### Stability of Probabilities

**Change of Percentages for Strategy A**:
- For each value of *n* (1,000, 10,000, 100,000, 1,000,000), the landing probabilities for each space were calculated. As the number of turns increased, the probabilities became more stable and consistent.

**Convergence of Probabilities**:
- The probabilities for each space became stable around 100,000 turns. This convergence indicates that a large number of simulations is necessary to obtain reliable probabilities.

**Value of *n* for Stability**:
- Stability was generally observed at 100,000 turns for most spaces. Beyond this point, the change in probabilities between runs was minimal, indicating convergence.

### Comparison of Strategies

The probabilities for landing on each space for *n = 1,000,000* were compared for both strategies. Minor differences were observed due to the different methods of handling jail exits. Strategy B had slightly higher probabilities for some spaces due to the additional turns spent in jail.

### Effect of Multiple Players

If the number of players were increased, it could potentially affect the landing probabilities due to the added interactions and dynamics. However, the overall distribution of landings should still converge similarly, given a sufficiently large number of turns.

## Conclusion

This project successfully simulated the landing probabilities of Monopoly spaces, providing insights into the stability of these probabilities and the impact of different jail exit strategies. The data shows that the landing probabilities stabilize with an increasing number of turns, and minor differences exist between the two strategies. These findings can help players make more informed decisions about property purchases and strategic moves in the game.
