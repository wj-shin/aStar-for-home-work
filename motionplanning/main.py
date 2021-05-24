import fire
import gridMap as gm
import aStar as star
import animation as ani
import pathPlanning as pp
from matplotlib import pyplot as plt
from matplotlib import ticker

def main(start=(0,0),end=(14,14),runAnimation=True,Index=10):
    maze = gm.initMaze(gm.Map,gm.obstacle,gm.tlList)
    if(start==None or end ==None):
        print("Please give me a start point and end point")
    else:
        if(start[0]>14 or start[1]>14 or end[0]>14 or end[1]>14):
            print("out of range")
        else:
            time,path = pp.pathplanning(maze,start,end)
            print(time)
            if(Index == 10):
                temp = min(time)
                minIndex = time.index(temp)
                if(runAnimation==True):
                    ani.animation(maze,path[minIndex],time[minIndex])
            else:
                if(runAnimation == True):
                    ani.animation(maze,path[Index-1],time[Index-1])

if __name__ == '__main__':
    fire.Fire()
