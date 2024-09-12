import random
class TicTacToe:
    def __init__(self, board=None):
        self.board = board
        
        if self.board == None:
            self.board = [[None, None, None], [None, None, None], [None, None, None]]
        else:
            #Checks that the given board is in the proper format#
            for i in self.board:
                if isinstance(i, list) == False:
                    raise ValueError
                if len(i) !=3:
                    raise ValueError

    def check_winner(self):
        for i in range(3):
            #Rows#
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            #Columns#
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        
        #Verticals#
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        else:
            return None

    def randomly_fill_board(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        symbols = ['X', 'O']
        #Randomly chooses which symbol will have 5 turns#
        random.shuffle(symbols)

        first = []
        for i in range(4):
            first.append(symbols[0])
        print(first)

        second = []
        for i in range(5):
            second.append(symbols[1])
        print(second)

        choice = 0
        for i in range(3):
            for j in range(3):
                choice = random.randint(0,1)
                if choice == 0:
                    if len(first) == 0:
                        self.board[i][j] = second.pop()
                    else:
                        self.board[i][j] = first.pop()
                if choice == 1:
                    if len(second) == 0:
                        self.board[i][j] = first.pop()
                    else:
                        self.board[i][j] = second.pop()
        print(self.board)
