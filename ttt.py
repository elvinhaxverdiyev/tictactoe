class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9 
        self.current_player = "X" 

    def display(self):
        sep_horizontal = "-----+-----+-----"
        sep_vertical = "     |     |"

        first = "  |  ".join(self.board[:3])
        second = "  |  ".join(self.board[3:6])
        third = "  |  ".join(self.board[6:])

        print("\n")
        print(sep_vertical)
        print(f"  {first}  ")
        print(sep_horizontal)
        print(f"  {second}  ")
        print(sep_vertical)
        print(sep_horizontal)
        print(f"  {third}  ")
        print(sep_vertical)
        print("\n")

    def check_winner(self):
        combo = (
            # setir kombinasiyalari
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # sutun kombinasiyalari
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # diaqonal kombinasiyalar
            (0, 4, 8),
            (2, 4, 6),
        )

        for a, b, c in combo:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return -1 

        return None 

    def make_move(self, position):
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False 

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        while True:
            self.display()
            try:
                move = int(input(f"{self.current_player} move (1-9): ")) - 1
            except ValueError:
                print("Wrong number!")
                continue

            if not self.make_move(move):
                print("Wrong position! (1-9)")
                continue

            result = self.check_winner()
            if result is not None:
                self.display()
                if result == -1:
                    print("No winner!")
                else:
                    print(f"Winner: {result}!")
                break

            self.switch_player()


            
            
    