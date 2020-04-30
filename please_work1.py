import math
import random
import sys
import time
import pygame
from pygame.locals import *

# import time
pygame.init()
Surface = pygame.display.set_mode((800, 600))

# Create Empty lists
circleHolder = []
infectedNumber = 0
recoveredNumber = 0
t0 = 0
t1 = 0
totalTime = 0


def main():
    while True:
        GetInput()
        Move()
        Draw()
        CollisionDetect()


class Circle:
    def __init__(self, k=0):
        self.radius = 5
        self.x = random.randint(self.radius, 800 - (2 * self.radius + 10))
        self.y = random.randint(self.radius, 600 - (2 * self.radius + 10))
        self.speedx = 0.5 * (random.random() + 2)
        self.speedy = 0.5 * (random.random() + 2)
        self.Infected = False
        self.Susceptible = False
        self.Removed = False
        self.NewColor = False
        self.FirstHit = False
        self.InfectedTime = 0

        if k == 1:
            self.Infected = True
            self.InfectedTime = time.time()

        else:
            self.Susceptible = True


for x in range(100):
    circleHolder.append(Circle(0))
for x in range(1):
    circleHolder.append(Circle(1))


#     Circle.NewColor = True
#     Circle.Infected = True

def CircleCollide(c1, c2):
    global infectedNumber

    C1Speed = math.sqrt((c1.speedx ** 2) + (c1.speedy ** 2))
    XDiff = -(c1.x - c2.x)
    YDiff = -(c1.y - c2.y)

    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff / XDiff))
            XSpeed = -C1Speed * math.cos(math.radians(Angle))
            YSpeed = -C1Speed * math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff / XDiff))
            XSpeed = -C1Speed * math.cos(math.radians(Angle))
            YSpeed = -C1Speed * math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff / XDiff))
            XSpeed = -C1Speed * math.cos(math.radians(Angle))
            YSpeed = -C1Speed * math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff / XDiff))
            XSpeed = -C1Speed * math.cos(math.radians(Angle))
            YSpeed = -C1Speed * math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed * math.cos(math.radians(Angle))
        YSpeed = C1Speed * math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed * math.cos(math.radians(Angle))
        YSpeed = C1Speed * math.sin(math.radians(Angle))
    else:
        print("helllo")

    if (c1.Susceptible and c2.Infected) is True:
        c1.NewColor = True
        c2.NewColor = True
        c1.FirstHit = True
        c2.FirstHit = True
        c1.Susceptible = False
        c1.Infected = True
        infectedNumber = infectedNumber + 1
        print("Number of Infected: ")
        print(infectedNumber)
        c1.InfectedTime = time.time()

    elif (c1.Infected and c2.Susceptible) is True:
        c1.NewColor = True
        c2.NewColor = True
        c1.FirstHit = True
        c2.FirstHit = True
        c2.Susceptible = False
        c2.Infected = True
        infectedNumber = infectedNumber + 1
        print("Number of Infected: ")
        print(infectedNumber)
        c2.InfectedTime = time.time()

    c1.speedx = XSpeed
    c1.speedy = YSpeed
    pygame.display.flip()


def Move():
    for Circle in circleHolder:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy


def CollisionDetect():
    # hitting wall
    for Circle in circleHolder:
        if Circle.x < Circle.radius or Circle.x > 800 - (2 * Circle.radius + 10):
            Circle.speedx *= -1
        if Circle.y < Circle.radius or Circle.y > 600 - (2 * Circle.radius + 10):
            Circle.speedy *= -1

    # hitting each other
    for Circle in circleHolder:
        for Circle2 in circleHolder:
            if Circle != Circle2:
                if math.sqrt(((Circle.x - Circle2.x) ** 2) + ((Circle.y - Circle2.y) ** 2)) <= (
                        Circle.radius + Circle2.radius):
                    CircleCollide(Circle, Circle2)


def Draw():
    global t0
    global t1
    global totalTime
    global infectedNumber
    global recoveredNumber

    if infectedNumber == 2:
        t0 = time.time()
    if infectedNumber == 100:
        t1 = time.time()
        totalTime = t1 - t0
        print(totalTime)
        infectedNumber = 101

    for Circle in circleHolder:
        if Circle.InfectedTime > 0 and Circle.Removed == False:
            timeHolder = (time.time() - Circle.InfectedTime)
            if 14 <= timeHolder <= 15:
                Circle.Removed = True
                Circle.Infected = False
                Circle.NewColor = False
                recoveredNumber = recoveredNumber + 1
                print("Number Recovered: ")
                print(recoveredNumber)

    Surface.fill((255, 255, 255))
    for Circle in circleHolder:
        if Circle.NewColor:
            pygame.draw.circle(Surface, (150, 0, 0), (int(Circle.x), int(600 - Circle.y)), Circle.radius)
            # start timer for 10 seconds, when time runs out switch color to Removed.
        elif Circle.Removed:
            pygame.draw.circle(Surface, (0, 150, 0), (int(Circle.x), int(600 - Circle.y)), Circle.radius)
        else:
            pygame.draw.circle(Surface, (0, 0, 150), (int(Circle.x), int(600 - Circle.y)), Circle.radius)

    pygame.display.flip()


def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit();
            sys.exit()


if __name__ == '__main__': main()
