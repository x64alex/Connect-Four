import copy


class Brain:
    def __init__(self, repo):
        self._repo = repo

    def block_win(self):
        """
        If the first player is one move from winning the brain will block the move
        """
        for move in self._repo.possible_moves():
            repo = copy.deepcopy(self._repo)
            repo.move(move[0], move[1], 1)
            if repo.check_win() is True:
                self._repo.move(move[0], move[1], 2)
                return True

    def best_move(self):
        """
        Find the move with the shortest way to win with the maximum depth 4
        """
        repo = copy.deepcopy(self._repo)
        depth = []
        for move1 in repo.possible_moves():
            moves = 0
            repo.move(move1[0], move1[1], 2)
            if repo.check_win() is True:
                moves += 1
                move = [move1, moves]
                depth.append(move)
            for move2 in repo.possible_moves():
                repo.move(move2[0], move2[1], 2)
                if repo.check_win() is True:
                    moves += 2
                    move = [move1, moves]
                    depth.append(move)
                for move3 in repo.possible_moves():
                    repo.move(move3[0], move3[1], 2)
                    if repo.check_win() is True:
                        moves += 3
                        move = [move1, moves]
                        depth.append(move)
                    for move4 in repo.possible_moves():
                        repo.move(move4[0], move4[1], 2)
                        if repo.check_win() is True:
                            moves += 4
                            move = [move1, moves]
                            depth.append(move)



        def get_moves(el):
            return el[1]
        depth.sort(key=get_moves)
        #print(depth)
        move = depth[0][0]
        self._repo.move(move[0], move[1], 2)

    def next_move(self):
        if self.block_win() is True:
            return
        self.best_move()
