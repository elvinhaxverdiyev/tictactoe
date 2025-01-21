from ttt import check_winner, display

def main() -> None:
    gameboard = [" "] * 9
    player = "X"
    
    while True:
        display(gameboard)
        try:
            move = int(input(f"{player} move: (1-9) "))
            move -= 1
        except ValueError:
            print("Write correct!!!")
            continue
        if move < 0 or move > 8:
            print("Write correct posotion!!!")
            continue
            
        gameboard[move] = player
        
        result = check_winner(gameboard)
        if result is not None:
            display(gameboard)
            if result == -1:
                print("No winner")
            else:
                print(f"Winner {result}")    
            break
        player = "O" if player == "X" else "X"        
            
if __name__ == "__main__":
    main()
        
    
            
            
    