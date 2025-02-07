
class Hero:
    def __init__(self, pos, land):
        self.mode = True
        self.land = land
        self.hero = loader.loadModel("characterlowpoly2.obj")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setP(0)
        base.camera.setR(0)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False   

    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('a',self.turn_left)
        base.accept('a'+'-repeat',self.turn_left)
        base.accept('d', self.turn_right)
        base.accept('d'+'-repeat', self.turn_right)

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)



    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()


       
    def just_move(self, angle):
        pass
    def try_move(self, angle):
        pass
    def move_to(self, angle):
        pass



    def look_at(self, angle):
        pass
    def check_dir(self, angle):
        pass



    