"""
Assignment: W02 Prove: Developer - Solo Code Submission
File: Tic-Tac-Toe game
Author: Andrea Garzon
Version: 0.0.1
Date: Jan 12th, 2022

Purpose: Make a program to play the Tic-Tac-Toe game.

"""

#Define the main function
def main():

    #Start the game
    status = "going"

    #Create a list called marks to contain the squares for the game's interface.
    marks = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    player = "Player 1"
    
    #call the print_squares function
    print_squares(marks)
    print()

    #Ask user for a move
    while status =="going":

        #Verify if the user input is valid
        if player == "Player 1":
            mark = int(input("Player 1: select a square (1-9) to mark: "))
            if marks[mark-1] != "X" and marks[mark-1] != "O":
                marks[mark-1] = "X"
                player = "Player 2"
            else:
                print()
                print("Invalid mark, try again")
        
        elif player == "Player 2":
            mark = int(input("Player 2: select a square (1-9) to mark: "))
            if marks[mark-1] != "X" and marks[mark-1] != "O":
                marks[mark-1] = "O"
                player = "Player 1"
            else:
                print()
                print("Invalid mark, try again")
        
        print()
        print_squares(marks)
        print()
        status = draw_check(marks, status)
        status = winner_check(marks, status)

    print()
    print("Good game. Thanks for playing!")

#Define the print_squares function
def print_squares(marks):
    """
    creates and print an interface for the game
    Return: an interface.
    """
    print(f"{marks[0]} | {marks[1]} | {marks[2]}")
    print("--+---+---")
    print(f"{marks[3]} | {marks[4]} | {marks[5]}")
    print("--+---+---")
    print(f"{marks[6]} | {marks[7]} | {marks[8]}")

#Define the draw_check function
def draw_check(marks, status):
    """
    Check is there is a draw and finish the game.

    parameters:
        marks: An element from the marks list.
        status: The status of the game.
    Return: status.
    """
    for mark in marks:
        if mark != "X" and mark != "O":
            status = "going"
            break
        else:
            status = "end"
            continue

    return(status)


#Define the winner_check function
def winner_check(marks, status):
    """
    Check is there is a winner or if game is over.

    parameters:
        marks: An element from the marks list.
        status: The status of the game, eigther "going" or "end".
    Return: status.
    """
    winner = "none"

    #Check horizontally
    if marks[0] == "X" and marks[1] == "X" and marks[2] == "X":
        winner = "Player 1"
    elif marks[0] == "O" and marks[1] == "O" and marks[2] == "O":
        winner = "Player 2"
    
    elif marks[3] == "X" and marks[4] == "X" and marks[5] == "X":
        winner = "Player 1"
    elif marks[3] == "O" and marks[4] == "O" and marks[5] == "O":
        winner = "Player 2"

    elif marks[6] == "X" and marks[7] == "X" and marks[8] == "X":
        winner = "Player 1"
    elif marks[6] == "O" and marks[7] == "O" and marks[8] == "O":
        winner = "Player 2"
    
    #Check vertically
    elif marks[0] == "X" and marks[3] == "X" and marks[6] == "X":
        winner = "Player 1"
    elif marks[0] == "O" and marks[3] == "O" and marks[6] == "O":
        winner = "Player 2"
    
    elif marks[1] == "X" and marks[4] == "X" and marks[7] == "X":
        winner = "Player 1"
    elif marks[1] == "O" and marks[4] == "O" and marks[7] == "O":
        winner = "Player 2"

    elif marks[2] == "X" and marks[5] == "X" and marks[8] == "X":
        winner = "Player 1"
    elif marks[2] == "O" and marks[5] == "O" and marks[8] == "O":
        winner = "Player 2"
    
    #Check diagonally
    elif marks[0] == "X" and marks[4] == "X" and marks[8] == "X":
        winner = "Player 1"
    elif marks[0] == "O" and marks[4] == "O" and marks[8] == "O":
        winner = "Player 2"
    
    elif marks[2] == "X" and marks[4] == "X" and marks[6] == "X":
        winner = "Player 1"
    elif marks[2] == "O" and marks[4] == "O" and marks[6] == "O":
        winner = "Player 2"
    
    #print a frienly message
    if winner == "Player 1":
        print("Player 1 wins")
        status = "end"
    elif winner == "Player 2":
        print("Player 2 wins")
        status = "end"
    
    return (status)

if __name__ == "__main__":
    main()
