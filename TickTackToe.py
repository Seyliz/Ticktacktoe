import time

class TickTackToe:

    def __init__(self):
        self.board = [["|", "|", "|"],["|", "|", "|"],["|", "|", "|"]]
        self.round_counter = 0
        self.gamemode = 0
        self.usedsquares = ""

    def bord_reset(self):
        self.usedsquares = ""
        for i in range(3):
            for j in range(3):
                self.board[i][j] = "|"


    def print_board(self):
        print(str(self.board[0]))
        print(str(self.board[1]))
        print(str(self.board[2]))

    def check_player(self):
        return (self.round_counter % 2) + 1

    def start_game(self):
        self.print_intro()
        while True:
            if not(self.gamemode == 1 or self.gamemode == 2):
                self.gamemode = self.main_menu()
            elif self.gamemode == 1:
                self.gamemode = self.start_round()
            elif self.gamemode == 2:
                break
    
    def mark_field(self, x, y):
        if self.check_player() == 1:
            self.board[y][x] = "X"
        else:
            self.board[y][x] = "O"               

    def print_intro(self):
        print("------------------\n", "---TIC-TACK-TOE---\n", "------------------")
        time.sleep(1)
    
    def main_menu(self):
        mode = 0
        while True:
            try:
                mode = int(input("-----MAINMENU-----\n------------------\n---Enter number---\n----to select-----\n------------------\n--1--Start Game---\n--2--Exit Game----\n------------------\n"))
                return mode
            except:
                print("Try Again")

    def start_round(self):        
        self.round_counter = 0
        self.bord_reset()
        for self.round_counter in range(10):
            self.print_board()
            userescape = self.user_input()
            if userescape == 1:
                return 2
            winner = self.check_win()
            if winner > 0 and winner < 4:
                self.end_round(winner)
                return 0

    def end_round(self,player):
        if player == 1:
            print("Player 1 has won!. Congratulation")
            self.print_board()
            time.sleep(2)
        elif player == 2:
            print("Player 2 has won!. Congratulation")
            self.print_board()
            time.sleep(2)
        elif player == 3:
            print("Its a Draw")
            self.print_board()
            time.sleep(2)

    def user_input(self):
        playerinput = 0
        while True:
            while True:
                if self.check_player() == 1:
                    playerinput = input("Player 1\n")
                else:
                    playerinput = input("Player 2\n")                   
            
                if playerinput == "exit":
                    return 1
                
                try:
                    playerinput = int(playerinput)
                    break
                except:
                    print("Wrong Input\n Try Again")
                    self.print_board()

            if not(playerinput > 0 and playerinput < 10):
                print("Wrong Input\n Try Again")
                self.print_board()
            elif self.usedsquares.count(str(playerinput)) != 0:
                print("Already Used\n Try Again")
                self.print_board()
            else:                
                self.usedsquares = self.usedsquares + str(playerinput)
                break

        if playerinput == 1:
            self.mark_field(0,2)
        elif playerinput == 2:
            self.mark_field(1,2)
        elif playerinput == 3:
            self.mark_field(2,2)
        elif playerinput == 4:
            self.mark_field(0,1)
        elif playerinput == 5:
            self.mark_field(1,1)
        elif playerinput == 6:
            self.mark_field(2,1)
        elif playerinput == 7:
            self.mark_field(0,0)
        elif playerinput == 8:
            self.mark_field(1,0)
        elif playerinput == 9:
            self.mark_field(2,0)
        return 0
     
    def check_win(self):
        
        winh = 0
        wind1 = 0
        wind2 = 0
        winv = 0

        for i in range(3):
            for field in self.board[i]:
                if field == "X":
                    winh += 1
                elif field == "O":
                    winh -= 1
            if winh == 3:
                return 1
            elif winh == -3:
                return 2
            else:
                winh = 0
                
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == "X":
                    winv += 1
                elif self.board[j][i] == "O":
                    winv -= 1
            if winv == 3:
                return 1
            elif winv == -3:
                return 2
            else:
                winv = 0            

        for i in range(3):
            if self.board[i][i] == "X":
                wind1 += 1
            elif self.board[i][i] == "O":
                wind1 -= 1
        
        j=0
        for i in range(2,-1,-1):
            if self.board[i][j] == "X":
                wind2 += 1
            elif self.board[i][j] == "O":
                wind2 -= 1
            j += 1            
                
        if wind1 == 3 or wind2 == 3:
            return 1
        elif wind1 == -3 or wind2 == -3:
            return 2

        if self.round_counter == 8:
            return 3
        
        return 0


def run_game():
    game = TickTackToe()
    game.start_game()

