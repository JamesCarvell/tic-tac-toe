BOARD = """
 {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
"""
POSITIONS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

score = [0.0, 0.0]

# Loop through matches
keep_playing = True
while keep_playing:
    played_positions = POSITIONS[:]

    # Starting player of next match
    if (score[0] + score[1]) % 2 == 0:
        current_player = "X"
    else:
        current_player = "O"

    # Loop through plays in match
    plays = 0
    while plays < 9:
        print(f"It's {current_player} player's turn.",
              f"Pick a numbered position to play.\n",
              BOARD.format(*played_positions))
        pick = input("pick a position: ")

        # Check if pick is a valid play
        if (pick == "X") or (pick == "O"):
            print("That's not a move you can make")
            continue
        elif pick in played_positions:
            played_positions[int(pick) - 1] = current_player
            plays += 1
        else:
            print("That's not a move you can make")
            continue

        # Check for win
        win = False
        for i in range(3):
            # Check rows
            if played_positions[i * 3] == played_positions[i * 3 + 1] == played_positions[i * 3 + 2]:
                win = True
            # Check columns
            if played_positions[i] == played_positions[i + 3] == played_positions[i + 6]:
                win = True
        # Check diagonals
        if played_positions[0] == played_positions[4] == played_positions[8]:
            win = True
        if played_positions[2] == played_positions[4] == played_positions[6]:
            win = True

        # End match on win or last play
        if win:
            print(f"Player {current_player} wins!")
            if current_player == "X":
                score[0] += 1
            else:
                score[1] += 1
            plays = 9
        elif plays >= 9:
            print("This match ends in a tie.")
            score[0] += 0.5
            score[1] += 0.5
        else:
            # Change next player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

    # Check if playing another game
    print(BOARD.format(*played_positions),
          f"\ncurrent score is X:{score[0]} O:{score[1]}")
    while True:
        keep_playing_yesno = input("Keep playing?\nyes or no: ").lower()
        if keep_playing_yesno == "yes":
            break
        elif keep_playing_yesno == "no":
            keep_playing = False
            break
        else:
            print("that wasn't yes or no")
