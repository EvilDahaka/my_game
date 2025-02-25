from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from menu import Menu
import sys 

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        self.land.addBlock((0, 0, 0))
        self.land.loadLand("land.txt")
        self.hero = Hero((10, 8, 2), self.land, self)

        self.game_started = False
        self.paused = False


        self.menu = Menu(self.start_game, self.exit_game)
        

    def switch_menu(self):
        if self.menu.frame.isHidden():
            self.menu.show()
            self.paused = True  
        else:
            self.menu.hide()
            self.paused = False  



    def start_game(self):
        self.menu.hide()
        self.game_started = True  
        self.accept("escape", self.switch_menu)

    def exit_game(self):
        sys.exit()

    

game = Game()
game.run()  # Запускає гру