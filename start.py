from repository.repo import Repository
from brain.brain import Brain
from service.service import Service
from ui.ui import UI
from ui.gui import GUI

repo = Repository(6, 7)
brain = Brain(repo)
service = Service(repo, brain)
ui = GUI(service, False)
ui.start()
