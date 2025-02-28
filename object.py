from panda3d.core import *

class GameObject:
    def __init__(self, model_path, texture_path, scale, pos):
        self.model = loader.loadModel(model_path)
        self.model.setTexture(loader.loadTexture(texture_path))
        self.model.setScale(scale)
        self.model.setPos(pos)
        self.model.reparentTo(render)

class Tree(GameObject):
    def __init__(self, pos):
        super().__init__("Tree low.obj", "Image1.png", 0.1, pos)

class House(GameObject):
    def __init__(self, pos):
        super().__init__("House.obj", "HouseTexture.png", 0.4, pos)

