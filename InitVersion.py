from PyUI.Screen import Screen
from PyUI.PageElements import Button

class InitVersion(Screen):
    def __init__(self, window):
        super().__init__(window, (35, 55, 200))
        self.elements = [
            FlipperButton()
        ]




class FlipperButton(Button):
    def __init__(self):
        super().__init__((50, 50), 10, 10, "Hello")

    def onClick(self, screen):
        if self.text == "Hello":
            self.text = "World"
        else:
            self.text = "Hello"