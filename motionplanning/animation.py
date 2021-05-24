from matplotlib import pyplot as plt
from matplotlib import ticker
import pathPlanning as pp
import gridMap as gm

tlList = gm.tlList


def animation(maze, path, time):
    plt.grid()
    ax = plt.axes()
    plt.xlim([0,15])
    plt.ylim([0,15])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    for i in range(time+1):
        for j in range(len(tlList)):
            if pp.can_pass(tlList[j],i):
                for k in range(len(tlList[j].Location)):
                    maze[tlList[j].Location[k][0]][tlList[j].Location[k][1]] = 0
            else:
                for k in range(len(tlList[j].Location)):
                    maze[tlList[j].Location[k][0]][tlList[j].Location[k][1]] = 5
        maze[path[i][0]][path[i][1]] = 2
        print(path[i])
        for x in range(len(maze)):
            for y in range(len(maze[x])):
                if maze[x][y] == 1:
                    X  = [x,x+1]
                    Y1 = [y,y]
                    Y2 = [y+1, y+1]
                    plt.fill_between(X, Y1, Y2, color = 'blue', alpha = 0.5)
                if maze[x][y] == 2:
                    X  = [x,x+1]
                    Y1 = [y,y]
                    Y2 = [y+1, y+1]
                    plt.fill_between(X, Y1, Y2, color = 'gray', alpha = 0.5)
                if maze[x][y] == 5:
                    X  = [x,x+1]
                    Y1 = [y,y]
                    Y2 = [y+1, y+1]
                    plt.fill_between(X, Y1, Y2, color = 'red', alpha = 0.5)
                if maze[x][y] == 0:
                    X  = [x,x+1]
                    Y1 = [y,y]
                    Y2 = [y+1, y+1]
                    plt.fill_between(X, Y1, Y2, color = 'white', alpha = 0.5)
        plt.pause(0.1)
    plt.show()
