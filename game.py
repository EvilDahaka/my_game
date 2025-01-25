from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model=self.loader.loadModel('13793_MaleHeroStanding_v1.obj')
        self.model.reparentTo(self.render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)
        self.camLens.setFov(90)

    

game = Game()
game.run()  # Запускає гру
