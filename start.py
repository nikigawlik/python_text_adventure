## game flow diagram ##

#main
  #gen new world
    #ingame...
  #load world
    #select world
      #ingame...
  #exit

#ingame
  #scene
    #select path
      #scene...
    #exit

## ------------------

import os


## METHODS #

def cls():
    #os.system('cls' if os.name=='nt' else 'clear')
    #print('\n'*128)
    pass


## game state machine ##

def game_state_init():
    global game_state
    game_state = "men_main"

def set_game_state(state):
    global game_state
    cls()
    #print( str(game_state) + " -> " + str(state))
    game_state = state

    if game_state == "men_main":
        show_multichoice("generate new world", "load existing world", "exit")
        evalmc_gs("men_gen", "men_load", "game_end")
        
    elif game_state == "men_gen":
        show_multichoice("generate world", "back")
        evalmc_gs("worldgen", "men_main")
        
    elif game_state == "men_load":
        show_text("Sorry! Loading and saving is currently not supported.")
        show_multichoice("back")
        evalmc_gs("men_main") #TODO
        
    elif game_state == "game_end":
        pass
    
    elif game_state == "worldgen":
        #TODO game init stuff
        global world
        world = World()
        world.page.addOption("do nothing", Link(world.page))
        world.page.setText("You sit in an empty room. There is nothing to do.")
        set_game_state("ingame")
        
    elif game_state == "ingame":
        set_game_state("scene")
        
    elif game_state == "scene":
        #print('World: ' + str(world.getOptionTexts()))
        show_text(world.getCurrentText())
        show_multichoice(*world.getOptionTexts())
        world.chooseOption(evalmc())
        set_game_state("scene")
        
    elif game_state == "":
        show_multichoice()
        evalmc_gs()



## UI methods ##

def show_multichoice(*args):
    i = 0;
    for arg in args:
        i+=1
        print(str(i) + " - " + arg)

def evalmc():
    try:
        r = int(input(">"))-1
    except (ValueError):
        r = evalmc()
    return r

def evalmc_gs(*args):
    num = -1
    while num < 0 or num >= len(args):
        num = evalmc()
    set_game_state(args[num])
    return num

def show_text(text):
    print("\n" + text + "\n")


## World model ##

class World:
    def __init__(self):
        self.page = Page()
    def getCurrentText(self):
        return self.page.getText()
    def getOptionTexts(self):
        return self.page.getOptionTexts()
    def chooseOption(self, num):
        self.page = self.page.getOptionLinks()[num].getDestination()

class Page:
    def __init__(self):
        self.text = ""
        self.options = []
    def setText(self, text):
        self.text = text
    def getText(self):
        return self.text
    def getOptionTexts(self):
        return [o[0] for o in self.options]
    def getOptionLinks(self):
        return [o[1] for o in self.options]
    def addOption(self, text, link):
        self.options.append([text, link])

class Link:
    def __init__(self, dest):
        self.dest = dest
    def setDestination(self, dest):
        self.dest = dest
    def getDestination(self):
        return self.dest

## GAME ##

game_state_init()
set_game_state("men_main")




