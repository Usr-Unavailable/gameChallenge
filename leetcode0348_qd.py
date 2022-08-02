import random
from colorama import Fore, Style

# parameters init 
gridNames = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
gridDict = {idx: " " for idx in gridNames}
player1Pocket = []
player2Pocket = []
player1Mark = "X"
player2Mark = "O"
nl = "\n"
# playerColor = {"player1": "BLUE", \
#                 "player2": "GREEN"}

# board display
row0 = " " * 30 + " " + "_" * 17 + " "
for i in range(0, 3):
    globals()['row%s' % (1 + i * 3)] =  " " * 30 + \
                                        ("|" + " (") + gridNames[i * 3 + 0] + ") " + \
                                        ("|" + " (") + gridNames[i * 3 + 1] + ") " + \
                                        ("|" + " (") + gridNames[i * 3 + 2] + ") " + "|"
row3 = row6 = row9 = " " * 30 + ("|" + "_" * 5) * 3 + "|"

def printGrid():
    for i in range(0, 3):
        globals()['row%s' % (2 + i * 3)] =  " " * 30 + \
                                            ("|" + " " * 2) + gridDict[gridNames[i * 3 + 0]] + " " * 2 + \
                                            ("|" + " " * 2) + gridDict[gridNames[i * 3 + 1]] + " " * 2 + \
                                            ("|" + " " * 2) + gridDict[gridNames[i * 3 + 2]] + " " * 2 + "|"
    showGrid = []
    for j in range(0, 10):
        showGrid.append(globals()['row%s' % j])
    print(nl.join(showGrid))

# game init
player1 = input("What is the name for player 1? >> ") or "theShy"
player2 = input("What is the name for player 2? >> ") or "Rookie"
print(f"Welcome {Fore.BLUE}{player1}{Style.RESET_ALL} and {Fore.GREEN}{player2}{Style.RESET_ALL}! \
    Enter the corresponding key in the grid to place your mark. \
    'X' for {player1} and 'O' for {player2}. ")
printGrid()

# game start
def gameOn():
    availableGrid = gridNames[:] # clone list
    for i in range(0, 9):
        player = globals()['player%s' % (1 + i % 2)]
        badWords = [f"You nuts, {player}?",
                    f"You took no coffee this morning, {player}?",
                    f"You need to see a doctor, {player}!"]
        move = input(f"It is {player}'s turn. Make your move: {availableGrid} >> ").lower().strip()
        while move not in availableGrid:
            print(f"{Fore.RED}{random.choice(badWords)} Try again Bastard!{Style.RESET_ALL}")
            move = input(f"It is {player}'s turn. Make your move: {availableGrid} >> ").lower().strip()
        globals()['player%sPocket' % (1 + i % 2)].append(move)
        availableGrid.remove(move)
        gridDict[move] = globals()['player%sMark' % (1 + i % 2)]
        printGrid()
        if checkWin():
            print(f"{player} wins!")
            break

# win condition
winSet = [("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i"), \
        ("a", "d", "g"), ("b", "e", "h"), ("c", "f", "i"), \
        ("a", "e", "i"), ("c", "e", "g")]

def checkWin():
    win = False
    for t in winSet:
        if set(t).issubset(set(player1Pocket)):
            win = True
            break
    return win

gameOn()
        
    



