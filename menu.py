from direct.gui.DirectGui import DirectFrame, DirectButton
from direct.showbase.DirectObject import DirectObject

class Menu(DirectObject):
    def __init__(self, start_game, exit_game):
        self.start_game = start_game  
        self.exit_game = exit_game

       
        self.frame = DirectFrame(frameColor=(0, 0, 0, 0.5), frameSize=(-1.33, 1.33, -1, 1))

        
        self.start_button = DirectButton(parent=self.frame, text='Play', scale=0.09,
                                         command=self.start_game, pos=(0, 0, 0.2))

        self.exit_button = DirectButton(parent=self.frame, text='Exit', scale=0.09,
                                        command=self.exit_game, pos=(0, 0, -0.1))

    def show(self):
        self.frame.show()

    def hide(self):
        self.frame.hide()
