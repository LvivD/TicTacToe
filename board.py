import random
from btree import BinaryTree


class Board:
    TRANSFORM = {0: " ", 1: "O", -1: "X"}

    def __init__(self):
        self.board = [[0]*3 for i in range(3)]
        self.move = 1
        self._tree = None

    def __str__(self):
        s = ''
        for i in range(3):
            s += Board.TRANSFORM[self.board[i][0]] + ' | ' + Board.TRANSFORM[self.board[i][1]] + ' | ' + \
                 Board.TRANSFORM[self.board[i][2]] + '\n'
            if i != 2:
                s += '- + - + -\n'
        return s

    def if_win(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
            elif self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[2][2]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return -2

    def str_board_gen(self):
        s = ''
        for i in range(3):
            for j in range(3):
                s += Board.TRANSFORM[self.board[i][j]]
        # print(s)
        return s

    def tree_generation(self):

        def if_win_str(s):
            for i in range(3):
                if s[3 * i + 1] == s[3 * i] == s[3 * i + 2] != ' ':
                    return s[3 * i]
                elif s[i] == s[i + 3] == s[i + 6] != ' ':
                    return s[i]
            if s[0] == s[4] == s[8] != ' ':
                return s[0]
            elif s[2] == s[4] == s[6] != ' ':
                return s[2]
            for i in s:
                if i == ' ':
                    return 0
            return -2

        def random_move(board, without=None):
            choices = []
            for i in range(9):
                if board[i] == ' ' and i != without:
                    choices.append(i)
            if choices:
                return random.choice(choices)
            else:
                return None

        def gen_nex_move(node, move):
            res = if_win_str(node.data)
            if res:
                if res == -2:
                    res = 0
                elif res == 'X':
                    res = -1
                elif res == 'O':
                    res = 1
                tree.add_right(node, res * self.move)
                tree.add_left(node, 0)
                return

            left_move = random_move(node.data)
            right_move = random_move(node.data, without=left_move)

            if right_move is not None:
                right_board = node.data[:right_move] + Board.TRANSFORM[move] + node.data[right_move+1:]
                tree.add_right(node, right_board)
                gen_nex_move(node.right, -1 * move)
            else:
                tree.add_right(node, 0)

            left_board = node.data[:left_move] + Board.TRANSFORM[move] + node.data[left_move + 1:]
            tree.add_left(node, left_board)
            gen_nex_move(node.left, -1 * move)

        tree = BinaryTree()
        tree.add_root(self.str_board_gen())
        gen_nex_move(tree.get_root(), self.move)
        self._tree = tree

    def get_next_move(self):
        self.tree_generation()
        # print('\n', self._tree, '\n')

        def count(node):
            res = 0
            for elem in self._tree.inorder(node):
                if type(elem) == int:
                    res += elem
            return res

        def get_position(best_board):
            real_board = self.str_board_gen()
            for i in range(9):
                try:
                    if best_board[i] != real_board[i]:
                        res = i
                        break
                except TypeError:
                    print(i, best_board, real_board)
            # print(res % 3, res // 3)
            return (res % 3, res // 3)

        right_points = count(self._tree.root.right)
        left_points = count(self._tree.root.left)
        if right_points > left_points:
            return get_position(self._tree.root.right.data)
        else:
            return get_position(self._tree.root.left.data)

    def do_move(self, pos):
        # print(pos)
        if self.board[pos[1]][pos[0]] != 0:
            print('alert')
            input()
        self.board[pos[1]][pos[0]] = self.move
        self.move *= -1
        self._tree = None




if __name__ == "__main__":
    board = Board()
    print(board.if_win())
    print(board)
    board.board = [[0, 1, 1], [-1, 0, -1], [0, 0, -1]]
    print(board.str_board_gen())
    print(board)
    for it in range(3):
        next_move = board.get_next_move()
        print(next_move, 'res')
        # print(board._tree)
        board.do_move(next_move)
        print(board)
        print(board.str_board_gen())


    # print(board.move)


