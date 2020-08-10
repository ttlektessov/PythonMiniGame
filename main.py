import random
import pygame
from tkinter import *
from pygame.locals import *
from tkinter.messagebox import *
import tkinter.messagebox
global tr
tr=0
def scoretext():
    font_name = pygame.font.match_font('arial')
    font=pygame.font.Font(font_name,24)
    return font.render("Score = " + str(level), 1, (255, 255, 255))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.image=pygame.image.load('spaceship [32].png').convert()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect=self.image.get_rect()
    def update(self,key_pressed):
        if key_pressed[K_UP]:
            self.rect.move_ip(0,-1)
        if key_pressed[K_DOWN]:
            self.rect.move_ip(0,1)
        if key_pressed[K_LEFT]:
            self.rect.move_ip(-1,0)
        if key_pressed[K_RIGHT]:
            self.rect.move_ip(1,0)
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.bottom>600:
            self.rect.bottom=600
        if self.rect.right>700:
            self.rect.left=0
            global level
            global speeds
            level=level+1
            speeds+=1
        if self.rect.left<0:
            self.rect.left=0
            
class Finish(pygame.sprite.Sprite):
    def __init__(self):
        super(Finish,self).__init__()
        self.surf=pygame.Surface((25,600))
        self.surf.fill((255,40,0))
        self.rect=self.surf.get_rect()
       
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.image=pygame.image.load('comet 2.png').convert()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(820,900),random.randint(0,600)))
        self.speed=1
    def update(self):
        global speeds
        self.rect.move_ip(-(self.speed+speeds),0)
        if self.rect.right<=100:
            self.kill()
            
def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def text_objects1(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
class Combodia(pygame.sprite.Sprite):
    def __init__(self):
        super(Combodia,self).__init__()
        self.image=pygame.image.load('elon.png').convert()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect=self.image.get_rect(center=(random.randint(300,500),random.randint(0,600)))
    def update(self):
        self.kill()


def game_intro():
    intro = True
    background_image = pygame.image.load("backg.jpg")
    screen.blit(background_image, [0, 0])
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects1("Cosmo Flight", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2.5))
        screen.blit(TextSurf, TextRect)

        button("LET PLAY", 150, 450, 100, 50, green, bright_green, game)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
def game_chance():
    root=Tk()
    root.attributes("-topmost", True)
    root.title("Quiz")
    root.geometry('500x300')
    q = Label(root, text="Give right answer to continue",font="Arial 11");
    q.pack()
    def call(par):
        print(par)
        if par==0:
            root.destroy()
            game()
        else:
            message="Wrong answer!"
            title="Sorry".title()
            tkinter.messagebox.showinfo(title, message)
            pygame.quit()  
            quit()
    correct=StringVar()
    correct1=StringVar()
    correct2=StringVar()
    q1=Label(root,text="Q1) Callisto is a moon of which palnet?",)
    q1.place(x=0,y=20)
    rad = Radiobutton(root, text='Jupiter', variable=correct, value=0)
    rad2 = Radiobutton(root, text='Saturn', variable=correct, value=1)
    rad3 = Radiobutton(root, text='Mars', variable=correct, value=2)
    rad.place(x=250,y=20)
    rad2.place(x=250,y=40)
    rad3.place(x=250,y=60)
    q2=Label(root,text="\nQ2) What is the closest elliptical galaxy?")
    q2.place(x=0,y=80)
    rad4 = Radiobutton(root, text='Andromeda', variable=correct1, value=1)
    rad5 = Radiobutton(root, text='The Sagittarius Dwarf elliptical galaxy', variable=correct1, value=0)
    rad4.place(x=250,y=95)
    rad5.place(x=250,y=115)
    q3=Label(root,text="\nQ3) What is the temperature of Sun's surface?")
    q3.place(x=0,y=135)
    rad6 = Radiobutton(root,text='5443 K',variable=correct2,value=1)
    rad7 = Radiobutton(root,text='5778 K',variable=correct2,value=0)
    rad8 = Radiobutton(root,text='4703 K',variable=correct2,value=2)
    rad9 = Radiobutton(root,text='6003 K',variable=correct2,value=3)
    rad6.place(x=250,y=150)
    rad7.place(x=250,y=170)
    rad8.place(x=250,y=190)
    rad9.place(x=250,y=210)
    correct.set(None)
    correct1.set(None)
    correct2.set(None)
    btn = Button(root, text='Submit',font="Arial 12", command=lambda: call(int(correct.get())+int(correct1.get())+int(correct2.get())))
    btn.place(x=220,y=250)
    global tr
    tr=1 
    root.mainloop()
def game():
    pygame.init()
    level=0
    finish=Finish()
    ADDENEMY=pygame.USEREVENT+5
    all_sprites=pygame.sprite.Group()
    enemies=pygame.sprite.Group()
    pygame.time.set_timer(ADDENEMY,500)
    combodias=pygame.sprite.Group()
    SPAWNCOMBODIA=pygame.USEREVENT+2
    pygame.time.set_timer(SPAWNCOMBODIA,9000)
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption('Cosmo Flight')
    player=Player()
    all_sprites.add(player)
    background_image = pygame.image.load("background.jpg").convert()
    MOVEENEMY=pygame.USEREVENT+1
    pygame.time.set_timer(MOVEENEMY,1)
    icon= pygame.image.load('galaxy 2.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
            if event.type==QUIT:
                running=False
            if event.type==SPAWNCOMBODIA:
                combodia=Combodia()
                all_sprites.add(combodia)
                combodias.add(combodia)
            if event.type==ADDENEMY:
                enemy=Enemy()
                enemies.add(enemy)
                all_sprites.add(enemy)
            if event.type == MOVEENEMY:
                enemies.update()
        pressed_key=pygame.key.get_pressed()
        player.update(pressed_key)
        screen.blit(background_image, [0, 0])
        screen.blit(scoretext(), (5, 10))
        screen.blit(finish.surf,(700,0))
        for entity in all_sprites:
            screen.blit(entity.image,entity.rect)
        if pygame.sprite.spritecollideany(player,enemies):
            player.kill()
            crash()
            running=False
        if pygame.sprite.spritecollideany(player,combodias):
            combodias.update()
            global speeds
            speeds=0
        pygame.display.flip()

def crash():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects1("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2.5))
    screen.blit(TextSurf, TextRect)
    global tr
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if tr==0:
            button("Chance to live", 150, 450, 150, 50, green, bright_green, game_chance)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)
pygame.init()
level=0
speeds=0
finish=Finish()
ADDENEMY=pygame.USEREVENT+5
all_sprites=pygame.sprite.Group()
enemies=pygame.sprite.Group()
pygame.time.set_timer(ADDENEMY,500)
combodias=pygame.sprite.Group()
SPAWNCOMBODIA=pygame.USEREVENT+2
pygame.time.set_timer(SPAWNCOMBODIA,9000)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Cosmo Flight')
player=Player()
all_sprites.add(player)
background_image = pygame.image.load("background.jpg").convert()
MOVEENEMY=pygame.USEREVENT+1
pygame.time.set_timer(MOVEENEMY,1)
icon= pygame.image.load('galaxy 2.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)
game_intro()
game()
pygame.quit()
quit()
