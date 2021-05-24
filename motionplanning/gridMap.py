Map = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
class Obstacle:
    def __init__(self,Location=None):
        self.Location=Location

class TrafficLight:
    def __init__(self, Location=None,pass_time=None,stop_time=None):
        self.Location = Location
        self.pass_time = pass_time
        self.stop_time = stop_time

obstacleLocation = [(2,2),(3,2),(4,2),(5,2),
                    (2,3),(3,3),(4,3),(5,3),
                    (2,4),(3,4),(4,4),(5,4),
                    (2,5),(3,5),(4,5),(5,5),
                    (8,5),(9,5),(10,5),(11,5),
                    (8,6),(9,6),(10,6),(11,6),
                    (8,7),(9,7),(10,7),(11,7),
                    (8,8),(9,8),(10,8),(11,8),
                    (13,8),(14,8),
                    (13,9),(14,9),
                    (13,10),(14,10),
                    (13,11),(14,11),
                    (9,11),(10,11),(11,11),
                    (9,12),(10,12),(11,12),
                    (9,13),(10,13),(11,13),
                    (3,11),(4,11),(5,11),(6,11),
                    (3,12),(4,12),(5,12),(6,12),
                    (3,13),(4,13),(5,13),(6,13),
                    ]
obstacle = Obstacle(obstacleLocation)

tlLoccationlist =[[(0,5),(1,5)],
                  [(6,5),(7,5)],
                  [(12,8)],
                  [(0,11),(1,11),(2,11)],
                  [(7,11),(8,11)],
                  [(12,11)]
                  ]
tlPass_time = [3,3,3,3,3,3]
tlStop_time = [10,10,10,10,10,10]
tlList = []
for i in range(len(tlPass_time)):
    tlList.append(TrafficLight(Location=tlLoccationlist[i],pass_time = tlPass_time[i],stop_time=tlStop_time[i]))


def initMaze(Map,Obstacle,TrafficLightList):
    maze = Map
    for i in range(len(Obstacle.Location)):
        maze[Obstacle.Location[i][0]][Obstacle.Location[i][1]] = 1
    for i in range(len(TrafficLightList)):
        tl = TrafficLightList[i]
        location = tl.Location
        for j in range(len(location)):
            maze[location[j][0]][location[j][1]] = 5
    return maze
