#coding=gbk
#created by Adam Chen 2016.12

from graphics import *
import math
from ship import *

# 创建窗口
win=GraphWin('battleship',600,300)
win.setCoords(0,0,26,13)
def changecolor():
    for m in range(10):
        for x in range(15):
            if H[m][x]!=0:
                if H[m][x][0] == H[k][l][0] and H[m][x][1] == H[k][l][1]:
                    Line(Point(x+1,11.5-m),Point(x+2,11.5-m)).draw(win)
                    Line(Point(x+1.5,12-m),Point(x+1.5,11-m)).draw(win)
def main():
    #画格子
    for i in range(2,13):
        Line(Point(1,i),Point(16,i)).draw(win)
    for i in range(1,17):
        Line(Point(i,2),Point(i,12)).draw(win)
    #画坐标
    for i in range(15):
        Text(Point(1.5+i,12.5),'%d' %i).draw(win)
    x='ABCDEFGHIJ'
    for i in range(10):
        Text(Point(0.5,11.5-i),x[i]).draw(win)

   

main()



#消息提示框
t = Text(Point(7,1),'Enter a number between 2 and 8 then Start!')
t.draw(win)

        
t2 = Entry(Point(23,1),4)
t2.draw(win)

t3=Text(Point(19.5,1),'Ship numbers:')
t3.draw(win)

x=Rectangle(Point(18.5,4),Point(23,2))
x.setFill('lightgrey')
x.draw(win)

q=Rectangle(Point(23.5,12.5),Point(25.5,11.5))
q.setFill('grey')
q.draw(win)

tq=Text(Point(24.5,12),'Quit')
tq.draw(win)

t4=Text(Point(20.75,3),'Start!')
t4.draw(win)



#开始游戏的准备    
while True:
    pt=win.getMouse()
    if 23.5<=pt.getX()<=25.5 and 11.5<=pt.getY()<=12.5:
        win.close()
    if 18.5<=pt.getX()<=23 and 2<=pt.getY()<=4:
        try:
            n0 = t2.getText()
            n=eval(n0)
            if not 2<=n<=8:
                assert False
            t4.setText('Playing....')
            t4.setFill('darkgrey')
            G,H,I= randship(n)
            break
        except:
            t.setText('You should enter a integer between 2 and 8!')
            continue
        
       
    if 23.5<=pt.getX()<=25.5 and 11.5<=pt.getY()<=12.5:
        win.close()
        
for i in G:
    print i
    
Missile=100
t5=Text(Point(20.5,10),'Missile left:%d' %Missile)
t5.draw(win)

t6=Text(Point(20.5,8),'Ship to sink:%d' %n)
t6.draw(win)

t7=Text(Point(20.5,6),'Hit rate:0.00%')
t7.draw(win)

hitnumber=0

t.setText('Game start!\nClick a square to fight!')

#游戏主进程
while True:
    p = win.getMouse()
    if 23.5<=p.getX()<=25.5 and 11.5<=p.getY()<=12.5:
        win.close()
    a = math.floor(p.getX())
    b = math.ceil(p.getY())
    if 1<=a<=15 and 3<=b<=12:
        i = int(13-b)
        j = int(a)
        if G[i-1][j-1] == 0:
            t.setText('Ha Ha,You missed me!')
            Line(Point(a,b),Point(a+1,b-1)).draw(win)
            Line(Point(a,b-1),Point(a+1,b)).draw(win)
            G[i-1][j-1] = -1
            
        elif G[i-1][j-1] == 1:

            c = Circle(Point(a+0.5,b-0.5),0.5)
            c.setFill('Cyan')
            c.draw(win)
            k = H[i-1][j-1][0]-1
            l = H[i-1][j-1][1]-1
            hitnumber+=1
            if H[k][l][4] == 1:
                t.setText('You sank the rowboat!')
                n=n-1
                I[1]-=1
                if I[1]==0:
                    t.setText('You sank the rowboat!\nNo rowboat remaining to sink.')
                else:
                    t.setText('You sank the rowboat!\n %d rowboat remaining to sink.' %I[1])
                t6.setText('Ship to sink:%d' %n)
                changecolor()
            else:
                H[k][l][4]=H[k][l][4]-1
                t.setText('Direct hit!')
            G[i-1][j-1] = -1
        elif G[i-1][j-1] == 2:

            c = Circle(Point(a+0.5,b-0.5),0.5)
            c.setFill('Red')
            c.draw(win)
            k = H[i-1][j-1][0]-1
            l = H[i-1][j-1][1]-1
            hitnumber+=1
            if H[k][l][4] == 1:
                t.setText('You sank the submarine!')
                n=n-1
                I[2]-=1
                if I[2]==0:
                    t.setText('You sank the submarine!\nNo submarine remaining to sink.')
                else:
                    t.setText('You sank the submarine!\n %d submarine remaining to sink.' %I[2])
                t6.setText('Ship to sink:%d' %n)
                changecolor()
            else:
                H[k][l][4]=H[k][l][4]-1
                t.setText('Direct hit!')
            G[i-1][j-1] = -1
        elif G[i-1][j-1] == 3:

            c = Circle(Point(a+0.5,b-0.5),0.5)
            c.setFill('Blue')
            c.draw(win)
            k = H[i-1][j-1][0]-1
            l = H[i-1][j-1][1]-1
            hitnumber+=1
            if H[k][l][4] == 1:
                t.setText('You sank the speedboat!')
                n=n-1
                I[3]-=1
                if I[3]==0:
                    t.setText('You sank the speedboat!\nNo speedboat remaining to sink.')
                else:
                    t.setText('You sank the speedboat!\n %d speedboat remaining to sink.' %I[3])
                t6.setText('Ship to sink:%d' %n)
                changecolor()
            else:
                H[k][l][4]=H[k][l][4]-1
                t.setText('Direct hit!')
            G[i-1][j-1] = -1
        elif G[i-1][j-1] == 4:

            c = Circle(Point(a+0.5,b-0.5),0.5)
            c.setFill('Green')
            c.draw(win)
            k = H[i-1][j-1][0]-1
            l = H[i-1][j-1][1]-1
            hitnumber+=1
            if H[k][l][4] == 1:
                t.setText('You sank the battleship!')
                n=n-1
                I[4]-=1
                if I[4]==0:
                    t.setText('You sank the battleship!\nNo battleship remaining to sink.')
                else:
                    t.setText('You sank the battleship!\n %d battleship remaining to sink.' %I[4])
                t6.setText('Ship to sink:%d' %n)
                changecolor()
            else:
                H[k][l][4]=H[k][l][4]-1
                t.setText('Direct hit!')
            G[i-1][j-1] = -1
        elif G[i-1][j-1] == 5:
            c = Circle(Point(a+0.5,b-0.5),0.5)
            c.setFill('Magenta')
            c.draw(win)
            k = H[i-1][j-1][0]-1
            l = H[i-1][j-1][1]-1
            hitnumber+=1
            if H[k][l][4] == 1:
                t.setText('You sank the longboat!')
                n=n-1
                I[5]-=1
                if I[5]==0:
                    t.setText('You sank the longboat!\nNo longboat remaining to sink.')
                else:
                    t.setText('You sank the longboat!\n %d longboat remaining to sink.' %I[5])
                t6.setText('Ship to sink:%d' %n)
                changecolor()
            else:
                H[k][l][4]=H[k][l][4]-1
                t.setText('Direct hit!')
            G[i-1][j-1] = -1
        elif G[i-1][j-1] == -1:
            t.setText('You have already tried that!')
    else:
        t.setText('That\'s not a valid square,try again!')
        
    Missile-=1
    t5.setText('Missile left:%d' %Missile)

    hitrate=float(hitnumber)/(100-Missile)*100
    t7.setText('Hit rate:%.2f%%' %hitrate)

    if Missile<=0:
        t.setText('You fail the game!')
        break
    if n<=0:
        t.setText('You win!')
        break
    

while True:
    px=win.getMouse()
    if 23.5<=px.getX()<=25.5 and 11.5<=px.getY()<=12.5:
        win.close()

#Copyright@陈沈威 @李嘉麒 2016.12.13
    
    
        
