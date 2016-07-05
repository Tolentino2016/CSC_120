class TicTacToe:
    def __init__(self):
        self.__board = [ ['?']*3,['?']*3,['?']*3]
    def isFull(self):
        for x in range(3):
            for y in range(3):
                if self.__board[x][y] =='?':
                    return False
        return True
    
    def move(self, coordinates, mark):
        # coordinates = [ 1,2]
        # coordinates is list of two numbers in range 0-2
        self.__testCoordinates(coordinates)
        self.__board[coordinates[0]][coordinates[1]]= mark

    def __testCoordinates(self, coordinates):
        x,y =coordinates
        if (x not in range(3)) or (y not in range(3)) or self.__board != '?':
            print("This is already occupied")
            pass
            #raise ValueError, "Invalid move"

    def isWon(self):
        for row in self.__board:
            if '?' != row[0]==row[1]==row[2]:
                return row[0]
        for col in range(3):
            if '?' ==self.__board[0][col] == self.__board[1][col] == self.__board[2][col]:
                return self.__board[0][col]
        # checking the diagonals
        if '?' ==self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
                return self.__board[0][0]
        if '?' ==self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
                return self.__board[0][2]

    def displayBoard(self):
        for row in range(3):
            for col in range(3):
                print(self.__board[row][col], sep = ' ', end = '')
            print()
        
        
            
        
        
            
        
        
        
