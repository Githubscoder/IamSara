#Drawer - a easy coding envirment
from turtle import *
Error1 ='''
WritingError -
Command not found'''
def output(do, val):
    global Error1
    do = do.upper()
    if do == "F":
        forward(val)
    elif do == "B":
        backward(val)
    elif do == "R":
        right(val)
    elif do == "L":
        left(val)
    elif do == "U":
        penup()
    elif do == "D":
        pendown()
    elif do == "N":
        reset()
    else:
        print(Error1)
def string(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        output(cmd_type,num)
intro = '''Enter a program :
CLEAR = new drawing
U = put pen up,(so it doesn't touch screen while navgating)
D = oppsite of U, soyour pen will touch the screen
F100 = go forward the number of pixels written after F
B50 = go back,the number of pixels wrriten after B
R90 = turn the number of digrees after R to the right
L90 = turn the number of digrees after R to the left'''
screen = getscreen()
while True:
    t_prog = screen.textinput("Drawer", intro)
    print(t_prog)
    if t_prog == None or t_prog.upper() == "END":
        break
    string(t_prog)
        
