class Player:
    def __init__(self,name,sign):
        self.name= name
        self.sign= sign
    def get_sign(self):
        return (self.sign)
    def get_name(self):
        return (self.name)    
    def choose(self,board):
        done=False
        while not done:
            cell_list=["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
            choice=input(f"\n{self.name},{self.sign}: Enter a cell [A-C][1-3]:").upper()
            if choice in cell_list and board.isempty(cell_list.index(choice)):
                board.set(cell_list.index(choice),self.sign)
                done=True
            else:
                print("You did not choose correctly.")
                done=False

class AI(Player):
    def __init__(self,name,sign):
        Player.__init__(self,name,sign)
    #def choose(self,board): 

class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.winner = ""
    def get_size(self):
        return (self.size)
    def get_winner(self):
        return (self.winner)
    def set(self, index, sign):
        self.board[index]=sign
    def isempty(self, index):
        if self.board[index]==self.sign:
            return True
        else:
            return False
        
    
    def isdone(self):
        done = False
        winning_conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in winning_conditions:
            if self.board[i[0]]!= self.sign:
                if self.board[i[0]]==self.board[i[1]] and self.board[i[0]]==self.board[i[2]]:    
                    done=True
                    self.winner=self.board[i[0]]    
                    break
        if self.sign not in self.board:
            done=True
        return done
                
    def show(self):
        print("\n     A       B       C    ")
        print(" + - - - + - - - + - - - +")
        print("1|   "+self.board[0]+"   |   "+self.board[1]+"   |   "+self.board[2]+"   |")
        print(" + - - - + - - - + - - - +")
        print("2|   "+self.board[3]+"   |   "+self.board[4]+"   |   "+self.board[5]+"   |")
        print(" + - - - + - - - + - - - +")
        print("3|   "+self.board[6]+"   |   "+self.board[7]+"   |   "+self.board[8]+"   |")
        print(" + - - - + - - - + - - - +")
        
        
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = Player("Bob", "X")
    player2 = Player("Alice", "O")
    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N] ").upper()
    if (ans != "Y"):
        break
print("Goodbye!")
