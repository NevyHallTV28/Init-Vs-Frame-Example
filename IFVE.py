#Init Frame vs from 
from PyUI.Screen import Screen
from PyUI.PageElements import *

class Ifve(Screen):
    def __init__(self, window):
        super().__init__(window, (10, 0, 145))
        self.elements = [
        ]
        #loop to setup board
        index = -1
        for x in range(8):
            index += 1
            coordX = 11*x + 15                     
            self.elements.append(ImageClass((coordX, 50), 10, 10, "./imgs/picture.png", index))

class ImageClass(Image):
    def __init__(self, centerXY, width, height, imagePath, index):
        super().__init__(centerXY, width, height, imagePath)
        self.index = index
    def onClick(self, screen):
        screen.elements.remove(self)
