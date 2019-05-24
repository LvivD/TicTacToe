from board import Board


class BoardException(Exception):
    pass


class CoordOutOfTheFieldError(BoardException):
    pass


class CoordIsNotEmptyError(BoardException):
    pass


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player_move = None

    def start(self):
        move = input('Choose X or O (O start the game): ')
        if move == 'O':
            self.player_move = 1
        elif move == 'X':
            self.player_move = -1
        else:
            while move != 'O' and move != 'X':
                move = input('Wrong input!\nChoose X or O: ')
            if move == 'O':
                self.player_move = 1
            else:
                self.player_move = -1

        while not self.board.if_win():
            print(self.board)
            try:
                self.move(self.get_coord())
            except BoardException:
                coords = (100, 100)
                while 0 > coords[0] or coords[0] > 2 or 0 > coords[1] or coords[1] > 2 or \
                        self.board.board[coords[1]][coords[0]] != 0:
                    print('Wrong coordinates')
                    coords = self.get_coord()
                self.move(coords)

        print(self.board)
        res = self.board.if_win()
        if res == -2:
            print("It's a draw.")
        else:
            print(Board.TRANSFORM[res]+" win!")

        if res*

    def get_coord(self):
        if self.player_move == self.board.move:
            row, col = int(input('print row: ')), int(input('print col: '))
            return (col - 1, row - 1)
        else:
            return self.board.get_next_move()

    def move(self, coords):
        if 0 > coords[0] or coords[0] > 2 or 0 > coords[1] or coords[1] > 2:
            raise CoordOutOfTheFieldError
        elif self.board.board[coords[1]][coords[0]] != 0:
            raise CoordIsNotEmptyError
        self.board.do_move(coords)






if __name__ == "__main__":
    a = TicTacToe()
    a.start()

    # b = LinkedBinaryTree()
    # root = b._add_root(1)
    # print(type(b), type(root))
    # b._add_left(root, 2)
    # b._add_right(root, 3)
    # for i in b._subtree_inorder(root):
    #     print(i.element)
