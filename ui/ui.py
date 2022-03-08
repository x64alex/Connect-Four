class UI:
    def __init__(self, service, multiplayer):
        self._service = service
        self.multiplayer = multiplayer

    def print_table(self):
        print(self._service.table)

    def player(self, p):
        self.print_table()
        m = int(input(p + " i:"))
        n = int(input(p + " j:"))
        while self._service.validate_move(m, n) is False:
            print("Bad move!")
            m = int(input(p + " i:"))
            n = int(input(p + " j:"))
        self._service.move_player(m, n, 1)

    def start(self):
        p1 = 1
        p2 = 0
        while True:

            if self._service.check_win() is True:
                self.print_table()

                if p1 == 1:
                    print("P2 has won")
                else:
                    print("P1 has won")
                return
            elif self._service.check_draw() is True:
                print("Draw")
                return
            elif p1 == 1:
                self.player("P1")
            elif p2 == 1:
                if self.multiplayer is True:
                    self.player("P2")

                else:
                    self._service.move_brain()
            p1, p2 = p2, p1
