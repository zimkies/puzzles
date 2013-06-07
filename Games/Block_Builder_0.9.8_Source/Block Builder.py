# No, fail... try:
print "Loading chipmunk---"
import pymunk
print "Loaded---"
print "Loading other modules---"
import pygame
#import psyco
import pickle
import os, sys
import math, random, time
import urllib
print "Loaded---"
print

print "Ready to start! Launching window!"
print
print "Arguments:"
for arg in sys.argv:
    print "\t"+str(arg)
print

X,Y = 0,1
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_EXPLOSION = 2
COLLTYPE_CHAR = 3
COLLTYPE_FIRE = 4

class storer():
    def __init__(self):
        self.version="0.9.8"
        self.curr_version="0.0.0"
        self.state="menu"
        self.have_connection=False
        self.numbers={pygame.K_0:0, pygame.K_1:1, pygame.K_2:2, pygame.K_3:3, pygame.K_4:4,
                        pygame.K_5:5, pygame.K_6:6, pygame.K_7:7, pygame.K_8:8, pygame.K_9:9,
                        pygame.K_MINUS:"-"}
        self.letters={}
        self.ddown=False
        self.lines=[]
        self.balls=[]
        self.explosions=[]
        self.polys=[]
        self.springs=[]
        self.motors = []
        self.rods=[]
        self.pins=[]
        self.drop_item="line"
        self.all=[]
        self.totald=[0,0]
        self.old=[None,None]
        self.marbleim={}
        self.n=0
        self.explodeimgsequence=[]
        self.fireimgsequence=[]
        self.colors={"adding":[0,255,0]}
        self.gravityposition=[23,44]
        self.menu_state="tool"
        self.square_size=20
        self.circle_size=10
        self.line_width=2
        self.explosion_power=100
        self.motor_rate = 10
        self.char_jumped=False
        self.mh=575
        self.menux=1000
        self.old_pos=[0,0]
        self.menuy=660
        self.about_on = False
        self.char = None
        self.delete_down = False
        self.save_name = ""
        self.load_name = ""
        self.files=[[]]
        self.current_page=0
        self.speed = 60.0
        self.selection = None
        self.campos=[0,0]
        self.menu_state="start"
        self.check_updates()
        self.move_frame=0
        self.draw_delay=15
        self.line_constrain=None
        self.poly_points=[]
        
    def find_all(self):
        self.files=[[]]
        for path, dirs, files in os.walk("levels/"):
            for file in files:
                if len(self.files[-1]) == 20:
                    self.files.append([])
                self.files[-1].append(file[:-5])
        for item in self.files:
            print item
            
    def check_updates(self):
        try:
            update_site=urllib.urlopen("http://www.eggplantanimation.com/current_bb_version.txt")
            self.curr_version=update_site.read()
            self.have_connection=True
        except:
            self.have_connection=False


    def update_ingame_menu(self):
        #pygame.draw.rect(screen, [85, 80, 250], [0, 600, 600, 60], 0)
        screen.blit(menubar, [0,self.mh])

        #---Box button-------------
        pygame.draw.rect(screen, [0,0,0], [515, self.mh+5, 35, 27], 3)
        if self.drop_item=="box":
            pygame.draw.rect(screen, [255, 255, 255], [517, self.mh+7, 31, 23], 0)
        screen.blit(boxdropimg, [520, self.mh+10])
        #-----------------------

        #---Explode button-------------
        pygame.draw.rect(screen, [0,0,0], [430, self.mh+5, 80, 27], 3)
        if self.drop_item=="explosion":
            pygame.draw.rect(screen, [255, 255, 255], [432, self.mh+7, 76, 23], 0)
        screen.blit(explosiondropimg, [435, self.mh+10])
        #-----------------------

        #---Fire button-------------
        pygame.draw.rect(screen, [0,0,0], [390, self.mh+5, 36, 27], 3)
        if self.drop_item=="fire":
            pygame.draw.rect(screen, [255, 255, 255], [392, self.mh+7, 32, 23], 0)
        screen.blit(firedropimg, [395, self.mh+10])
        #-----------------------
        
        #---Draw button-------------
        pygame.draw.rect(screen, [0,0,0], [432, self.mh+60, 41, 22], 3)
        if self.drop_item=="draw":
            pygame.draw.rect(screen, [255, 255, 255], [434, self.mh+62, 37, 18], 0)
        screen.blit(drawdropimg, [436, self.mh+62])
        #-----------------------
        
        #---Poly button-------------
        pygame.draw.rect(screen, [0,0,0], [477, self.mh+60, 41, 22], 3)
        if self.drop_item=="poly":
            pygame.draw.rect(screen, [255, 255, 255], [479, self.mh+62, 37, 18], 0)
        screen.blit(polydropimg, [481, self.mh+62])
        #-----------------------

        #---Motor button-------------
        pygame.draw.rect(screen, [0,0,0], [330, self.mh+5, 56, 27], 3)
        if self.drop_item=="motor":
            pygame.draw.rect(screen, [255, 255, 255], [332, self.mh+7, 52, 23], 0)
        screen.blit(motordropimg, [334, self.mh+10])
        #-----------------------

        #---Character button-------------
        pygame.draw.rect(screen, [0,0,0], [585, self.mh+35, 88, 22], 3)
        if self.drop_item=="character":
            pygame.draw.rect(screen, [255, 255, 255], [587, self.mh+37, 84, 18], 0)
        screen.blit(characterdropimg, [590, self.mh+37])
        #-----------------------

        #---Square button----------
        pygame.draw.rect(screen, [0,0,0], [515, self.mh+35, 65, 22], 3)
        if self.drop_item=="square":
            pygame.draw.rect(screen, [255, 255, 255], [517, self.mh+37, 61, 18], 0)
        screen.blit(squaredropimg, [520, self.mh+37])
        #------------------------

        #---Spring button----------
        pygame.draw.rect(screen, [0,0,0], [450, self.mh+35, 60, 22], 3)
        if self.drop_item=="spring":
            pygame.draw.rect(screen, [255, 255, 255], [453, self.mh+37, 55, 18], 0)
        screen.blit(springdropimg, [455, self.mh+37])
        #------------------------

        #---Line button----------
        pygame.draw.rect(screen, [0,0,0], [410, self.mh+35, 35, 22], 3)
        if self.drop_item=="line":
            pygame.draw.rect(screen, [255, 255, 255], [413, self.mh+37, 30, 18], 0)
        screen.blit(linedropimg, [414, self.mh+37])
        #------------------------
        
        #---Car button----------
        pygame.draw.rect(screen, [0,0,0], [598, self.mh+5, 35, 27], 3)
        if self.drop_item=="car":
            pygame.draw.rect(screen, [255, 255, 255], [601, self.mh+7, 30, 23], 0)
        screen.blit(cardropimg, [602, self.mh+10])
        #------------------------
        
        #---Pin button----------
        pygame.draw.rect(screen, [0,0,0], [638, self.mh+5, 35, 27], 3)
        if self.drop_item=="pin":
            pygame.draw.rect(screen, [255, 255, 255], [641, self.mh+7, 30, 23], 0)
        screen.blit(pindropimg, [642, self.mh+10])
        #------------------------
        
        #---Missile button----------
        #TODO: Make Missiles!
        #pygame.draw.rect(screen, [0,0,0], [598, self.mh+5, 35, 27], 3)
        #if self.drop_item=="car":
            #pygame.draw.rect(screen, [255, 255, 255], [601, self.mh+7, 30, 23], 0)
        #screen.blit(cardropimg, [602, self.mh+10])
        #------------------------

        #---Grab button----------
        pygame.draw.rect(screen, [0,0,0], [363, self.mh+35, 43, 22], 3)
        if self.drop_item=="grab":
            pygame.draw.rect(screen, [255, 255, 255], [366, self.mh+37, 38, 18], 0)
        screen.blit(grabdropimg, [367, self.mh+37])
        #------------------------

        #---Rod button----------
        pygame.draw.rect(screen, [0,0,0], [393, self.mh+60, 35, 22], 3)
        if self.drop_item=="rod":
            pygame.draw.rect(screen, [255, 255, 255], [396, self.mh+62, 35, 18], 0)
        screen.blit(roddropimg, [397, self.mh+62])
        #------------------------
        
        #---Ball button-------------
        pygame.draw.rect(screen, [0,0,0], [555, self.mh+5, 38, 27], 3)
        if self.drop_item=="ball":
            pygame.draw.rect(screen, [255, 255, 255], [557, self.mh+7, 34, 23], 0)
        screen.blit(balldropimg, [560, self.mh+10])
        #----------------------------

        #---Save button-------------
        pygame.draw.rect(screen, [0,0,0], [55, self.mh+5, 44, 27], 3)
        screen.blit(saveimg, [60, self.mh+10])
        #----------------------------

        #---Clear button-------------
        pygame.draw.rect(screen, [0,0,0], [105, self.mh+5, 53, 27], 3)
        screen.blit(clearimg, [110, self.mh+10])
        #----------------------------

        #---Clear moveables button-------------
        pygame.draw.rect(screen, [0,0,0], [55, self.mh+35, 135, 23], 3)
        screen.blit(clearmoveablesimg, [60, self.mh+37])
        #----------------------------

        #---Load button-------------
        pygame.draw.rect(screen, [0,0,0], [5, self.mh+35, 44, 23], 3)
        screen.blit(loadimg, [10, self.mh+37])
        #----------------------------

        #---Menu button-------------
        pygame.draw.rect(screen, [0,0,0], [5, self.mh+5, 44, 27], 3)
        screen.blit(menuimg, [10, self.mh+10])
        #----------------------------
        
        #---Copy button-------------
        pygame.draw.rect(screen, [0,0,0], [195, self.mh+61, 44, 21], 3)
        if self.drop_item == "copy":
            pygame.draw.rect(screen, [255, 255, 255], [197, self.mh+63, 40, 17], 0)
        screen.blit(copyimg, [198, self.mh+62])
        #---------------------------

        #---Delete button-------------
        pygame.draw.rect(screen, [0,0,0], [195, self.mh+35, 54, 23], 3)
        if self.drop_item == "delete":
            pygame.draw.rect(screen, [255, 255, 255], [197, self.mh+37, 50, 19], 0)
        screen.blit(deleteimg, [200, self.mh+37])
        #---------------------------

        #---Gravity button-------------
        pygame.draw.rect(screen, [0,0,0], [720, self.mh+5, 69, 27], 3)
        if self.menu_state=="gravity":
            pygame.draw.rect(screen, [255, 255, 255], [722, self.mh+7, 65, 23], 0)
        screen.blit(gravityimg, [725, self.mh+10])
        #----------------------------

        #---Tool button-------------
        pygame.draw.rect(screen, [0,0,0], [720, self.mh+35, 45, 22], 3)
        if self.menu_state!="gravity":
            pygame.draw.rect(screen, [255, 255, 255], [722, self.mh+37, 41, 18], 0)
        screen.blit(toolimg, [725, self.mh+37])
        #----------------------------

        if self.menu_state=="gravity":
            self.draw_gravity_menu()

        if self.menu_state=="tool":
            self.draw_tool_menu()

    def clean_up(self, list):
        for item in list:
            if item.body.position.y<-1000:
                try:
                    self.remove_all_constraints(item)
                    list.remove(item)
                    space.remove(item, item.body)
                except:
                    pass

    def clean_up_constraints(self):
        for spring in self.springs:
            if spring.a == spring.b:
                print "Orphan Spring"

    def menu_update(self):
        screen.fill([85, 80, 250])
        screen.blit(menuback, [200, 0])
        pygame.draw.rect(screen, [254, 169, 65], [280, 0, 2500, 2000], 0)
        screen.blit(title, [(store.menux/2)-int((titlefont.size("Block Builder")[0]/2))+120, 0])

        #[254, 169, 65]
        
        #---Start Button-----------------------
        startrect=[5, 5, 191, 65]
        pygame.draw.rect(screen, [0,0,0], startrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), startrect):
            pygame.draw.rect(screen, [255, 255, 255], [startrect[0]+2, startrect[1]+2, startrect[2]-4, startrect[3]-4], 0)
        if self.menu_state=="start":
            pygame.draw.rect(screen, [254, 169, 65], [startrect[0]+2, startrect[1]+2, startrect[2]-4, startrect[3]-4], 0)    
        screen.blit(startbuttonimg, [startrect[0]+5, startrect[1]-3])
        #----------------------------------

        #---Play Button-----------------------
        playrect=[5, 100, 140, 65]
        pygame.draw.rect(screen, [0,0,0], playrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), playrect):
            pygame.draw.rect(screen, [255, 255, 255], [playrect[0]+2, playrect[1]+2, playrect[2]-4, playrect[3]-4], 0)
        screen.blit(playbuttonimg, [playrect[0]+5, playrect[1]-3])
        #----------------------------------
        
        #---Settings Button-----------------------
        settingsrect=[5, 495, 140, 65]
        pygame.draw.rect(screen, [0,0,0], settingsrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), settingsrect):
            pygame.draw.rect(screen, [255, 255, 255], [settingsrect[0]+2, settingsrect[1]+2, settingsrect[2]-4, settingsrect[3]-4], 0)
        screen.blit(settingsbuttonimg, [settingsrect[0]+5, settingsrect[1]+16])
        #----------------------------------
        
        #---Load Button-----------------------
        loadrect=[5, 195, 145, 65]
        pygame.draw.rect(screen, [0,0,0], loadrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), loadrect):
            pygame.draw.rect(screen, [255, 255, 255], [loadrect[0]+2, loadrect[1]+2, loadrect[2]-4, loadrect[3]-4], 0)
        if self.menu_state=="load":
            pygame.draw.rect(screen, [254, 169, 65], [loadrect[0]+2, loadrect[1]+2, loadrect[2]-4, loadrect[3]-4], 0)
        screen.blit(loadbuttonimg, [loadrect[0]+5, loadrect[1]-3])
        #----------------------------------

        #---About Button-----------------------
        aboutrect=[5, 400, 190, 65]
        pygame.draw.rect(screen, [0,0,0], aboutrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), aboutrect):
            pygame.draw.rect(screen, [255, 255, 255], [aboutrect[0]+2, aboutrect[1]+2, aboutrect[2]-4, aboutrect[3]-4], 0)
        if self.menu_state=="about":
            pygame.draw.rect(screen, [254, 169, 65], [aboutrect[0]+2, aboutrect[1]+2, aboutrect[2]-4, aboutrect[3]-4], 0)
        screen.blit(aboutbuttonimg, [aboutrect[0]+5, aboutrect[1]-3])
        #----------------------------------
        if store.menu_state=="start":
            box_pos=[(store.menux/2)-200+120,575]
            pygame.draw.rect(screen, [85, 80, 250],[box_pos[0]+1, box_pos[1]+1,399,74], 0)
            pygame.draw.rect(screen, [0,0,0],[box_pos[0], box_pos[1],400,75], 3)
            screen.blit(font.render("Updates:", 1, [0,0,0]), [box_pos[0]+165, box_pos[1]+5])
            screen.blit(font.render("This is BlockBuilder version: "+self.version, 1, [0,0,0]), [box_pos[0]+68, box_pos[1]+30])
            if self.have_connection:
                if self.version==self.curr_version:
                    screen.blit(font.render("You have the latest version!", 1, [0,0,0]), [box_pos[0]+85, box_pos[1]+55])
                else:
                    screen.blit(font.render("There is a new version available. Click here:", 1, [0,0,0]), [box_pos[0]+5, box_pos[1]+53])
            else:
                screen.blit(font.render("Could not connect to update server.", 1, [0,0,0]), [box_pos[0]+5, box_pos[1]+53])
                
            box_pos=[(store.menux/2)-300+120,125]
            pygame.draw.rect(screen, [85, 80, 250],[box_pos[0]+1, box_pos[1]+1,599,374], 0)
            pygame.draw.rect(screen, [0,0,0],[box_pos[0], box_pos[1],600,375], 3)
            screen.blit(font.render("News:", 1, [0,0,0]), [box_pos[0]+165, box_pos[1]+5])
            #screen.blit(font.render("This is BlockBuilder version: "+self.version, 1, [0,0,0]), [box_pos[0]+68, box_pos[1]+30])
            #if self.have_connection:
                #if self.version==self.curr_version:
                    #screen.blit(font.render("You have the latest version!", 1, [0,0,0]), [box_pos[0]+85, box_pos[1]+55])
                #else:
                    #screen.blit(font.render("There is a new version available. Click here:", 1, [0,0,0]), [box_pos[0]+5, box_pos[1]+53])
            #else:
                #screen.blit(font.render("Could not connect to update server.", 1, [0,0,0]), [box_pos[0]+5, box_pos[1]+53])
                
        if store.menu_state=="about":
            mid=int(store.menux/2)+100
            #screen.blit(abouttrans, [0,0])
            screen.blit(aboutbuttonimg, [mid-(aboutbuttonimg.get_width()/2), 100])
            screen.blit(line_1, [mid-(line_1.get_width()/2), 180])
            screen.blit(line_2, [mid-(line_2.get_width()/2), 215])
            screen.blit(line_3, [mid-(line_3.get_width()/2), 270])
            screen.blit(line_4, [mid-(line_4.get_width()/2), 305])
            screen.blit(line_5, [mid-(line_5.get_width()/2), 330])
            screen.blit(line_6, [mid-(line_6.get_width()/2), 365])
            screen.blit(line_7, [mid-(line_7.get_width()/2), 400])
            screen.blit(line_8, [mid-(line_8.get_width()/2), 435])
            screen.blit(line_9, [mid-(line_9.get_width()/2), 490])
            screen.blit(line_10, [mid-(line_10.get_width()/2), 525])
            
        if store.menu_state=="load":
            pygame.draw.rect(screen, [85, 80, 250], [(self.menux/2)-110, 140, 420, 500], 0)
            pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-110, 140, 420, 500], 3)
            pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-100, 150, 400, 30], 0)
            pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-100, 150, 400, 30], 3)
            screen.blit(font.render(store.load_name, 1, [0,0,0]), [(self.menux/2)-95, 155])
            pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-100, 195, 400, 405], 0)
            pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-100, 195, 400, 405], 3)
            if store.selection != None:
                pygame.draw.rect(screen, [255, 0, 0], [(store.menux/2)-97,(store.selection*20)+198, font.size(store.load_name)[0]+4, 20], 0)
            for y in range(len(self.files[self.current_page])):
                screen.blit(font.render(self.files[self.current_page][y], 1, [0,0,0]), [(store.menux/2)-95,200+(y*20)])
            #---Load button-------------
            pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+103, 606, 44, 27], 3)
            screen.blit(loadimg, [(store.menux/2)+108, 611])
            #----------------------------
            #---Previous button-------------
            pygame.draw.rect(screen, [0,0,0], [(store.menux/2)-100, 606, 75, 27], 3)
            screen.blit(previousimg, [(store.menux/2)-95, 611])
            #----------------------------
            #---Next button-------------
            pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+255, 606, 45, 27], 3)
            screen.blit(nextimg, [(store.menux/2)+262, 611])
            #----------------------------

        #---Exit Button-----------------------
        exitrect=[5, 590, 140, 65]
        pygame.draw.rect(screen, [85, 80, 250], exitrect, 0)
        pygame.draw.rect(screen, [0,0,0], exitrect, 3)
        if self.check_bounds(pygame.mouse.get_pos(), exitrect):
            pygame.draw.rect(screen, [255, 255, 255], [exitrect[0]+2, exitrect[1]+2, exitrect[2]-4, exitrect[3]-4], 0)
        screen.blit(exitbuttonimg, [exitrect[0]+5, exitrect[1]-3])
        #----------------------------------
        
    def save_update(self):
        pygame.draw.rect(screen, [254, 169, 65], [(self.menux/2)-210, 40, 420, 500], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-210, 40, 420, 500], 3)
        pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-200, 50, 400, 30], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-200, 50, 400, 30], 3)
        screen.blit(font.render(store.save_name, 1, [0,0,0]), [(self.menux/2)-195, 55])
        pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-200, 95, 400, 405], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-200, 95, 400, 405], 3)
        for y in range(len(self.files[self.current_page])):
            screen.blit(font.render(self.files[self.current_page][y], 1, [0,0,0]), [(store.menux/2)-195,100+(y*20)])
        #---Save button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+3, 506, 44, 27], 3)
        screen.blit(saveimg, [(store.menux/2)+8, 511])
        #----------------------------
        #---Cancel button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)-61, 506, 60, 27], 3)
        screen.blit(cancelimg, [(store.menux/2)-56, 511])
        #----------------------------
        #---Previous button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)-200, 506, 75, 27], 3)
        screen.blit(previousimg, [(store.menux/2)-195, 511])
        #----------------------------
        #---Next button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+155, 506, 45, 27], 3)
        screen.blit(nextimg, [(store.menux/2)+162, 511])
        #----------------------------
        
    def load_update(self):
        pygame.draw.rect(screen, [254, 169, 65], [(self.menux/2)-210, 40, 420, 500], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-210, 40, 420, 500], 3)
        pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-200, 50, 400, 30], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-200, 50, 400, 30], 3)
        screen.blit(font.render(store.load_name, 1, [0,0,0]), [(self.menux/2)-195, 55])
        pygame.draw.rect(screen, [255, 255, 255], [(self.menux/2)-200, 95, 400, 405], 0)
        pygame.draw.rect(screen, [0,0,0], [(self.menux/2)-200, 95, 400, 405], 3)
        if store.selection != None:
            pygame.draw.rect(screen, [255, 0, 0], [(store.menux/2)-197,(store.selection*20)+98, font.size(store.load_name)[0]+4, 20], 0)
        for y in range(len(self.files[self.current_page])):
            screen.blit(font.render(self.files[self.current_page][y], 1, [0,0,0]), [(store.menux/2)-195,100+(y*20)])
        #---Load button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+3, 506, 44, 27], 3)
        screen.blit(loadimg, [(store.menux/2)+8, 511])
        #----------------------------
        #---Cancel button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)-61, 506, 60, 27], 3)
        screen.blit(cancelimg, [(store.menux/2)-56, 511])
        #----------------------------
        #---Previous button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)-200, 506, 75, 27], 3)
        screen.blit(previousimg, [(store.menux/2)-195, 511])
        #----------------------------
        #---Next button-------------
        pygame.draw.rect(screen, [0,0,0], [(store.menux/2)+155, 506, 45, 27], 3)
        screen.blit(nextimg, [(store.menux/2)+162, 511])
        #----------------------------

    def game_update(self):
        p = pygame.mouse.get_pos()
        mouse_pos = pymunk.Vec2d(p[0]-store.campos[0],flipy(p[Y])+store.campos[1])
        mouse_body.position = mouse_pos

        if run_physics:
            dt = 1.0/self.speed
            for x in range(1):
                try:
                    space.step(dt)
                except:
                    print "Error Stepping World Physics"
            for item in store.lines:
                if item.kill_me == True:
                    try:
                        store.lines.remove(item)
                        store.all.remove(item)
                        space.remove(item, item.body)
                    except:
                        pass
            for item in store.balls:
                if item.kill_me == True:
                    try:
                        store.remove_all_constraints(item)
                        space.remove(item, item.body)
                        store.all.remove(item)
                        store.balls.remove(item)
                    except:
                        pass
            for item in store.polys:
                if item.kill_me == True:
                    store.remove_all_constraints(item)
                    space.remove(item, item.body)
                    store.polys.remove(item)
                    store.all.remove(item)
                    for body in space.bodies:
                        if body==item.body:
                            del body
                        
                    #except:
                        #pass

            self.clean_up_constraints()
            #except:
            #    pass

        screen.fill([255, 255, 255])

        for ball in self.balls:
            r = ball.radius
            v = ball.body.position
            rot = ball.body.rotation_vector
            p = int(v.x)+self.campos[0], int(flipy(v.y)-self.campos[1])
            p2 = pymunk.Vec2d(rot.x, -rot.y) * r * 0.9
            if ball.collision_type==COLLTYPE_FIRE:
                pygame.draw.circle(screen, [0,0,0], p, int(r), 0)
                pygame.draw.line(screen, [255,0,0], p, p+p2)
                screen.blit(store.fireimgsequence[int(r)][ball.burn_level/15], [p[0]-r, p[1]-((ball.burn_level/10)*5)])
                ball.burn_level+=1
                if ball.burn_level >= 75:
                    ball.unsafe_set_radius(ball.radius-1)
                    ball.burn_level = 0
                    if ball.radius < 3:
                        try:
                            store.remove_all_constraints(ball)
                            space.remove(ball, ball.body)
                            store.all.remove(ball)
                            store.balls.remove(ball)
                        except:
                            pass

            else:
                pygame.draw.circle(screen, [0,0,255], p, int(r), 0)
                #screen.blit(store.marbleim[rot], p)
                pygame.draw.line(screen, [255,0,0], p, p+p2)

        if line_point1 is not None:
            p1 = [line_point1.x+self.campos[0], flipy(line_point1.y)-self.campos[1]]
            p2 = mouse_pos.x+self.campos[0], flipy(mouse_pos.y)-self.campos[1]
            pygame.draw.lines(screen, [0,255,0], False, [p1,p2])

        for line in self.lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)+self.campos
            pv2 = body.position + line.b.rotated(body.angle)+self.campos
            p1 = [pv1.x, flipy(pv1.y)]
            p2 = [pv2.x, flipy(pv2.y)]
            pygame.draw.line(screen, [0,0,0], p1, p2, int(line.radius*2))
            #pygame.draw.aaline(screen, [0,0,0], p1,p2)
            #p1[1]+=1
            #p2[1]+=1
            pygame.draw.circle(screen, [0,0,0], p1, int(line.radius), 0)
            pygame.draw.circle(screen, [0,0,0], p2, int(line.radius), 0)

        for poly in self.polys:
            #ball.burn_level+=1
            #if ball.burn_level >= 75:
            #    ball.unsafe_set_radius(ball.radius-1)
            #    ball.burn_level = 0
            #    if ball.radius < 3:
            #        try:
            #            store.remove_all_constraints(ball)
            #            space.remove(ball, ball.body)
            #            store.all.remove(ball)
            #            store.balls.remove(ball)
            #        except:
            #            pass
            #    else:
                self.draw_poly(poly)

        for explosion in self.explosions:
            r = explosion.radius
            v = explosion.body.position
            rot = explosion.body.rotation_vector
            p = int(v.x)-self.campos[0], int(flipy(v.y))+self.campos[1]
            p=[p[0], p[1]]
            p[0]= int(p[0]-r)
            p[1]= int(p[1]-r)
            p2 = pymunk.Vec2d(rot.x, -rot.y) * r * 0.9
            #explosionimgscale=pygame.transform.scale(explosionimg, [int(2*r), int(2*r)])
            #screen.blit(explosionimgscale, p)
            screen.blit(self.explodeimgsequence[int(r)], p)
            for i in range(0, 5):
                explosion.unsafe_set_radius(explosion.radius + i)
            if explosion.radius > 200:
                self.explosions.remove(explosion)
                self.all.remove(explosion)
                space.remove(explosion)

        if self.ddown == True:
            pygame.draw.circle(screen, [255, 0, 0, 100], pygame.mouse.get_pos(), 5, 0)

        if box_point1 is not None:
            if box_point1.x < pygame.mouse.get_pos()[0] and -box_point1.y+600 < pygame.mouse.get_pos()[1]:
                diff = [abs(box_point1.x-pygame.mouse.get_pos()[0]), abs(-box_point1.y+600-pygame.mouse.get_pos()[1])]
                pygame.draw.rect(screen, [0, 0, 255], [box_point1[0], -box_point1[1]+600, diff[0], diff[1]], 0)
            elif box_point1.x < pygame.mouse.get_pos()[0] and -box_point1.y+600 > pygame.mouse.get_pos()[1]:
                diff = [abs(box_point1.x-pygame.mouse.get_pos()[0]), abs(-box_point1.y+600-pygame.mouse.get_pos()[1])]
                pygame.draw.rect(screen, [0, 0, 255], [box_point1[0], -box_point1[1]+600-diff[1], diff[0], diff[1]], 0)
            elif box_point1.x > pygame.mouse.get_pos()[0] and -box_point1.y+600 < pygame.mouse.get_pos()[1]:
                diff = [abs(box_point1.x-pygame.mouse.get_pos()[0]), abs(-box_point1.y+600-pygame.mouse.get_pos()[1])]
                pygame.draw.rect(screen, [0, 0, 255], [box_point1[0]-diff[0], -box_point1[1]+600, diff[0], diff[1]], 0)
            elif box_point1.x > pygame.mouse.get_pos()[0] and -box_point1.y+600 > pygame.mouse.get_pos()[1]:
                diff = [abs(box_point1.x-pygame.mouse.get_pos()[0]), abs(-box_point1.y+600-pygame.mouse.get_pos()[1])]
                pygame.draw.rect(screen, [0, 0, 255], [box_point1[0]-diff[0], -box_point1[1]+600-diff[1], diff[0], diff[1]], 0)
        
        tmp_points=[]
        for point in store.poly_points:
            tmp_points.append([point[0],flipy(point[1])]) 
        
        if len(store.poly_points)>=3:
            pygame.draw.polygon(screen, [0,255,0], tmp_points, 0)
        else:
            if len(store.poly_points)==2:
                print tmp_points
                pygame.draw.line(screen, [0,255,0], tmp_points[0], tmp_points[1], 1)
        for spring in self.springs:
            pv1 = spring.a.position + spring.anchr1
            pv2 = spring.b.position + spring.anchr2
            pv1.x+=self.campos[0]
            pv1.y+=self.campos[1]
            pv2.x+=self.campos[0]
            pv2.y+=self.campos[1]
            p1 = flipyv(pv1)
            p2 = flipyv(pv2)
            pygame.draw.line(screen, [0, 255, 0], p1, p2, 2)
            
        for rod in self.rods:
            pv1 = rod.a.position + rod.anchr1
            pv2 = rod.b.position + rod.anchr2
            pv1.x+=self.campos[0]
            pv1.y+=self.campos[1]
            pv2.x+=self.campos[0]
            pv2.y+=self.campos[1]
            p1 = flipyv(pv1)
            p2 = flipyv(pv2)
            pygame.draw.line(screen, [100, 100, 100], p1, p2, 2)

        if spring_point1 is not None:
            pv1= [spring_point1[0]+springobject1.body.position.x,spring_point1[1]+springobject1.body.position.y]
            pv1[1]=-pv1[1]+600
            pygame.draw.line(screen, [0, 0, 255], pv1, pygame.mouse.get_pos(), 1)

        if mouse_grab_spring is not None:
            pygame.draw.line(screen, [255, 255, 0], flipyv(mouse_grab_spring.anchr2+mouse_grab_spring.b.position+self.campos), pygame.mouse.get_pos(), 1)

        for pin in self.pins:
            pos=[pin.real_pos[0], -pin.real_pos[1]+600]
            pygame.draw.circle(screen, [200,200,200], pos, 5, 0)
            
        for motor in self.motors:
            pygame.draw.circle(screen, [0,0,0], flipyv(motor.b.position), 3, 0)

        if self.delete_down:
            for item in store.polys:
                query = item.point_query(flipyv(pymunk.Vec2d(pygame.mouse.get_pos()[0]-3, pygame.mouse.get_pos()[1]-3)))
                print query
                if query:
                    print "KILL"
                    store.remove_all_constraints(item)
                    space.remove(item, item.body)
                    store.polys.remove(item)
                    #del item

            for item in store.lines:
                query = item.point_query(flipyv(pymunk.Vec2d(pygame.mouse.get_pos()[0]-3, pygame.mouse.get_pos()[1]-3)))
                print query
                if query:
                    print "KILL"
                    store.remove_all_constraints(item)
                    space.remove(item, item.body)
                    store.all.remove(item)
                    store.polys.remove(item)
            #        #del item

        self.clean_up(self.balls)
        self.clean_up(self.polys)

        self.update_ingame_menu()

    def rotate_marble(self, image):
        marbleimage=pygame.image.load("resources/images/marbles/"+image+".png")
        for i in range(0, 361):
            self.marbleim[i]=pygame.transform.rotate(marbleimage, i)

    def check_bounds(self, pos, rect):
        if pos[0]>rect[0]:
            if pos[0]<rect[0]+rect[2]:
                if pos[1]>rect[1]:
                    if pos[1]<rect[1]+rect[3]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def save_level(self, name):
        try:
            os.remove("levels/"+name+".marb")
        except:
            pass
        all_list=[]
        for item in self.all:
            if type(item) == pymunk.Segment:
                body = item.body
                pv1 = body.position + item.a.rotated(body.angle)
                pv2 = body.position + item.b.rotated(body.angle)
                p1 = pv1.x, pv1.y
                p2 = pv2.x, pv2.y
                all_list.append(["Line", p1, p2, item.radius])

            if type(item) == pymunk.Circle:
                motorlist = []
                for motor in store.motors:
                    if motor.a == item.body or motor.b == item.body:
                        motorlist.append(motor.rate)
                all_list.append(["Circle", [item.body.position.x, item.body.position.y], motorlist, item.radius])
                
            if type(item) == pymunk.Poly:
                print "Poly"
                motorlist=[]
                pointlist=item.get_points()
                newlist=[]
                for motor in store.motors:
                    if motor.a == item.body or motor.b == item.body:
                        motorlist.append(motor.rate)
                for duo in pointlist:
                    newlist.append([int(duo.x), int(duo.y)])
                all_list.append(["Poly", [item.body.position.x, item.body.position.y], newlist, item.body.moment, motorlist])
        
        for spring in self.springs:
            all_list.append(["Spring", [spring.anchr1.x+spring.a.position.x, spring.anchr1.y+spring.a.position.y], [spring.anchr2.x+spring.b.position.x, spring.anchr2.y+spring.b.position.y]])


        for line in all_list:
            for sep in line:
                print sep
            print
        dumpingfile = open("levels/"+name+".marb", "w")
        dumpingfile.close()
        pickle.dump(all_list, open("levels/"+name+".marb", "w"))

    def load_level(self, name):
        while len(store.balls) > 0:
            for ball in store.balls:
                store.remove_all_constraints(ball)
                space.remove(ball, ball.body)
                store.all.remove(ball)
                store.balls.remove(ball)
        while len(store.polys) > 0:
            for poly in store.polys:
                store.remove_all_constraints(poly)
                space.remove(poly, poly.body)
                store.polys.remove(poly)
        while len(store.motors) > 0:
            for motor in store.motors:
                space.remove(motor)
                store.motors.remove(motor)
        while len(store.springs) > 0:
            for spring in store.springs:
                space.remove(spring)
                store.springs.remove(spring)
        while len(store.lines) > 0:
            for line in store.lines:
                space.remove(line)
                store.all.remove(line)
                store.lines.remove(line)
        self.campos=[0,0]
        try:
            openfile=open("levels/"+name+".marb","r")
            full_items=pickle.load(openfile)
            print full_items
            for line in full_items:
                if line[0] == "Line":
                    print "Line"
                    body = pymunk.Body(pymunk.inf, pymunk.inf)
                    shape = pymunk.Segment(body, line[1], line[2], line[3])
                    shape.friction = 0.99
                    shape.kill_me = False
                    space.add(shape)
                    store.lines.append(shape)
                    store.all.append(shape)
                elif line[0] == "Circle":
                    print "Circle"
                    p = pymunk.Vec2d(line[1])
                    body = pymunk.Body(5, 100)
                    body.position = p
                    shape = pymunk.Circle(body, line[3], (0,0))
                    shape.friction = 0.5
                    shape.kill_me = False
                    space.add(body, shape)
                    for motor in line[2]:
                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                        rotation_body.position = shape.body.position
                        space.add(rotation_body)
                        #item.friction = 1
                        motor=pymunk.SimpleMotor(rotation_body, shape.body, motor)
                        space.add(motor)
                        store.motors.append(motor)
                    store.balls.append(shape)
                    store.all.append(shape)
                elif line[0] == "Poly":
                    print "Poly"
                    print pymunk.util.calc_center(line[2])
                    poly = store.create_load_poly(line[2], 5.0, line[1], line[3])
                    poly.body.reset_forces()
                    for motor in line[4]:
                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                        rotation_body.position = poly.body.position
                        space.add(rotation_body)
                        #item.friction = 1
                        motor=pymunk.SimpleMotor(rotation_body, poly.body, motor)
                        space.add(motor)
                        store.motors.append(motor)
                    store.polys.append(poly)
                    store.all.append(poly)
                
            for spring in full_items:
                if spring[0] == "Spring":
                    print
                    print "Spring. Data Line:"
                    print spring
                    print
                    for item in store.all:
                        if item.point_query(spring[1]):
                            o1=item
                            print o1
                    for item in store.all:
                        if item.point_query(spring[2]):
                            o2=item
                            print o2
                    rest_length=o1.body.position.get_distance(o2.body.position)
                    newspring=pymunk.DampedSpring(o1.body, o2.body, o1.body.world_to_local(spring[1]), o2.body.world_to_local(spring[2]), rest_length, 1000, 1)
                    newspring.bias_coef=1
                    store.springs.append(newspring)
                    space.add(newspring)
                    print
                    print
        except:
            print "File reading error!"

    def create_box(self, pos, sizex, sizey, mass = 5.0):
        print pos
        pos=[pos[0], pos[1]]
        #pos[0]-=self.campos[0]
        #pos[1]-=self.campos[1]
        box_points = map(pymunk.Vec2d, [(-sizex/2, -sizey/2), (-sizex/2, sizey/2), (sizex/2,sizey/2), (sizex/2, -sizey/2)])
        return self.create_poly(box_points, mass = mass, pos = pos)

    def create_poly(self, points, mass = 5.0, pos = (0,0), moment = None):
        if moment is None:
            moment = pymunk.moment_for_poly(mass,points, pymunk.Vec2d(0,0))
        #moment = 50000
        body = pymunk.Body(mass, moment)
        pos=[pos[0], pos[1]]
        pos[0]-=self.campos[0]
        pos[1]-=self.campos[1]
        #body.position = body.world_to_local(pymunk.Vec2d([pymunk.util.calc_center(points)[0]+pos[0],pymunk.util.calc_center(points)[1]+pos[1]]))
        body.position = pymunk.Vec2d([pos[0],pos[1]])

        shape = pymunk.Poly(body, points, pymunk.Vec2d(0,0))
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_DEFAULT
        shape.kill_me = False
        space.add(body, shape)
        return shape
    
    def create_diff_poly(self, points, mass, pos):
        points=pymunk.util.convex_hull(points)
        body = pymunk.Body(mass, 100000)#pymunk.moment_for_poly(mass, points, pymunk.Vec2d(pos[0],pos[1])))
        pos=[pos[0], pos[1]]
        pos[0]-=self.campos[0]
        pos[1]-=self.campos[1]
        #body.position = body.world_to_local(pymunk.Vec2d([pymunk.util.calc_center(points)[0]+pos[0],pymunk.util.calc_center(points)[1]+pos[1]]))
        body.position = pymunk.Vec2d(pos)
        #body.position.y+=400
        offset_value=pymunk.util.calc_center(points)

        shape = pymunk.Poly(body, points, pymunk.Vec2d(-offset_value[0], -offset_value[1]))
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_DEFAULT
        shape.kill_me = False
        space.add(body, shape)
        return shape
    
    def create_load_poly(self, points, mass = 5.0, pos = (0,0), moment = None):
        box_points = map(pymunk.Vec2d, points)
        if moment is None:
            moment = pymunk.moment_for_poly(mass, points, pymunk.Vec2d(0,0))
        #moment = 50000
        body = pymunk.Body(mass, moment)
        body.position = pymunk.Vec2d(pos)
        offset_value=pymunk.util.calc_center(box_points)
        shape = pymunk.Poly(body, box_points, pymunk.Vec2d(-offset_value[0], -offset_value[1]))
        #pymunk.Poly(
        #shape.body.position = body.world_to_local(pymunk.Vec2d(pos))
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_DEFAULT
        shape.kill_me = False
        space.add(body, shape)
        return shape

    def draw_poly(self, poly):
        body = poly.body
        ps = poly.get_points()
        
        for point in ps:
            point.x+=self.campos[0]
            point.y+=self.campos[1]
        ps.append(ps[0])
        ps = map(flipyv, ps)
        if poly.collision_type==COLLTYPE_FIRE:
            color=[0,0,0]
        else:
            color=[255, 0,0]
        color2=[255, 255,0]
        #pygame.draw.lines(screen, color, False, ps)
        pygame.draw.polygon(screen, color, ps, 0)
        pygame.draw.polygon(screen, color2, ps, 1)
        if poly.collision_type==COLLTYPE_FIRE:
            p_basic=pymunk.util.calc_center(ps)
            #dist = int(math.sqrt((ps[1][0]-ps[2][0])**2+(ps[1][1]-ps[2][1])**2))
            #dist = int(abs(ps[1][0]-ps[2][0])/2)
            #print
            #print
            #print
            #print dist
            otherdist = int(math.sqrt((ps[2][0]-ps[3][0])**2+(ps[2][1]-ps[3][1])**2))
            vert = int(poly.burn_level/15)+otherdist
            poly.burn_level+=3
            if poly.burn_level >= 75:
                poly.burn_level = 0

            #print otherdist
            #img = pygame.transform.rotate(store.fireimgsequence[int(dist/2)][poly.burn_level/15], poly.body.angle*57.3248408)
            #screen.blit(img, [p_basic[0]-int(dist/2), p_basic[1]])
            #screen.blit(img, ps[0])

            #pygame.draw.polygon(screen, [255, 0, 0], [ps[1], [p_basic[0]+random.randint(-20, 20), p_basic[1]-otherdist+random.randint(-20, 20)], ps[2]], 0)
            #pygame.draw.polygon(screen, [205, 140, 0], [ps[1], [p_basic[0]-15+random.randint(-5, 5), p_basic[1]-otherdist+random.randint(-10, 10)], ps[2]], 0)
            #pygame.draw.polygon(screen, [255, 255, 0], [ps[1], [p_basic[0]-15+random.randint(-5, 5), p_basic[1]-otherdist+random.randint(-10, 10)], ps[2]], 0)
            pygame.draw.polygon(screen, [255, 0, 0], [ps[1], [p_basic[0]+random.randint(-10, 10), p_basic[1]-vert], ps[2]], 0)
        pygame.draw.circle(screen, [0,0,0], flipyv(body.position),2,0)

        if poly.collision_type==COLLTYPE_CHAR:
            p_basic=pymunk.util.calc_center(ps)
            pygame.draw.circle(screen, [255, 255, 0], p_basic, 5, 0)

    def remove_all_constraints(self, item):
        for spring in store.springs:
            #print spring.a
            #print item.body
            #print 
            #print spring.b
            #print item.body
            #print
            
            if str(spring.a)==str(item.body):
                space.remove(spring)
                store.springs.remove(spring)
                #print "I was A"
                #print
            if str(spring.b)==str(item.body):
                space.remove(spring)
                store.springs.remove(spring)
                #print "I was B"
                #print
            #print "--------"

        for motor in store.motors:
            if motor.a==item.body or motor.b==item.body:
                try:
                    space.remove(motor)
                    store.motors.remove(motor)
                except:
                    pass
                    
        for pin in store.pins:
            if pin.a==item.body or pin.b==item.body:
                    space.remove(pin)
                    store.pins.remove(pin)
                #except:
                #    pass

    def draw_gravity_menu(self):
        pygame.draw.rect(screen, [0,0,0], [self.gravityposition[0]+945, self.gravityposition[1]+self.mh-10, 6, 6], 3)
        pygame.draw.rect(screen, [0,0,0], [945, self.mh+5, 50, 50], 3)
        pygame.draw.line(screen, [0,0,0], [945, self.mh+30],[995, self.mh+30], 2)
        pygame.draw.line(screen, [0,0,0], [970, self.mh+5],[970, self.mh+55], 2)
        #Down button-----------------
        pygame.draw.rect(screen, [0,0,0], [895, self.mh+30, 44, 23], 3)
        screen.blit(resetdownimg, [900, self.mh+32])
        #----------------------------
        #Up button-------------------
        pygame.draw.rect(screen, [0,0,0], [895, self.mh+7, 44, 23], 3)
        screen.blit(resetupimg, [910, self.mh+10])
        #----------------------------
        #None button-------------------
        pygame.draw.rect(screen, [0,0,0], [851, self.mh+30, 44, 23], 3)
        screen.blit(resetnoneimg, [856, self.mh+32])
        #----------------------------

    def draw_tool_menu(self):
        screen.blit(smallfont.render(self.drop_item, 1, [0,0,0]), [880, self.mh+2])
        if store.drop_item=="square":
            #---Square Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Square Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Side Length: "+str(self.square_size), 1, [0,0,0]), [818, self.mh+40])
        if store.drop_item=="ball":
            #---Ball Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Ball Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Radius: "+str(self.circle_size), 1, [0,0,0]), [850, self.mh+21])
        if store.drop_item=="draw":
            #---Draw Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Draw Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Delay: "+str(self.draw_delay), 1, [0,0,0]), [850, self.mh+21])
        if store.drop_item=="explosion":
            #---Explosion Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Explosion Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Power: "+str(self.explosion_power), 1, [0,0,0]), [850, self.mh+21])

        if store.drop_item=="motor":
            #---Motor Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Motor Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Speed: "+str(self.motor_rate), 1, [0,0,0]), [850, self.mh+21])
        
        if store.drop_item=="line":
            #---Line Down button-----------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+30, 44, 23], 3)
            screen.blit(resetdownimg, [955, self.mh+32])
            #----------------------------
            #---Line Up button-------------------
            pygame.draw.rect(screen, [0,0,0], [950, self.mh+7, 44, 23], 3)
            screen.blit(resetupimg, [965, self.mh+10])
            #----------------------------
            screen.blit(font.render("Width: "+str(self.line_width), 1, [0,0,0]), [850, self.mh+21])

def flipy(y):
    return -y+600

def flipyv(v):
    return int(v.x), int(-v.y+600)

def mouse_coll_func(space, arbiter):
    try:
        s1,s2 = arbiter.shapes
        if type(s1) == pymunk.Segment:
            if store.ddown:
                try:
                    s1.kill_me = True
                except:
                    pass
        if type(s2) == pymunk.Circle:
            if store.ddown:
                try:
                    s2.kill_me = True
                except:
                    pass
        if type(s1) == pymunk.Poly:
            if store.ddown:
                try:
                    s1.kill_me = True
                    print "Killing A Poly"
                except:
                    pass
    except:
        print "Collisision Handling Error"
        space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_DEFAULT, mouse_coll_func, None, None, None)
        print "Fixed"
    return False

def explosion_coll_func(space, arbiter):
    s1,s2 = arbiter.shapes
    if type(s1) == pymunk.Poly:
        if s1.body.position.x<s2.body.position.x:
            if s1.body.position.y>s2.body.position.y:
                s1.body.apply_impulse([-store.explosion_power+random.randint(-15,15), 2*store.explosion_power+random.randint(-15,15)], [0,0])
            if s1.body.position.y<s2.body.position.y:
                s1.body.apply_impulse([-store.explosion_power+random.randint(-15,15), -2*store.explosion_power+random.randint(-15,15)], [0,0])
        else:
            if s1.body.position.y>s2.body.position.y:
                s1.body.apply_impulse([store.explosion_power+random.randint(-15,15), 2*store.explosion_power+random.randint(-15,15)], [0,0])
            if s1.body.position.y<s2.body.position.y:
                s1.body.apply_impulse([store.explosion_power+random.randint(-15,15), -2*store.explosion_power+random.randint(-15,15)], [0,0])

    if type(s1) == pymunk.Circle:
        if s1.body.position.x<s2.body.position.x:
            if s1.body.position.y>s2.body.position.y:
                s1.body.apply_impulse([-store.explosion_power+random.randint(-15,15), 2*store.explosion_power+random.randint(-15,15)], [0,0])
            if s1.body.position.y<s2.body.position.y:
                s1.body.apply_impulse([-store.explosion_power+random.randint(-15,15), -2*store.explosion_power+random.randint(-15,15)], [0,0])
        else:
            if s1.body.position.y>s2.body.position.y:
                s1.body.apply_impulse([store.explosion_power+random.randint(-15,15), 2*store.explosion_power+random.randint(-15,15)], [0,0])
            if s1.body.position.y<s2.body.position.y:
                s1.body.apply_impulse([store.explosion_power+random.randint(-15,15), -2*store.explosion_power+random.randint(-15,15)], [0,0])
    return False

def char_coll_func(space, arbiter):
    s1,s2 = arbiter.shapes
    if type(s1) == pymunk.Segment:
        store.char_jumped=False
    if type(s1) == pymunk.Circle:
        store.char_jumped=False
    if type(s1) == pymunk.Poly:
        store.char_jumped=False
    return True

def fire_coll_func(space, arbiter):
    s1,s2 = arbiter.shapes
    if type(s1)!=pymunk.Segment and type(s2)!=pymunk.Segment:
        s1.collision_type=COLLTYPE_FIRE
        s2.collision_type=COLLTYPE_FIRE
        try:
            s1.burn_level
        except:
            s1.burn_level=0
        try:
            s2.burn_level
        except:
            s2.burn_level=0
    return True

store=storer()

pygame.init()
pygame.display.set_icon(pygame.image.load("resources/images/icon.png"))
#screen = pygame.display.set_mode([1000, 660], pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

menubar=pygame.image.load("resources/images/menubar.png")
menuback=pygame.image.load("resources/images/menuback.png")
explosionimg=pygame.image.load("resources/images/explosion.png")
fireimg=pygame.image.load("resources/images/fire.png")

pymunk.init_pymunk()
space = pymunk.Space(elastic_iterations=0)
space.gravity = pymunk.Vec2d(0.0, -900.0)

mouse_body = pymunk.Body(pymunk.inf, pymunk.inf)
mouse_shape = pymunk.Circle(mouse_body, 3, pymunk.Vec2d(0,0))
mouse_shape.collision_type = COLLTYPE_MOUSE
space.add(mouse_shape)

space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_DEFAULT, None, mouse_coll_func, None, None)
space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_FIRE, None, mouse_coll_func, None, None)
space.add_collision_handler(COLLTYPE_EXPLOSION, COLLTYPE_DEFAULT, None, explosion_coll_func, None, None)
space.add_collision_handler(COLLTYPE_EXPLOSION, COLLTYPE_FIRE, None, explosion_coll_func, None, None)
space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_CHAR, None, mouse_coll_func, None, None)
space.add_collision_handler(COLLTYPE_EXPLOSION, COLLTYPE_CHAR, None, explosion_coll_func, None, None)
space.add_collision_handler(COLLTYPE_CHAR, COLLTYPE_DEFAULT, None, char_coll_func, None, None)
space.add_collision_handler(COLLTYPE_FIRE, COLLTYPE_DEFAULT, fire_coll_func, fire_coll_func, None, None)

line_point1 = None
spring_point1=None
rod_point1 = None
rod_point1=None
box_point1=None
mouse_grab_spring=None
run_physics = True

pygame.key.set_repeat(50, 100)
pygame.display.set_caption("Block Builder")
smallfont = pygame.font.Font("resources/12tonsushi.ttf", 12)
font = pygame.font.Font("resources/12tonsushi.ttf", 18)
aboutfont = pygame.font.Font("resources/12tonsushi.ttf", 28)
bigfont = pygame.font.Font("resources/12tonsushi.ttf", 75)
titlefont = pygame.font.Font("resources/12tonsushi.ttf", 90)
midfont = pygame.font.Font("resources/12tonsushi.ttf", 35)
title = titlefont.render("Block Builder", 1, [85,80,250])
playbuttonimg=bigfont.render("Play", 1, [0,0,0])
aboutbuttonimg=bigfont.render("About", 1, [0,0,0])
settingsbuttonimg=midfont.render("Settings", 1, [0,0,0])
loadbuttonimg=bigfont.render("Load", 1, [0,0,0])
startbuttonimg=bigfont.render("Start", 1, [0,0,0])
exitbuttonimg=bigfont.render("Exit", 1, [0,0,0])
boxdropimg=font.render("Box", 1, [0,0,0])
squaredropimg=font.render("Square", 1, [0,0,0])
characterdropimg=font.render("Character", 1, [0,0,0])
springdropimg=font.render("Spring", 1, [0,0,0])
linedropimg=font.render("Line", 1, [0,0,0])
drawdropimg=font.render("Draw", 1, [0,0,0])
grabdropimg=font.render("Grab", 1, [0,0,0])
balldropimg=font.render("Ball", 1, [0,0,0])
pindropimg=font.render("Pin", 1, [0,0,0])
polydropimg=font.render("Poly", 1, [0,0,0])
roddropimg=font.render("Rod", 1, [0,0,0])
explosiondropimg=font.render("Explosion", 1, [0,0,0])
firedropimg=font.render("Fire", 1, [0,0,0])
motordropimg=font.render("Motor", 1, [0,0,0])
cardropimg=font.render("Car", 1, [0,0,0])
cancelimg=font.render("Cancel", 1, [0,0,0])
missiledropimg=font.render("Missile", 1, [0,0,0])
resetdownimg=font.render("Down", 1, [0,0,0])
resetupimg=font.render("Up", 1, [0,0,0])
resetnoneimg=font.render("None", 1, [0,0,0])
saveimg=font.render("Save", 1, [0,0,0])
clearimg=font.render("Clear", 1, [0,0,0])
clearmoveablesimg=font.render("Clear Moveables", 1, [0,0,0])
loadimg=font.render("Load", 1, [0,0,0])
menuimg=font.render("Menu", 1, [0,0,0])
nextimg=font.render("Next", 1, [0,0,0])
copyimg=font.render("Copy", 1, [0,0,0])
previousimg=font.render("Previous", 1, [0,0,0])
gravityimg=font.render("Gravity", 1, [0,0,0])
toolimg=font.render("Tool", 1, [0,0,0])
deleteimg=font.render("Delete", 1, [0,0,0])

#---About Text
abouttrans = pygame.surface.Surface([1000, 660], pygame.SRCALPHA)
abouttrans.fill([85, 80, 250, 200])

line_1 = aboutfont.render("Block Builder by Eggplant Animation", 1, [0,0,0])
line_2 = aboutfont.render(store.version, 1, [0,0,0])
line_3 = aboutfont.render("-----Credits-----", 1, [0,0,0])
line_4 = aboutfont.render("Programmed with python version 2.5.4", 1, [0,0,0])
line_5 = aboutfont.render("Made with pygame version 1.9.1", 1, [0,0,0])
line_6 = aboutfont.render("Uses pymunk 1.0.0, which is based on chipmunk version 5.x.xr428", 1, [0,0,0])
line_7 = aboutfont.render("Font is 12TonSushi", 1, [0,0,0])
line_8 = aboutfont.render("Programming: pie", 1, [0,0,0])
line_9 = aboutfont.render("-----Help-----", 1, [0,0,0])
line_10 = aboutfont.render("None!", 1, [0,0,0])
#----------

trans = pygame.surface.Surface([1000, 660], pygame.SRCALPHA)
trans.fill([85, 80, 250, 1])

store.rotate_marble("one_marble")

screen = pygame.display.set_mode([1000, 660], pygame.RESIZABLE)

try:
    psyco.full()
except:
    print "No psyco. This will run slower!"

for i in range(1, 220):
    store.explodeimgsequence.append(pygame.transform.scale(explosionimg, (2*i, 2*i)))

for x in range(0, 1000):
    store.fireimgsequence.append([])

for x in range(1, 500):
    for y in range(1, 6):
        store.fireimgsequence[x].append(pygame.transform.scale(fireimg, (2*x, y*10)))

#screen.blit(menuback, [0,0])

if "-c" in sys.argv:
    test_the_cmd=cmdtest.eggcmd()
    test_the_cmd.cmdloop()

if "-e" in sys.argv:
    pass

#test = ask.ask([0,0], 15, font, 5)

while running:
    pygame.draw.line(screen, [0,0,0], store.old_pos, pygame.mouse.get_pos(), store.line_width)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type==pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]==True:
                if store.drop_item=="draw":
                    print "out"
                    store.move_frame+=1
                    if store.move_frame==store.draw_delay:
                        body = pymunk.Body(pymunk.inf, pymunk.inf)
                        shape= pymunk.Segment(body, store.old_pos, [event.pos[0], flipy(event.pos[1])], store.line_width)
                        store.old_pos=[event.pos[0], flipy(event.pos[1])]
                        shape.friction = 0.99
                        shape.kill_me = False
                        space.add(shape)
                        store.lines.append(shape)
                        store.all.append(shape)
                        store.move_frame=0
                    pygame.draw.line(screen, [0,0,0], store.old_pos, pygame.mouse.get_pos(), store.line_width)

        elif event.type==pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            store.mh = screen.get_height()-85
            store.menux = screen.get_width()
            store.menuy = screen.get_height()
            trans = pygame.surface.Surface([screen.get_width(), screen.get_height()], pygame.SRCALPHA)
            abouttrans = pygame.surface.Surface([screen.get_width(), screen.get_height()], pygame.SRCALPHA)
            abouttrans.fill([85, 80, 250, 200])
            trans.fill([85, 80, 250, 1])

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print "making poly, brb"
                def area(verts):
                    accum = 0.0
                    for i in range(len(verts)):
                        j = (i + 1) % len(verts)
                        accum += verts[j][0] * verts[i][1] - verts[i][0] * verts[j][1]
                    return accum / 2
                def centroid(verts):
                    x, y = 0, 0
                    for i in range(len(verts)):
                        j = (i + 1) % len(verts)
                        factor = verts[j][0] * verts[i][1] - verts[i][0] * verts[j][1]
                        x += (verts[i][0] + verts[j][0]) * factor
                        y += (verts[i][1] + verts[j][1]) * factor
                    polyarea = area(verts)
                    x /= 6 * polyarea
                    y /= 6 * polyarea
                    return (x, y)
                x_total=0
                for point in store.poly_points:
                    x_total+=point[0]
                y_total=0
                for point in store.poly_points:
                    y_total+=point[1]
                x_total=x_total/len(store.poly_points)
                y_total=y_total/len(store.poly_points)
                #cen_pos=pymunk.util.calc_center(store.poly_points)
                cen_pos=centroid(store.poly_points)
                #cen_pos[0]+= cen_pos[0]*0.5
                #cen_pos[1]+= cen_pos[1]*0.5
                print cen_pos
                poly=store.create_diff_poly(store.poly_points, 5.0, cen_pos)
                store.polys.append(poly)
                store.all.append(poly)
                store.poly_points=[]
                
            if event.key == pygame.K_q:
                if pygame.key.get_mods() & pygame.KMOD_META:
                	print "mac quit"
                	running = False
                
            if event.key == pygame.K_o:
                if pygame.key.get_mods() & pygame.KMOD_META:
                	print "mac load"
                	store.state="load"
                
            if event.key == pygame.K_s:
                if pygame.key.get_mods() & pygame.KMOD_META:
                	print "mac save"
                	store.state="save"
                
            if store.state == "save":
                if pygame.key.name(event.key) in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    if font.size(store.save_name)[0]<384:
                        store.save_name += pygame.key.name(event.key)
                else:
                    if pygame.key.name(event.key) == "backspace":
                        store.save_name = store.save_name[:-1]
                    elif pygame.key.name(event.key) == "space":
                        store.save_name += " "
                    elif pygame.key.name(event.key) == "return":
                        store.save_level(store.save_name)
                        store.state = "game"
                    else:
                        print pygame.key.name(event.key)

            if event.key in store.numbers:
                if store.state == "game" and store.menu_state == "tool":
                    if store.drop_item == "ball":
                        if store.numbers[event.key]!="-":
                            if len(str(store.circle_size)) < 4:
                                store.circle_size*=10
                                store.circle_size+=store.numbers[event.key]

                    if store.drop_item == "square":
                        if store.numbers[event.key]!="-":
                            if len(str(store.square_size)) < 4:
                                store.square_size*=10
                                store.square_size+=store.numbers[event.key]
                            
                    if store.drop_item == "explosion":
                        if store.numbers[event.key]!="-":
                            if len(str(store.explosion_power)) < 4:
                                store.explosion_power*=10
                                store.explosion_power+=store.numbers[event.key]
                                
                    if store.drop_item == "line":
                        if store.numbers[event.key]!="-":
                            if len(str(store.line_width)) < 4:
                                store.line_width*=10
                                store.line_width+=store.numbers[event.key]
                                
                    if store.drop_item == "draw":
                        if store.numbers[event.key]!="-":
                            if len(str(store.draw_delay)) < 4:
                                store.draw_delay*=10
                                store.draw_delay+=store.numbers[event.key]

                    if store.drop_item == "motor":
                        if store.numbers[event.key]!="-":
                            if len(str(store.motor_rate)) < 4:
                                store.motor_rate*=10
                                store.motor_rate+=store.numbers[event.key]
                        else:
                            store.motor_rate=-store.motor_rate

            if store.state=="game":
                if event.key == pygame.K_BACKSPACE:
                    if store.menu_state == "tool":
                        if store.drop_item == "ball":
                            store.circle_size=int(store.circle_size/10)

                        if store.drop_item == "square":
                            store.square_size=int(store.square_size/10)

                        if store.drop_item == "explosion":
                            store.explosion_power=int(store.explosion_power/10)

                        if store.drop_item == "motor":
                            store.motor_rate=int(store.motor_rate/10)
                            
                        if store.drop_item == "line":
                            store.line_width=int(store.line_width/10)
                            
                        if store.drop_item == "draw":
                            store.draw_delay=int(store.draw_delay/10)

                if  event.key == pygame.K_SPACE:
                    run_physics = not run_physics
                    
                if event.key == pygame.K_o:
                    for spring in store.springs:
                        print spring.a
                        print spring.b
                        print

                #if event.key == pygame.K_d:
                    #store.ddown = True

                elif event.key == pygame.K_f:
                    screen=pygame.display.set_mode(pygame.display.list_modes()[0], pygame.FULLSCREEN)
                    store.mh=pygame.display.list_modes()[0][1]-85

                elif event.key == pygame.K_ESCAPE:
                    screen=pygame.display.set_mode([1000, 660], pygame.RESIZABLE)
                    store.mh=575
                    
                elif event.key == pygame.K_0:
                    for i in range(0,1000):
                        p = pygame.mouse.get_pos()[0]-store.campos[0], flipy(pygame.mouse.get_pos()[1])-store.campos[1]
                        body = pymunk.Body(5, 100)
                        body.position = p
                        shape = pymunk.Circle(body, 3, (0,0))
                        shape.friction = 0.5
                        shape.kill_me = False
                        space.add(body, shape)
                        store.balls.append(shape)
                        store.all.append(shape)

                elif event.key == pygame.K_w:
                    store.campos[1]-=10
                elif event.key == pygame.K_s:
                    store.campos[1]+=10
                elif event.key == pygame.K_d:
                    store.campos[0]-=10
                elif event.key == pygame.K_a:
                    store.campos[0]+=10

                elif event.key == pygame.K_LEFT:
                    print "Left!"
                    try:
                        store.char.body.apply_impulse([-300,20])
                        print "Moved Left!"
                    except:
                        print "Failed Moving Left!"

                elif event.key == pygame.K_RIGHT:
                    print "Right"
                    try:
                        store.char.body.apply_impulse([300,20])
                        print "Moved Right!"
                    except:
                        print "Failed Moving Right!"

                elif event.key == pygame.K_UP:
                    try:
                        if store.char_jumped==False:
                            store.char.body.apply_impulse([0,1500])
                            store.char_jumped=True
                    except:
                        pass

                #elif event.key == pygame.K_m:
                    #rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                    #rotation_body.position = store.balls[0].body.position
                    #rotation_shape = pymunk.Circle(rotation_body, 2)
                    #space.add(rotation_body)
                    #pivot=pymunk.PinJoint(rotation_body, store.balls[0].body, [0,0], [0,0])
                    #space.add(pivot, rotation_shape)
                
                elif event.key == pygame.K_EQUALS:
                    store.speed -= 5
                    print store.speed
                    
                elif event.key == pygame.K_MINUS:
                    store.speed += 5
                    print store.speed

        #elif event.type == pygame.KEYUP:
            #if store.state=="game":
                #if event.key == pygame.K_d:
                    #store.ddown=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if store.state=="menu":
                if store.check_bounds(pygame.mouse.get_pos(), [5, 5, 191, 65]):
                    store.menu_state="start"
                
                if store.check_bounds(pygame.mouse.get_pos(), [5, 100, 140, 65]):
                    store.state="game"
                
                if store.check_bounds(pygame.mouse.get_pos(), [5, 195, 140, 65]):
                    store.menu_state="load"
                    store.find_all()    
                    
                if store.check_bounds(pygame.mouse.get_pos(), [5, 590, 140, 65]):
                    running=False

                if store.check_bounds(pygame.mouse.get_pos(), [5, 400, 190, 65]):
                    store.menu_state = "about"
                   
                if store.check_bounds(pygame.mouse.get_pos(), [5, 495, 140, 65]):
                    store.menu_state = "settings" 
                
                    
                if store.menu_state=="load":
                    if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-200, 95, 400, 405]):
                    #print "box"
                        store.selection = int((pygame.mouse.get_pos()[1]-195)/20)
                        try:
                            store.load_name=store.files[store.current_page][store.selection]
                        except:
                            store.load_name = ""
                            store.selection = None
                        
                    if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+103, 606, 44, 27]):
                        store.load_level(store.load_name)
                        store.state = "game"
                        
                    if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+155, 506, 45, 27]):
                        if store.current_page < len(store.files)-1:
                            store.selection = None
                            store.current_page += 1
                        
                    if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-200, 506, 75, 27]):
                        if store.current_page !=0:
                            store.selection = None
                            store.current_page -= 1

                        
            elif store.state == "save":
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+3, 506, 44, 27]):
                    store.save_level(store.save_name)
                    store.state = "game"
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-61, 506, 60, 27]):
                    store.state = "game"
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+155, 506, 45, 27]):
                    if store.current_page < len(store.files)-1:
                        store.current_page += 1
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-200, 506, 75, 27]):
                    if store.current_page !=0:
                        store.current_page -= 1
                                        
            elif store.state == "load":
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-200, 95, 400, 405]):
                    #print "box"
                    store.selection = int((pygame.mouse.get_pos()[1]-95)/20)
                    try:
                        store.load_name=store.files[store.current_page][store.selection]
                    except:
                        store.load_name = ""
                        store.selection = None

                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+3, 506, 44, 27]):
                    store.load_level(store.load_name)
                    store.state = "game"
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-61, 506, 60, 27]):
                    store.state = "game"
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)+155, 506, 45, 27]):
                    if store.current_page < len(store.files)-1:
                        store.selection = None
                        store.current_page += 1
                    
                if store.check_bounds(pygame.mouse.get_pos(), [(store.menux/2)-200, 506, 75, 27]):
                    if store.current_page !=0:
                        store.selection = None
                        store.current_page -= 1

            elif store.state=="game":
                if store.drop_item=="square":
                    if event.button==4:
                        store.square_size+=1
                    if event.button==5:
                        if store.square_size>1:
                            store.square_size-=1
                if store.drop_item=="explosion":
                    if event.button==4:
                        store.explosion_power+=10
                    if event.button==5:
                        if store.explosion_power>10:
                            store.explosion_power-=10
                
                if pygame.mouse.get_pos()[1]<store.mh:
                    if event.button == 1:
                        if line_point1 is None:
                            if store.drop_item == "ball":
                                p = event.pos[0]-store.campos[0], flipy(event.pos[1])-store.campos[1]
                                body = pymunk.Body(5, 100)
                                body.position = p
                                shape = pymunk.Circle(body, store.circle_size, (0,0))
                                shape.friction = 0.5
                                shape.kill_me = False
                                space.add(body, shape)
                                store.balls.append(shape)
                                store.all.append(shape)

                            if store.drop_item == "box":
                                if box_point1 is None:
                                    box_point1 = pymunk.Vec2d(event.pos[X], flipy(event.pos[Y]))
                                #p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                #store.polys.append(store.create_box(pos = p, size=20))

                            if store.drop_item == "delete":
                                print "Delete"
                                store.ddown = True
                                #for item in store.polys:
                                #    query = item.point_query(flipyv(pymunk.Vec2d(event.pos[0]-3, event.pos[1]-3)))
                                #    print query
                                #    if query:
                                #        print "KILL"
                                #        store.remove_all_constraints(item)
                                #        space.remove(item, item.body)
                                #        store.polys.remove(item)
                                #        #del item
                                #
                                #for item in store.lines:
                                #    query = item.point_query(flipyv(pymunk.Vec2d(event.pos[0]-3, event.pos[1]-3)))
                                #    print query
                                #    if query:
                                #        print "KILL"
                                #        store.remove_all_constraints(item)
                                #        space.remove(item, item.body)
                                #        store.all.remove(item)
                                #        store.polys.remove(item)
                                #        #del item

                            if store.drop_item == "square":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                new_square=store.create_box(pos = p, sizex=store.square_size, sizey=store.square_size)
                                store.polys.append(new_square)
                                store.all.append(new_square)

                            if store.drop_item == "car":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                p=[p[0], p[1]]
                                car_body=store.create_box(pos = p, sizex=50, sizey=50)
                                store.polys.append(car_body)
                                store.all.append(car_body)

                                left_body = pymunk.Body(5, 100)
                                left_body.position = pymunk.Vec2d([p[0]-30-store.campos[0], p[1]-60-store.campos[1]])
                                left_shape = pymunk.Circle(left_body, 20, (0,0))
                                left_shape.friction = 0.5
                                left_shape.kill_me = False
                                space.add(left_body, left_shape)
                                store.balls.append(left_shape)
                                store.all.append(left_shape)

                                right_body = pymunk.Body(5, 100)
                                right_body.position = pymunk.Vec2d([p[0]+30-store.campos[0], p[1]-60-store.campos[1]])
                                right_shape = pymunk.Circle(right_body, 20, (0,0))
                                right_shape.friction = 0.5
                                right_shape.kill_me = False
                                space.add(right_body, right_shape)
                                store.balls.append(right_shape)
                                store.all.append(right_shape)

                                wheel_rest_length=right_shape.body.position.get_distance(left_shape.body.position)
                                wheelspring=pymunk.DampedSpring(right_shape.body, left_shape.body, [0,0], [0,0], wheel_rest_length, 1000, 1)
                                wheelspring.bias_coef=1
                                store.springs.append(wheelspring)
                                space.add(wheelspring)

                                left_rest_length=right_shape.body.position.get_distance(left_shape.body.position)
                                leftspring=pymunk.DampedSpring(left_shape.body, car_body.body, [0,0], [0,0], left_rest_length, 1000, 1)
                                leftspring.bias_coef=1
                                store.springs.append(leftspring)
                                space.add(leftspring)

                                right_rest_length=right_shape.body.position.get_distance(left_shape.body.position)
                                rightspring=pymunk.DampedSpring(right_shape.body, car_body.body, [0,0], [0,0], right_rest_length, 1000, 1)
                                rightspring.bias_coef=1
                                store.springs.append(rightspring)
                                space.add(rightspring)
                                
                            if store.drop_item == "copy":
                                for item in store.all:
                                    new=store.create_diff_poly(item.get_points(), 5.0, [item.body.position[0]+1,item.body.position[1]])
                                    print item._hashid
                                    print new._hashid
                                    pymunk.reset_shapeid_counter()
                                    #new._hashid=289984
                                    #space.add(new)

                            if store.drop_item == "spring":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                p=[p[0], p[1]]
                                p[0]-=store.campos[0]
                                p[1]-=store.campos[1]
                                if spring_point1==None:
                                    for item in store.balls:
                                        if item.point_query(p):
                                            springobject1=item
                                            spring_point1=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    for item in store.polys:
                                        if item.point_query(p):
                                            springobject1=item
                                            spring_point1=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                else:
                                    for item in store.balls:
                                        if item.point_query(p):
                                            springobject2=item
                                            spring_point2=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    for item in store.polys:
                                        if item.point_query(p):
                                            springobject2=item
                                            spring_point2=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    try:
                                        o1=springobject1
                                        o2=springobject2
                                        rest_length=o1.body.position.get_distance(o2.body.position)
                                        newspring=pymunk.DampedSpring(o1.body, o2.body, spring_point1, spring_point2, rest_length, 1000, 1)
                                        newspring.bias_coef=1
                                        store.springs.append(newspring)
                                        space.add(newspring)
                                    except:
                                        pass
                                    springobject2=None
                                    springobject1=None
                                    spring_point1=None
                                    spring_point2=None
                                    
                            if store.drop_item == "rod":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                p=[p[0], p[1]]
                                p[0]-=store.campos[0]
                                p[1]-=store.campos[1]
                                if rod_point1==None:
                                    for item in store.balls:
                                        if item.point_query(p):
                                            rodobject1=item
                                            rod_point1=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    for item in store.polys:
                                        if item.point_query(p):
                                            rodobject1=item
                                            rod_point1=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                else:
                                    for item in store.balls:
                                        if item.point_query(p):
                                            rodobject2=item
                                            rod_point2=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    for item in store.polys:
                                        if item.point_query(p):
                                            rodobject2=item
                                            rod_point2=[p[0]-item.body.position.x+store.campos[0],p[1]-item.body.position.y]
                                    try:
                                        o1=rodobject1
                                        o2=rodobject2
                                        rest_length=o1.body.position.get_distance(o2.body.position)
                                        newrod=pymunk.PinJoint(o1.body, o2.body, rod_point1, rod_point2)
                                        store.rods.append(newrod)
                                        space.add(newrod)
                                    except:
                                        pass
                                    rodobject2=None
                                    rodobject1=None
                                    rod_point1=None
                                    rod_point2=None

                            if store.drop_item == "fire":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                for item in store.balls:
                                    if item.point_query(p):
                                        item.collision_type=COLLTYPE_FIRE
                                        item.burn_level=0
                                for item in store.polys:
                                    if item.point_query(p):
                                        item.collision_type=COLLTYPE_FIRE
                                        item.burn_level=0
                                        
                            if store.drop_item == "draw":
                                store.old_pos=[pygame.mouse.get_pos()[0], flipy(pygame.mouse.get_pos()[1])]

                            if store.drop_item == "character":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                for item in store.polys:
                                    if item.point_query(p):
                                        item.collision_type=COLLTYPE_CHAR
                                        store.char = item
                                        
                            if store.drop_item == "poly":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                p=[p[0], p[1]]
                                p[0]+=store.campos[0]
                                p[1]+=store.campos[1]
                                store.poly_points.append(p)

                            if store.drop_item == "motor":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                for item in store.balls:
                                    if item.point_query(p):
                                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                                        rotation_body.position = item.body.position
                                        space.add(rotation_body)
                                        item.friction = 1
                                        motor=pymunk.SimpleMotor(rotation_body, item.body, store.motor_rate)
                                        space.add(motor)
                                        store.motors.append(motor)
                                for item in store.polys:
                                    if item.point_query(p):
                                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                                        rotation_body.position = item.body.position
                                        space.add(rotation_body)
                                        item.friction = 1
                                        motor=pymunk.SimpleMotor(rotation_body, item.body, store.motor_rate)
                                        space.add(motor)
                                        store.motors.append(motor)
                                        
                            if store.drop_item == "pin":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                for item in store.balls:
                                    if item.point_query(p):
                                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                                        rotation_body.position = p
                                        #space.add(rotation_body)
                                        item.friction = 1
                                        pin=pymunk.PinJoint(rotation_body, item.body, [0,0], item.body.world_to_local(p))
                                        space.add(pin)
                                        store.pins.append(pin)
                                        pin.real_pos=p
                                for item in store.polys:
                                    if item.point_query(p):
                                        rotation_body = pymunk.Body(pymunk.inf, pymunk.inf)
                                        rotation_body.position = p
                                        #space.add(rotation_body)
                                        item.friction = 1
                                        pin=pymunk.PinJoint(rotation_body, item.body, [0,0], item.body.world_to_local(p))
                                        space.add(pin)
                                        store.pins.append(pin)
                                        pin.real_pos=p

                            if store.drop_item == "explosion":
                                p = pygame.mouse.get_pos()[0]+store.campos[0], flipy(pygame.mouse.get_pos()[1])+store.campos[1]
                                body = pymunk.Body(pymunk.inf, pymunk.inf)
                                body.position = p
                                shape = pymunk.Circle(body, 1, (0,0))
                                shape.friction = 0.99
                                space.add(shape)
                                store.explosions.append(shape)
                                store.all.append(shape)
                                shape.collision_type = COLLTYPE_EXPLOSION

                            if store.drop_item == "line":
                                if line_point1 is None:
                                    line_point1 = pymunk.Vec2d(event.pos[X]-store.campos[0], flipy(event.pos[Y])-store.campos[1])

                            if store.drop_item == "grab":
                                p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                                for item in store.polys:
                                    if item.point_query(p):
                                        print "Grabbed a Poly"
                                        mouse_grab_spring = pymunk.DampedSpring(mouse_shape.body, item.body, [0, 0], [0,0], 10, 200, 1)
                                        space.add(mouse_grab_spring)
                                for item in store.balls:
                                    if item.point_query(p):
                                        print "Grabbed a Ball"
                                        mouse_grab_spring = pymunk.DampedSpring(mouse_shape.body, item.body, [0, 0], [0,0], 10, 200, 1)
                                        space.add(mouse_grab_spring)

                    elif event.button == 3:
                        line_point1 = None
                        box_point1 = None
                        spring_point1 = None
                else:
                    #---Box Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [515, store.mh+5, 80, 27]):
                        store.drop_item= "box"
                        store.menu_state="tool"
                    #------------------------------

                    #---Square Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [515, store.mh+35, 65, 22]):
                        store.drop_item= "square"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Line Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [410, store.mh+35, 35, 22]):
                        store.drop_item= "line"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Spring Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [450, store.mh+35, 60, 22]):
                        store.drop_item= "spring"
                        store.menu_state="tool"
                    #---------------------------------
                    
                    #---Poly Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [477, store.mh+60, 41, 22]):
                        store.drop_item= "poly"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Explosion Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [430, store.mh+5, 80, 27]):
                        store.drop_item= "explosion"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Character Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [585, store.mh+35, 88, 22]):
                        store.drop_item= "character"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Grab Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [363, store.mh+35, 43, 22]):
                        store.drop_item= "grab"
                        store.menu_state="tool"
                    #---------------------------------
                    
                    #---Fire Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [432, store.mh+60, 41, 22]):
                        store.drop_item= "draw"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Fire Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [390, store.mh+5, 36, 27]):
                        store.drop_item= "fire"
                        store.menu_state="tool"
                    #---------------------------------
                    
                    #---Car Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [598, store.mh+5, 35, 27]):
                        store.drop_item= "car"
                        store.menu_state="tool"
                    #---------------------------------
                    
                    #---Copy Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [195, store.mh+61, 44, 21]):
                        store.drop_item= "copy"
                        store.menu_state="tool"
                    #---------------------------------
                    
                    #---Motor Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [330, store.mh+5, 56, 27]):
                        store.drop_item= "motor"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Delete Button-----------------
                    if store.check_bounds(pygame.mouse.get_pos(), [195, store.mh+35, 54, 23]):
                        store.drop_item= "delete"
                        store.menu_state="tool"
                    #---------------------------------

                    #---Ball Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [555, store.mh+5, 35, 27]):
                        store.drop_item= "ball"
                        store.menu_state="tool"
                    #------------------------------
                    
                    #---Rod Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [393, store.mh+60, 35, 22]):
                        store.drop_item= "rod"
                        store.menu_state="tool"
                    #------------------------------
                    
                    #---Pin Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [638, store.mh+5, 35, 27]):
                        store.drop_item= "pin"
                        store.menu_state="tool"
                    #------------------------------

                    #---Gravity Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [720, store.mh+5, 69, 27]):
                        store.menu_state="gravity"
                    #------------------------------

                    #---Gravity Menu------------------
                    if store.menu_state=="gravity":
                        if store.check_bounds(pygame.mouse.get_pos(), [948, store.mh, 44, 44]):
                            store.gravityposition=[pygame.mouse.get_pos()[0]-948, pygame.mouse.get_pos()[1]-store.mh+8]
                            grav_y=int((store.gravityposition[1]-25)/2)
                            grav_x=int((store.gravityposition[0]-25)/2)
                            space.gravity.y=int(-grav_y*18)*6
                            space.gravity.x=int(grav_x*18)*6

                        if store.check_bounds(pygame.mouse.get_pos(), [895, store.mh+30, 44, 23]):
                            space.gravity.y=-900
                            space.gravity.x=0
                            store.gravityposition=[23,44]

                        if store.check_bounds(pygame.mouse.get_pos(), [895, store.mh+7, 44, 23]):
                            space.gravity.y=900
                            space.gravity.x=0
                            store.gravityposition=[23,0]

                        if store.check_bounds(pygame.mouse.get_pos(), [851, store.mh+30, 44, 23]):
                            space.gravity.y=0
                            space.gravity.x=0
                            store.gravityposition=[23,23]
                    #------------------------------

                    #---Tool Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [720, store.mh+35, 69, 27]):
                        store.menu_state=store.drop_item
                    if store.menu_state=="tool":
                        if store.drop_item=="square":
                            if event.button==4:
                                store.square_size+=1
                            if event.button==5:
                                if store.square_size>1:
                                    store.square_size-=1
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.square_size+=1
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                if store.square_size>1:
                                    store.square_size-=1
                        if store.drop_item=="ball":
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.circle_size+=1
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                if store.circle_size>1:
                                    store.circle_size-=1

                        if store.drop_item=="explosion":
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.explosion_power+=10
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                if store.explosion_power>20:
                                    store.explosion_power-=10

                        if store.drop_item=="motor":
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.motor_rate+=5
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                store.motor_rate-=5
                                
                        if store.drop_item=="line":
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.line_width+=2
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                if store.line_width>2:
                                    store.line_width-=2
                                    
                        if store.drop_item=="draw":
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+7, 44, 23]):
                                store.draw_delay+=1
                                store.move_frame=0
                            if store.check_bounds(pygame.mouse.get_pos(),  [950, store.mh+30, 44, 23]):
                                if store.draw_delay>1:
                                    store.draw_delay-=1
                                    store.move_frame=0
                    #------------------------------

                    #---Menu----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [5, store.mh+5, 44, 27]):
                        store.state="menu"
                        screen.blit(menuback, [0,0])
                    #------------------------------

                    #---Clear Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [105, store.mh+5, 53, 27]):
                        while len(store.balls) > 0:
                            for ball in store.balls:
                                store.remove_all_constraints(ball)
                                space.remove(ball, ball.body)
                                store.all.remove(ball)
                                store.balls.remove(ball)
                        while len(store.polys) > 0:
                            for poly in store.polys:
                                store.remove_all_constraints(poly)
                                space.remove(poly, poly.body)
                                store.polys.remove(poly)
                        while len(store.motors) > 0:
                            for motor in store.motors:
                                space.remove(motor)
                                store.motors.remove(motor)
                        while len(store.springs) > 0:
                            for spring in store.springs:
                                space.remove(spring)
                                store.springs.remove(spring)
                        while len(store.lines) > 0:
                            for line in store.lines:
                                space.remove(line)
                                store.all.remove(line)
                                store.lines.remove(line)
                    #------------------------------

                    #---Clear Moveables Button----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [55, store.mh+35, 135, 23]):
                        while len(store.balls) > 0:
                            for ball in store.balls:
                                store.remove_all_constraints(ball)
                                space.remove(ball, ball.body)
                                store.all.remove(ball)
                                store.balls.remove(ball)
                        while len(store.polys) > 0:
                            for poly in store.polys:
                                store.remove_all_constraints(poly)
                                space.remove(poly, poly.body)
                                store.polys.remove(poly)
                        while len(store.motors) > 0:
                            for motor in store.motors:
                                space.remove(motor)
                                store.motors.remove(motor)
                        while len(store.springs) > 0:
                            for spring in store.springs:
                                space.remove(spring)
                                store.springs.remove(spring)
                    #------------------------------

                    #---Save--------------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [55, store.mh+5, 44, 27]):
                        run_physics=False
                        for i in range(0, 100):
                            screen.blit(trans, [0,0])
                            pygame.time.delay(1)
                            pygame.display.flip()
                        store.state = "save"
                        store.find_all()
                    #------------------------------

                    #---Load----------------------
                    if store.check_bounds(pygame.mouse.get_pos(), [5, store.mh+35, 44, 23]):
                        run_physics=False
                        for i in range(0, 100):
                            screen.blit(trans, [0,0])
                            pygame.time.delay(1)
                            pygame.display.flip()
                        store.state = "load"
                        store.find_all()
                    #------------------------------

        elif event.type == pygame.MOUSEBUTTONUP:
            if store.state=="game":
                if event.button == 1:
                    if store.drop_item=="box":
                        if box_point1 is not None:
                            box_point2 = pymunk.Vec2d(event.pos[X], flipy(event.pos[Y]))
                            diff = [abs(box_point1.x-box_point2.x), abs(box_point1.y-box_point2.y)]
                            #diff = [box_point1.x-box_point2.x, box_point1.y-box_point2.y]
                            p = flipyv(pymunk.Vec2d(pygame.mouse.get_pos()))
                            p = [p[0], p[1]]
                            p[0]-=int(diff[0]/2)
                            p[1]-=int(diff[1]/2)
                            p[1]+=int(diff[1])
                            if box_point1.y < box_point2.y:
                                p[1]-=diff[1]
                            if box_point1.x > box_point2.x:
                                p[0]+=diff[0]
                            newpoly=store.create_box(pos = p, sizex=diff[0], sizey=diff[1])
                            newpoly.kill_me = False
                            store.polys.append(newpoly)
                            store.all.append(newpoly)
                            box_point1=None
                            box_point2=None

                    if store.drop_item=="line":
                        if line_point1 is not None:
                            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                                diff_x=abs(line_point1[0]-pygame.mouse.get_pos()[0])
                                diff_y=abs(line_point1[1]-pygame.mouse.get_pos()[1])
                                if diff_x>diff_y:
                                    print "set x"
                                    line_point2 = pymunk.Vec2d(event.pos[X]-store.campos[0], line_point1[1])
                                if diff_x<diff_y:
                                    print "set y"
                                    line_point2 = pymunk.Vec2d(line_point1[0], event.pos[1]-store.campos[1])    
                            else:
                                line_point2 = pymunk.Vec2d(event.pos[X]-store.campos[0], flipy(event.pos[Y])-store.campos[1])
                
                            body = pymunk.Body(pymunk.inf, pymunk.inf)
                            shape= pymunk.Segment(body, line_point1, line_point2, store.line_width)
                            
                            shape.friction = 0.99
                            shape.kill_me = False
                            space.add(shape)
                            store.lines.append(shape)
                            store.all.append(shape)

                            line_point1 = None

                    if store.drop_item=="grab":
                        if mouse_grab_spring != None:
                            space.remove(mouse_grab_spring)
                            mouse_grab_spring=None

                    if store.drop_item == "delete":
                        store.ddown = False

    if store.state=="menu":
        store.menu_update()
    elif store.state=="game":
        store.game_update()
    elif store.state=="save":
        store.save_update()
    elif store.state=="load":
        store.load_update()

    pygame.display.flip()
    clock.tick(60)
print "Exiting"