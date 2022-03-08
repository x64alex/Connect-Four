from domain.table import Table
from repository.repo import Repository
from service.service import Service
from brain.brain import Brain
import unittest


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        unittest.TestCase.setUp(self)

    def tearDown(self) -> None:
        unittest.TestCase.tearDown(self)

    def test_table_class(self):
        table = Table(2, 2)
        assert table.value(0, 0) == 0
        table.set(0, 0, 1)
        assert table.value(0, 0) == 1
        assert table.number_columns() == 2
        assert table.number_rows() == 2
        assert str(table)[0] == '1'

    def test_repo(self):
        repo = Repository(4, 4)
        assert repo.check_win_column() is False
        assert repo.check_win_row() is False
        repo.move(3, 0, 1)
        repo.move(3, 1, 1)
        repo.move(3, 2, 1)
        repo.move(3, 3, 1)
        assert repo.validate_move(0, 0) is False
        assert repo.validate_move(3, 3) is False
        assert repo.validate_move(2, 0) is True
        assert repo.check_win_row() is True
        assert repo.check_win() is True
        repo.move(2, 0, 1)
        repo.move(1, 0, 1)
        repo.move(0, 0, 1)
        assert repo.check_win_column() is True
        repo.move(1, 1, 1)
        repo.move(2, 2, 1)
        assert repo.check_win_diagonal() is True
        # print(repo.table)

    def test_repo_second_diagonal(self):
        repo = Repository(4, 4)
        repo.move(3, 0, 1)
        repo.move(2, 1, 1)
        repo.move(1, 2, 1)
        assert repo.check_win_diagonal() is False
        repo.move(0, 3, 1)
        print(repo.table)
        assert repo.check_win_diagonal() is True
        assert repo.check_win() is True

    def test_repo_first_diagonal(self):
        repo = Repository(4, 4)
        repo.move(0, 0, 1)
        repo.move(1, 1, 1)
        repo.move(2, 2, 1)
        repo.move(3, 3, 1)
        assert repo.check_win_diagonal() is True

    def test_repo_draw(self):
        repo = Repository(1, 1)
        assert repo.check_draw() is False
        repo.move(0, 0, 1)
        assert repo.check_draw() is True

        repo2 = Repository(3, 3)
        repo2.move(0, 0, 1)
        repo2.move(0, 1, 1)
        repo2.move(0, 2, 1)
        repo2.move(1, 0, 1)
        repo2.move(1, 1, 1)
        repo2.move(1, 2, 1)
        repo2.move(2, 0, 1)
        repo2.move(2, 1, 1)
        repo2.move(2, 2, 1)

        assert repo2.check_draw() is True

    def test_possible_moves(self):
        repo = Repository(2, 2)
        assert repo.possible_moves() == [[1, 0], [1, 1]]

    def test_service(self):
        repo = Repository(4, 4)
        brain = Brain(repo)
        service = Service(repo, brain)
        assert service.validate_move(0, 0) is False
        service.move_player(0, 0, 1)
        service.move_player(1, 1, 1)
        service.move_player(2, 2, 1)
        service.move_player(3, 3, 1)
        assert service.check_win() is True

    def test_service_draw(self):
        repo = Repository(1, 1)
        brain = Brain(repo)
        service = Service(repo, brain)
        service.move_player(0, 0, 1)
        assert service.check_draw() is True

    def test_service_brain(self):
        repo = Repository(6, 7)
        brain = Brain(repo)
        service = Service(repo, brain)
        service.move_brain()
        print(service.table)
        assert repo.table.table[5][1] == 2

    def test_brain(self):
        repo = Repository(6, 7)
        brain = Brain(repo)
        service = Service(repo, brain)
        service.move_player(5, 0, 1)
        service.move_player(4, 0, 1)
        service.move_player(3, 0, 1)
        service.move_brain()
        print(service.table)
        assert service.table.table[2][0] == 2
