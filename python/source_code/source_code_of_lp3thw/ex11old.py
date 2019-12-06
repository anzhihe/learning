import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
keep_going=True
GREEN=(0,255,0)#RGB color triplet for GREEN
radius=25
while keep_going:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            keep_going=False
    pygame.draw.circle(screen,GREEN,(100,100),radius)
    pygame.display.update()
pygame.quit()

'''

print ("How old are you?",end=' ')
age= input()
print("How tall are you?",end=' ')
height= input()
print("How much do you weight?",end=' ')
weight=input()
print (f"So, you`re {age} old ,{height} tall and {weight} heavy.")
'''
