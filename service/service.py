class Service:
    def __init__(self, repo, brain):
        self.repo = repo
        self.brain = brain
        self.table = repo.table

    def validate_move(self, m, n):
        return self.repo.validate_move(m, n)

    def check_win(self):
        return self.repo.check_win()

    def check_draw(self):
        return self.repo.check_draw()

    def move_player(self, m, n, val):
        self.repo.move(m, n, val)

    def move_brain(self):
        self.brain.next_move()
