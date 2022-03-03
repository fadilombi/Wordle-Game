import json
import pygame
import random

from pyparsing import Word

pygame.init()


with open("words.json", "r") as f:
    words = json.load(f)


WIDTH, HEIGHT = 600, 750

BLACK = (0,0,0)
YELLOW = (220, 230, 48)
GREEN = (0,255,0)

FONT = 	pygame.font.SysFont("arial", 60)

Win = pygame.display.set_mode((WIDTH, HEIGHT))

WinnerPic = pygame.transform.scale(pygame.image.load("Winner.jpg"), (WIDTH, HEIGHT))

class Box:
    def __init__(self, text, win, x, y):
        self.text = text
        self.win = win
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, 60, 60)
        self.color = (132, 164, 179)


    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
        Win.blit(FONT.render(self.text, True, (255,255,255)), (self.x+10, self.y-10))

def WonScreen(Win):
    Win.blit(WinnerPic, (0,0))
    

def ColorFinding(wordchosen, wordtofind):
    ColorList = [0,0,0,0,0]

    for i in range(len(wordchosen)):

        if wordchosen[i] == wordtofind[i]:
            ColorList[i] = GREEN
        
        elif wordchosen[i] != wordtofind[i] and wordchosen[i] in wordtofind:
            ColorList[i] = YELLOW

        elif wordchosen[i] != wordtofind[i] and wordchosen[i] not in wordtofind:
            ColorList[i] = BLACK

    return ColorList, wordchosen


def DrawBoxes(Boxes):
    StartingPosx = 30
    StartingPosy = 10
    for i in range(1, 7):
        for j in range(1, 6):
            box = Box("", Win, StartingPosx+(j*80), StartingPosy+(i*80))
            Boxes.append(box)

def ChangeBoxColors(WordOrder, Boxes, colorSequence):
    if WordOrder == 0:
        for i in range(5):
            Boxes[i].color = colorSequence[0][i]
            Boxes[i].text = colorSequence[1][i]
    
    elif WordOrder > 0:
        startingPos = WordOrder+(4*WordOrder)
        for i, j in enumerate(range(startingPos, startingPos+5)):
            Boxes[j].color = colorSequence[0][i]
            Boxes[j].text = colorSequence[1][i]

def MainWindow():
    WordOrder = 0
    WordToFind = random.choice(words)
    print(WordToFind)

    Boxes = []
    
    DrawBoxes(Boxes)

    IsFound = False

    while not IsFound:

        pygame.display.update()
        Win.fill((237, 243, 252))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IsFound = True
                break
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    IsFound = True
                    break
            
        
        for bx in Boxes:
            bx.draw()    
        
        WordFile = open("word.txt", "r")
        ChosenWord = WordFile.readlines()
        if len(ChosenWord) > 0:   

            if WordToFind == ChosenWord[0]:
                WonScreen(Win)

            else:
                colorSequence = ColorFinding(ChosenWord[0], str(WordToFind))
                file = open("word.txt", "w")
                file.truncate(0)
                ChangeBoxColors(WordOrder, Boxes, colorSequence)
                WordOrder += 1

        

if __name__ == "__main__":
    MainWindow()