from direct.gui.DirectGui import DirectFrame, DirectButton
from direct.showbase.DirectObject import DirectObject

class Menu(DirectObject):
    def __init__(self, start_game, exit_game):
        self.start_game = start_game  
        self.exit_game = exit_game

        button_default = 'UIButton.png'
        button_guidance = 'UIButtonHighlighted.png'
        frame_border = 'stoneFrame.png'
        
        self.frame = DirectFrame(frameColor=(0, 0, 0, 0.5), frameSize=(-1.33, 1.33, -1, 1), image=frame_border,  image_scale=(1.33, 1, 1))

        self.start_button = DirectButton(parent=self.frame, text='Play', scale=(0.6, 1, 0.15),
                                         command=self.start_game, pos=(0, 0, 0.25),
                                         image=(button_default, button_guidance, button_guidance, button_default),
                                         relief=None, text_scale=(0.5, 0.6), text_pos=(0, -0.02)
                                         )

        self.exit_button = DirectButton(parent=self.frame, text='Exit', scale=(0.6, 1, 0.15),
                                        command=self.exit_game, pos=(0, 0, -0.15),
                                        image=(button_default, button_guidance, button_guidance, button_default),
                                        relief=None, text_scale=(0.5, 0.6), text_pos=(0, -0.02)
                                        )

    def show(self):
        self.frame.show()

    def hide(self):
        self.frame.hide()
