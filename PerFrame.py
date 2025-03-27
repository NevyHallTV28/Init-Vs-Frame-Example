from PyUI.Screen import Screen
from PyUI.PageElements import Button

class PerFrame(Screen):
    def __init__(self, window):
        super().__init__(window, (35, 55, 200))
        self.showWord = "Hello"

    def elementsToDisplay(self):
        self.elements = [
            FlipperButton(self.showWord)
        ]




class FlipperButton(Button):
    def __init__(self, word):
        super().__init__((50, 50), 10, 10, word)

    def onClick(self, screen):
        if screen.showWord == "Hello":
            screen.showWord = "World"
        else:
            screen.showWord = "Hello"