class Mapmanager():
    def __init__(self):
        self.model = '20821_Cube_box_cover_v1.obj'
        self.texture = 'Blank image.jpg'
        self.color = (0.2,0.2,0.35,1)
    def startNew(self):
        self.land = self.render.attachNewNode('Land')
    def addBlock(self, position):
        self.block = self.loader.loadModel(self.model)
        self.block.setTexture(self.loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)