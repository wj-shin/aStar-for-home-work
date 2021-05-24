import gridMap as gm
import aStar as star

def can_pass(TrafficLight,time):
    pt = TrafficLight.pass_time
    st = TrafficLight.stop_time
    period = pt + st
    if time%period<pt:
        return True
    else:
        return False

def remain_time(TrafficLight,time):
    pt = TrafficLight.pass_time
    st = TrafficLight.stop_time
    period = pt + st
    specific_time = time % period
    remain_time = st - specific_time + pt
    return remain_time

def set_temp(i,j):
    temp1 = gm.tlList[i]
    tempLocation1 = temp1.Location
    tempDestination1 = tempLocation1[len(tempLocation1)-1]
    temp2=gm.tlList[j]
    tempLocation2 = temp2.Location
    tempDestination2 = tempLocation2[len(tempLocation2)-1]
    return temp1,temp2,tempDestination1, tempDestination2

def pathplanning(maze,start,end):
    count = 0
    time = [0,0,0,0,0,0,0,0,0]
    path = [[],[],[],[],[],[],[],[],[]]
    for i in range(3):
        for j in range(3,6):
            print(i,"  ", j)
            print(count)
            print(path[count])
            temp1, temp2,tempDestination1,tempDestination2 = set_temp(i,j)
            print("pass")
            if(i == 2 and j == 3):
                tempPath1 = star.astar1(maze, start, tempDestination1)
                tempPath2 = star.astar1(maze,tempDestination1,tempDestination2)
                del(tempPath2[0])
                tempPath3 = star.astar2(maze,tempDestination2,end)
                del(tempPath3[0])
            else:
                tempPath1 = star.astar1(maze, start, tempDestination1)
                tempPath2 = star.astar2(maze,tempDestination1,tempDestination2)
                del(tempPath2[0])
                tempPath3 = star.astar2(maze,tempDestination2,end)
                del(tempPath3[0])
            time1 = len(tempPath1)-1
            time2 = len(tempPath2)
            time3 = len(tempPath3)
            if can_pass(temp1,time1):
                print("this line was exacuted code number1  ",i,"  ", j)
                time[count] = time1+time2
            else:
                rt = remain_time(temp1,time1)
                for k in range(rt):
                    tempPath1.append(tempDestination1)
                time[count] = time1+rt+time2
                print("this line was exacuted code number2  ",i,"  ", j)
            time4 = time[count]
            if can_pass(temp2,time4):
                time[count] = time4 + time3
                print("this line was exacuted code number3  ",i,"  ", j)
            else:
                rt = remain_time(temp2,time4)
                for k in range(rt):
                    tempPath2.append(tempDestination2)
                time[count] = time4+rt+time3
                print("this line was exacuted code number4  ",i,"  ", j)
            path[count].extend(tempPath1)
            path[count].extend(tempPath2)
            path[count].extend(tempPath3)

            count = count + 1
    return time,path
