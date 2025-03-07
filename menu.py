from direct.gui.DirectGui import DirectFrame, DirectButton, DirectLabel
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TextNode

class Menu(DirectObject):
    def __init__(self, start_game, exit_game):
        self.start_game = start_game  
        self.exit_game = exit_game

        self.accept('h', self.toggle_controls)

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


        self.hint_frame = DirectFrame(frameColor=(0.1, 0.1, 0.1, 0.8), frameSize=(-1, 1, -0.4, 0.4),
                                      pos=(0, 0, 0), relief="raised")

       
        left_text = ("WASD - Move\nE - Up\n"
                     "Q - Down\nT - Teleport\nC - Change View\n"
                     "N - Turn Left\nM - Turn Right")
        self.left_hint = DirectLabel(parent=self.hint_frame, text=left_text, scale=0.06,
                                     pos=(-0.55, 0, 0.1), text_fg=(1, 1, 1, 1),
                                     text_align=TextNode.ALeft, frameColor=(0.2, 0.2, 0.2, 0.9),
                                     frameSize=(-0.4, 0.4, -0.3, 0.3))

        
        right_text = ("B - Build\nV - Build Brick\nX - Build Stone\n"
                      "Z - Destroy\nK - Save Map\nL - Load Map")
        self.right_hint = DirectLabel(parent=self.hint_frame, text=right_text, scale=0.06,
                                      pos=(0.55, 0, 0.1), text_fg=(1, 1, 1, 1),
                                      text_align=TextNode.ALeft, frameColor=(0.2, 0.2, 0.2, 0.9),
                                      frameSize=(-0.4, 0.4, -0.3, 0.3))

    
        self.hint_frame.hide()

    def toggle_controls(self):
        if self.hint_frame.isHidden():
            self.hint_frame.show()
        else:
            self.hint_frame.hide()

    def show(self):
        self.frame.show()

    def hide(self):
        self.frame.hide()
        
    def show_controls(self):
        self.hint_frame.show()

    def hide_controls(self):
        self.hint_frame.hide()