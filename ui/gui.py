import pygame
import math
import sys


class GUI:
    def __init__(self, service, multiplayer):
        self._service = service
        self.__multiplayer = multiplayer
        self.board = self._service.repo.table
        self.__columns = self._service.repo.number_columns
        self.__rows = self._service.repo.number_rows

        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.square_size = 100
        self.radius = int(self.square_size / 2 - 5)
        self.width = self.__rows * self.square_size
        self.height = (self.__columns + 1) * self.square_size
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

        self.game_over = False

    def print_table(self):
        print(self.board)

    def outcome_label(self, my_font, n):
        if self._service.check_win() is True:
            label = my_font.render(n + " wins!!", True, self.yellow)
            self.screen.blit(label, (40, 10))
            self.game_over = True
        if self._service.check_draw() is True:
            label = my_font.render("Draw!!", True, self.red)
            self.screen.blit(label, (40, 10))
            self.game_over = True

    def players(self, event, moves, my_font):
        posix = event.pos[0]
        col = int(math.floor(posix / self.square_size))
        m, n = 0, 0
        for move in moves:
            if move[1] == col:
                m = move[0]
                n = move[1]

        if self._service.validate_move(m, n):
            self._service.move_player(m, n, 2)

            if self._service.check_win() is True:
                label = my_font.render("Player 2 wins!!", True, self.yellow)
                self.screen.blit(label, (40, 10))
                self.game_over = True
            if self._service.check_draw() is True:
                label = my_font.render("Draw!!", True, self.red)
                self.screen.blit(label, (40, 10))
                self.game_over = True

    def draw_board(self):
        for c in range(self.__rows):
            for r in range(self.__columns):
                pygame.draw.rect(self.screen, self.blue, (
                    c * self.square_size, r * self.square_size + self.square_size, self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.black, (
                    int(c * self.square_size + self.square_size / 2),
                    int(r * self.square_size + self.square_size + self.square_size / 2)), self.radius)

        for c in range(self.__rows):
            for r in range(self.__columns):
                if self.board.value(r, c) == 1:
                    pygame.draw.circle(self.screen, self.red, (
                        int(c * self.square_size + self.square_size / 2),
                        self.height - int((self.__columns - r - 1) * self.square_size + self.square_size / 2)),
                                       self.radius)
                elif self.board.value(r, c) == 2:
                    pygame.draw.circle(self.screen, self.yellow, (
                        int(c * self.square_size + self.square_size / 2),
                        self.height - int((self.__columns - r - 1) * self.square_size + self.square_size / 2)),
                                       self.radius)
        pygame.display.update()

    def start(self):
        pygame.init()

        my_font = pygame.font.SysFont("monospace", 75)
        turn = 0
        self.draw_board()
        pygame.display.update()
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.square_size))
                    posix = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(self.screen, self.red, (posix, int(self.square_size / 2)), self.radius)
                    else:
                        pygame.draw.circle(self.screen, self.yellow, (posix, int(self.square_size / 2)), self.radius)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.black, (0, 0, self.width, self.square_size))
                    moves = self._service.repo.possible_moves()

                    # Ask for Player 1 Input
                    if turn == 0:
                        posix = event.pos[0]
                        col = int(math.floor(posix / self.square_size))
                        m, n = 0, 0
                        for move in moves:
                            if move[1] == col:
                                m = move[0]
                                n = move[1]
                        if self._service.validate_move(m, n):
                            self._service.move_player(m, n, 1)

                            if self._service.check_win() is True:
                                label = my_font.render("Player 1 wins!!", True, self.red)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True
                                self.__multiplayer = True
                                turn += 1

                            if self._service.check_draw() is True:
                                label = my_font.render("Draw!!", True, self.red)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True
                            if self.__multiplayer is False:
                                self._service.move_brain()
                                self.outcome_label(my_font, "Computer")
                                turn += 1

                    # Ask for Player 2 Input
                    else:
                        self.players(event, moves, my_font)

                    # self.print_table()
                    self.draw_board()

                    turn += 1
                    turn = turn % 2

                    if self.game_over:
                        pygame.time.wait(3000)
