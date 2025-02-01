class Hero():
    def __init__(self,pos,land):
        self.land = land
        #self.hero = loader.loadModel()
        self.hero.setColor(1, 0.5,0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        base.mouse.InterfaceNode.setPos(x,y,z)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn
    def accept_events():
        base.accept('n', self.turn_left)
        base.accept('n'+' -repeat', self.turn_left)

    def turn_left(self):
        self.hero.setH((self.hero.getH() 5) %360)
        
    def changeView(self):
        if self.cameraOn:
            self.cameraUp
        else:
            self.cameraBind
