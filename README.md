# Minimax algorithm demonstration in a board game

Minimax algorithm is a backtracking like algorithm that focusses on decision making used in artificial intelligence, game theory, decision theory with the role of minimizing the possible loss for a worst case scenario.

## Installation

For this project I used [tkinter](https://docs.python.org/3/library/tkinter.html) to recreate the game TicTacToe, a board game in two players where the algorithm can be used.  
You can install tkinter using the package manager pip.

```bash
pip install tkinter
```

## Usage

By running the main.py script you will be greeted with a menu in which you can select the two main game modes:
- vs opponent where you can play with another player
- vs ai where you can battle the computer, where the minimax algorithm is used

<img src="https://user-images.githubusercontent.com/80782419/233426474-d3897fd3-fbbe-4463-a113-c4c8d643541f.png" width=20% height=20%>
<img src="https://user-images.githubusercontent.com/80782419/233426696-2fb472b9-5bbe-425d-b28b-60736ea94f4c.png" width=20% height=20%>


## Explanation of the algorithm

The minimax algorithm is widely used in two player turn-based games. The main idea is that there are two type of players, the minimizer and the maximizer. The maximizier tries to get the highest score possible at every play state while the minimizer tries the opposite.   

Every board state has a value type associated to it. The score of the board will either have a positive/negative value if the maximizer/minimizer has a upper hand. The method of how the value of each game state is calculated is purely based on the each type of game.

The best example where the algorithm is showcased is in the form of a binary tree. In the example shown the maximizer is the first one that can make the move.

If the node is at an even depth, maximizer(player) is on move, and the evaluation of its node is the maximum of the evaluations of its children.  
Same goes for the minimizer(opponent) at an odd depth, and the evaluation of its node is the minimum of the evaluations of its children.

Since this is a backtracking based algorithm, it tries all the possible decisions, then it backtracks trying to find the based decision based on the values.


For example, in the sketch shown the leaves represent the final state of a game (-10 represented for a loss and +10 for a win in the maximizer perspective), At depth 2 the player(maximizer) makes a move, trying to have the best outcome, choosing the higher number from his other two sons. This backtracks all the way to the top maximizer trying to get the highest value, and the minimizer the lowest one. Finally, at the top of the tree represents the best choice the player can make at a certain point in the game.

<img src="https://user-images.githubusercontent.com/80782419/233426969-f385d320-28d1-422b-b6f9-fdb70ccd1d22.png" width=50% height=40%>


This type of sketch also translates to TicTacToe in this manner.  
There are other game choices at this game state, but this sketch only reflects the most impactful ones.

<img src="https://user-images.githubusercontent.com/80782419/233427655-636cf964-d3c7-4a10-a2b3-22231a3d2976.png" width=50% height=40%>


## Roadamp

Further documentation about minimax algorithm and about alpha-beta pruning making the algorithm faster.  
Looking into how other, more complex games such as chess or checkers can have the minimax algorithm implemented into.
