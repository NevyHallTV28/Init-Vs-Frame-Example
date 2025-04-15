from PyUI.Window import Window
##import the custom screens you made---
from PerFrame import PerFrame
from InitVersion import InitVersion
##-------------------------------------


window = Window("Example App", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
perFrame = PerFrame(window)
initFrame = InitVersion(window)
##-----------------------------------

screen = initFrame ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---



    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
