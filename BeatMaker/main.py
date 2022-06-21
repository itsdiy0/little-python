import pygame as pg
import sys
import time

#colors
BACKGROUND_COLOR = (183,193,172)
BARS_COLOR = (20, 205, 200)
BARS_COLOR_PRESSED = (255, 148, 112)
FONT_COLOR = (0,0,0)

#cordinates
names_cordinates = {
    "snare" : (90, 95),
    "hi hat" : (300,95),
    "kick" : (520,95),
    "clap" : (95,285),
    "crash" : (305,285),
    "tom" : (525,285)
}
bars_cordinates = {
    "snare" : (20, 20, 190,170),
    "hi hat" : (230, 20, 190,170),
    "kick" : (440, 20, 190,170),
    "clap" : (20, 210, 190,170),
    "crash" : (230, 210, 190,170),
    "tom" : (440, 210, 190,170)
}

def draw_base_bars():
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["snare"])
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["hi hat"])
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["kick"])
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["clap"])
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["crash"])
    pg.draw.rect(screen, BARS_COLOR, bars_cordinates["tom"])
    text = font.render('snare', True, FONT_COLOR)
    screen.blit(text, names_cordinates["snare"])
    text = font.render('hi hat', True, FONT_COLOR)
    screen.blit(text, names_cordinates["hi hat"])
    text = font.render('kick', True, FONT_COLOR)
    screen.blit(text, names_cordinates["kick"])
    text = font.render('clap', True, FONT_COLOR)
    screen.blit(text, names_cordinates["clap"])
    text = font.render('crash', True, FONT_COLOR)
    screen.blit(text, names_cordinates["crash"])
    text = font.render('tom', True, FONT_COLOR)
    screen.blit(text, names_cordinates["tom"])
    pg.display.flip()

def press_bar(cor,key):
    pg.draw.rect(screen, BARS_COLOR_PRESSED, cor)
    text = font.render(key, True, FONT_COLOR)
    screen.blit(text, names_cordinates[key])
    pg.display.flip()
    pg.time.wait(150)
    pg.draw.rect(screen, BARS_COLOR, cor)
    text = font.render(key, True, FONT_COLOR)
    screen.blit(text, names_cordinates[key])
    pg.display.flip()

def load_sounds():
    snare = pg.mixer.Sound("sounds/snare.wav")
    hi_hat = pg.mixer.Sound("sounds/hi_hat.wav")
    kick = pg.mixer.Sound("sounds/kick.wav")
    clap = pg.mixer.Sound("sounds/clap.wav")
    crash = pg.mixer.Sound("sounds/crash.wav")
    tom = pg.mixer.Sound("sounds/tom.wav")
    return snare,hi_hat,kick,clap,crash,tom

if __name__ == '__main__':
    #initialize
    pg.init()
    font = pg.font.SysFont(None, 24)
    screen = pg.display.set_mode((650,400))
    screen.fill(BACKGROUND_COLOR)
    pg.display.set_caption("DRUMS !")
    draw_base_bars()
    pg.display.flip()
    snare,hi_hat,kick,clap,crash,tom = load_sounds()
    #main loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:    
                sys.exit()
            #adding mouse events to bars    
            if event.type == pg.MOUSEBUTTONDOWN:
                x = int(event.pos[0])
                y = int(event.pos[1])
                if y>=20 and y<=190 and x>=20 and x<=210:
                    snare.play()
                    press_bar(bars_cordinates["snare"],"snare")
                if y>=20 and y<=190 and x>=230 and x<=420:
                    hi_hat.play()
                    press_bar(bars_cordinates["hi hat"],"hi hat")
                if y>=20 and y<=190 and x>=440 and x<=630:
                    kick.play()
                    press_bar(bars_cordinates["kick"],"kick")
                if y>=210 and y<=380 and x>=20 and x<=210:
                    clap.play()
                    press_bar(bars_cordinates["clap"],"clap")
                if y>=210 and y<=380 and x>=230 and x<=420:
                    crash.play()
                    press_bar(bars_cordinates["crash"],"crash")
                if y>=210 and y<=380 and x>=440 and x<=630:
                    tom.play()
                    press_bar(bars_cordinates["tom"],"tom") 
            if event.type == pg.KEYDOWN: 
                #adding keyboard events for QWEASD
                if event.key == pg.K_q:
                    snare.play()
                    press_bar(bars_cordinates["snare"],"snare")
                if event.key == pg.K_w:
                    hi_hat.play()
                    press_bar(bars_cordinates["hi hat"],"hi hat")
                if event.key == pg.K_e:
                    kick.play()
                    press_bar(bars_cordinates["kick"],"kick")
                if event.key == pg.K_a:
                    clap.play()
                    press_bar(bars_cordinates["clap"],"clap")
                if event.key == pg.K_s:
                    crash.play()
                    press_bar(bars_cordinates["crash"],"crash")
                if event.key == pg.K_d:
                    tom.play()
                    press_bar(bars_cordinates["tom"],"tom")
                # getting Sheet and autoplay
                if event.key == pg.K_SPACE:
                    sheet = input("Please enter the Sheet you want : ")
                    bpm = int(input("Please enter BPM (8/4 BPM): "))
                    delay = float(input("Please enter delays between : "))
                    interval = 60/bpm/8
                    for i in sheet:
                        if i not in "qweasd-":
                            print("Invalid sheet")
                        if i=="q":
                            snare.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["snare"],"snare")
                        if i=="w":
                            hi_hat.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["hi hat"],"hi hat")
                        if i=="e":
                            kick.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["kick"],"kick")
                        if i=="a":
                            clap.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["clap"],"clap")
                        if i=="s":
                            crash.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["crash"],"crash")          
                        if i=="d":
                            tom.play()
                            time.sleep(interval)
                            press_bar(bars_cordinates["tom"],"tom")
                        if i=="-":
                            time.sleep(delay)
