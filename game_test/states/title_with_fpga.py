import pygame
from states.state import State
from states.menu_with_fpga import Menu
from objects.button import Button
from objects.input_text import InputText

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game = game
        self.game.song = 0

        buttonX = self.game.screenWidth/2
        buttonY = self.game.screenHeight*5/7
        buttonWidth = self.game.screenWidth/5
        buttonHeight = self.game.screenHeight/8
        self.button = Button(game, 'Go to menu', buttonX, buttonY, buttonWidth, buttonHeight, 50)
        
        self.titleFont = pygame.font.SysFont('arielblack', 100)
        self.titleText = 'Tilt Dancer'
        self.titleX = self.game.screenWidth/2 - len(self.titleText)*20
        self.titleY = self.game.screenHeight/4 - 30

        self.subTitleFont = pygame.font.SysFont('arielblack', 50)
        self.subTitleText = 'Enter your name:'
        self.subTitleX = self.game.screenWidth/2 - len(self.titleText)*9
        self.subTitleY = self.game.screenHeight*2/5 - 30

        self.inputTextX = buttonX
        self.inputTextY = self.game.screenHeight*4/7
        self.inputText = InputText(game, self.inputTextX, self.inputTextY, 40)
        self.text = ''

    def __titleText(self):
        titleText = self.titleFont.render(self.titleText, False, (255, 255, 255))
        subTitleText = self.subTitleFont.render(self.subTitleText, False, (255, 255, 255))
        self.game.screen.blit(titleText, (self.titleX, self.titleY))
        self.game.screen.blit(subTitleText, (self.subTitleX, self.subTitleY))
    
    def updateEvents():
        pass

    def updateObjects(self, pressedKeys):
        self.text = self.inputText.update()
        self.game.name = self.text

        pressed = self.button.update()
        if pressed:
            print('Player name:', self.text)
        # enter menu state upon user pressing return
        # and send self.text (player name) to the server
            message = [self.text, '_user']
            
            newState = Menu(self.game)
            newState.enterState()

    def updateScreen(self):
        self.game.screen.fill((0, 0, 0))
        # finish this by displaying the players' names and if they are ready
        self.__titleText()
        self.inputText.draw()
        self.button.draw()
        pygame.display.update()
