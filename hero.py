from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

class Hero:
    def __init__(self, pos, land, game):
        self.mode = True
        self.land = land
        self.game = game 
        self.hero = loader.loadModel("characterlowpoly2.obj")
        #self.texture = 'rp_nathan_animated_003_walking_A.jpg'
        self.hero.setColor(1, 0.5, 0)
        #self.hero.setTexture(loader.loadTexture(self.texture))
        self.hero.setScale(0.1)
        self.hero.setPos(pos)
        #self.hero.setHpr(0, 90, 0)  # Або спробуй (0, 270, 0)
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
        base.accept('n',self.turn_left)
        base.accept('n'+'-repeat',self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m'+'-repeat', self.turn_right)

        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)

        base.accept('d', self.right)
        base.accept('d'+'-repeat',self.right)
        base.accept('a', self.left)
        base.accept('a'+'-repeat',self.left)

        base.accept('e',self.up)
        base.accept('e'+'repeat',self.up)
        base.accept('q',self.changeMode)

        base.accept('b',self.build)
        base.accept('z',self.destroy)

        base.accept('g', self.down)
        base.accept('g' + '-repeat', self.down)

        base.accept('k', self.land.saveMap)
        base.accept('l',self.land.loadMap)

        base.accept('space', self.jump)
        base.accept('t', self.teleport)



    def turn_left(self):
        if not self.game.game_started or self.game.paused:
            return
        self.hero.setH((self.hero.getH() + 5) % 360)
    
    def turn_right(self):
        if not self.game.game_started or self.game.paused:
            return
        self.hero.setH((self.hero.getH() - 5) % 360)
    
    def back(self):
        if not self.game.game_started or self.game.paused:
            return
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def forward(self):
        if not self.game.game_started or self.game.paused:
            return
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    
    def right(self):
        if not self.game.game_started or self.game.paused:
            return
        angle =(self.hero.getH()+270) % 360
        self.move_to(angle)
    
    def left(self):
        if not self.game.game_started or self.game.paused:
            return
        angle =(self.hero.getH()+90) % 360
        self.move_to(angle)
    
    def up(self):
        if not self.game.game_started or self.game.paused:
            return
        self.hero.setZ(self.hero.getZ() + 1)
    
    def changeMode(self):
        if self.mode == True:
            self.mode == False
        else:
            self.mode == True
    
    def down(self):
        if not self.game.game_started or self.game.paused:
            return
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)




    def changeView(self):
        if not self.game.game_started or self.game.paused:
            return
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

       
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHigherEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0],pos[1],pos[2] +1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)



    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z
    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return 0,-1
        elif angle <= 65:
            return 1,-1
        elif angle <=110:
            return 1,0
        elif angle <= 155:
            return 1,1
        elif angle <= 200:
            return 0,1
        elif angle <= 245:
            return -1,1
        elif angle <= 290:
            return -1,0
        elif angle <=335:
            return -1,-1
        else:
            return 0,-1
        
    def build(self):
        if not self.game.game_started or self.game.paused:
            return
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)
    
    def destroy(self):
        if not self.game.game_started or self.game.paused:
            return
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def jump(self):
        if not self.game.game_started or self.game.paused:
            return
        self.hero.setZ(self.hero.getZ() + 2)  # Піднімає героя
        taskMgr.doMethodLater(0.3, lambda task: self.land(task), 'fall')   # Викликає посадку через 0.3 сек.

    def land(self, task):  # land ОБОВ'ЯЗКОВО має приймати параметр task
        self.hero.setZ(self.hero.getZ() - 2)  # Опускає героя назад
        return task.done  # Завершення задачі
    
    def teleport(self):
        if not self.game.game_started or self.game.paused:
            return
        self.hero.setPos(10, 8, 2)  # Телепорт на стартову точку
   






    
