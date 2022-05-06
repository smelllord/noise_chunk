from random import *
#creates a smooth 2d noise pattern
class Map:
    def __init__(self, length, width, intensity):
        self.length = length 
        self.width = width
        if intensity >= 1:
            self.intensity = 0.99
        elif intensity <= 0:
            self.intensity = 0.01
        else:
            self.intensity = intensity#value between 0.01 and 0.99 (1 and zero make boring maps :[ ). Low intensivity is recoomended
        self.map = [[choice([0,0,0,1]) for _ in range(width)]for i in range(self.length)]
    #generates the 2D array
    def generate(self):
        #coordinates nested for loop
        for pixelY in range(len(self.map)):
            for pixelX in range(len(self.map[pixelY])):
                #warping bc im lazy(-1 is end of list in python)
                neighbors = [[pixelX,pixelY],[pixelX+1,pixelY],[pixelX-1,pixelY],[pixelX,pixelY+1],[pixelX,pixelY-1],[pixelX+1,pixelY+1],[pixelX+1,pixelY-1],[pixelX-1,pixelY+1],[pixelX-1,pixelY-1]]
                
                x = 0
                for pixel in neighbors:
                    if pixel[1] >= self.length or pixel[0] >= self.width:
                        break
                    if self.map[pixel[1]][pixel[0]] >= 1-self.intensity:
                        self.map[pixelY][pixelX] = randint(100-self.intensity*100,100)/100
                        x += 1
                        break
                if x == 0:
                    self.map[pixelY][pixelX] = randint(0,self.intensity*100)/100