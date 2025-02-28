from direct.showbase.ShowBase import ShowBase
import pickle


class Mapmanager():
    def __init__(self, base):
        self.base = base
        self.model = 'block (1).egg'  # Модель кубика
        self.texture = 'brass.png'  # Текстура кубика
        self.land = self.base.render.attachNewNode("Land")  # Створення вузла для "землі"
        self.colors = [(0.5, 0.3, 0.0, 1),
                       (0.2, 0.2, 0.3, 1),
                       (0.5, 0.5, 0.2, 1),
                       (0.0, 0.6, 0.0, 1),]
      

    def addBlock(self, position, block_type=None):
        block = self.base.loader.loadModel(self.model)  

    
        textures = {
            "brick": "brick_.png",
            "stone": "Stone_wall_1.png",
            None: self.texture  # Базова текстура
        }
    
        texture_path = textures.get(block_type, self.texture)
        block.setTexture(self.base.loader.loadTexture(texture_path), 1)
        block.setPos(position)
        block.reparentTo(self.land)
        block.setColor(self.getColor(position[2]))
        block.setTag('at', str(position))
        return block

       # Додаємо блок до "землі"

    def startNew(self):
        # Скидання або оновлення "землі"
        self.land.removeNode()
        self.land = self.base.render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
    
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]
        


    def isEmpty(self,pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    
        
    def findBlocks(self,pos):
        return self.land.findAllMatches('=at=' +str(pos))
    
    def findHighestEmpty(self,pos):
        x, y, z =pos
        z =1
        while not self.isEmpty((x,y,z)):
            z+= 1
        return (x,y,z)
    def delBlock(self,position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def buildBlock(self, position, block_type=None):
        x, y, z = position
        new = self.findHighestEmpty(position)
        if new[2] <= z + 1:
            self.addBlock(new, block_type)


 

    def delBlockFrom(self,position):
        x,y,z = self.findHigherEmpty(position)
        pos = x,y,z-1
        for block in self.findBlocks(pos):
            block.removeNode()
  
    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat','wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)
                
    def loadMap(self):
        self.clear()
        with open('my_map.dat' ,'rb') as fin:
            lenght = pickle.load(fin)
            for i in range(lenght):
                pos = pickle.load(fin)
                self.addBlock(pos)


    