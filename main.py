import os, sys, time
from colorama import init, Fore, Back, Style
init()

class coord:
    def __init__(self, xcoord = 1, ycoord = 1):
        self.x = xcoord
        self.y = ycoord

def gotoxy(x, y):
    sys.stdout.write("\033[%d;%dH" % (y, x))
    sys.stdout.flush()
    
def gotogamexy(x, y):
    gotoxy((x + 1) * 2, y + 1)

def print_board():
    os.system("cls")
    for i in range(1, height + 3):
        for j in range(1, width + 3):
            gotoxy(2 * j - 1, i)
            if not((i > 1 and i < height + 2) and (j > 1 and j < width + 2)):
                print(Back.WHITE + "  ")
    print(Style.RESET_ALL)

def print_head():
    gotogamexy(head.x, head.y)
    print(Back.RED + "  ")
    print(Style.RESET_ALL)

def kbin():
    pass

height = 25
width = 30
head = coord(width / 2, height / 2)

print_board()
while True:
    print_head()
    kbin()


gotoxy(1, height + 3)
