class TicTacToe:
    def _init_():
        self._board = [ [ '?']*3, ['?']*3,['?']*3]
    def isFull(self):
        for x in range(3):
            for y in range(3):
                if self._board[x][y] == '?' :
                    return False
        return True

    def move(self,cordinates,mark):
        # Coordinates = [1,2]
        #coordinates is list of two numbers in range 0-2
        self._testCoordinates(coordinates)
        self._board[coordinates[0]][coordinates[1]] = mark

    def __testCoordinates(self, coordinates):
        x,y = coordinates
        if (x not in range(3)) or (y not in range(3)) or \
           self._board != '?':
            print("This is already occupied")
            pass
             # raise ValueError, "Invalid Move"

    def isWon(self):
        for row in self.board:
            if '?'!=row[0]==row[1]==row[2]:
                return row[0]
         for col in range(3):
             if '?' ==self._board[0][col] == self._board[1][col] ==self._board[2][col]:
                 return self.board[0][col]
        # Checking the diagonals
            if '?' ==self._board[0][0] == self._board[1][1] ==self._board[2][2]:
                 return self.board[0][0]
            if '?' ==self._board[0][2] == self._board[1][1] ==self._board[2][0]:
                 return self.board[0][2].

        def displayBoard(self):
            for in range(3):
            for col in range(3):
                print (self._board[row][col]
            print()
            
            
            
            
                                   
