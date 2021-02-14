import numpy as np
def create_maze():
    maze = np.zeros((12,12))
    maze[:,0] = 1
    maze[0,:] = 1
    maze[-1,:] = 1
    maze[:,-1] = 1
    maze[1:6,7] = 1
    maze[5,4:7] = 1
    maze[10,10] = 2
    return maze

def dist(x,y):
    return 10-x + 10-y


class point():
    def __init__(self,x,y,cost,path):
        self.x = x
        self.y = y
        self.cost = cost
        self.path = path

maze = create_maze()
points = []
points.append(point(1,1,0,[(1,1)]))
maze[1][1] = -1
while True:
# for k in range(5):
    evaluation = points[0].cost + dist(points[0].x,points[0].y)
    index = 0
    #find small
    for i in range(len(points)):
        if points[i].cost + dist(points[i].x,points[i].y) < evaluation:
            evaluation = points[i].cost + dist(points[i].x,points[i].y)
            index = i
    #update points
    if maze[points[index].x][points[index].y + 1] == 0:
        temp = points[index].path.copy()
        temp.append((points[index].x,points[index].y+1))
        points.append(point(points[index].x,points[index].y+1,points[index].cost + 1,temp))
        maze[points[index].x][points[index].y + 1] = -1
    if maze[points[index].x][points[index].y - 1] == 0:
        temp = points[index].path.copy()
        temp.append((points[index].x,points[index].y - 1))
        points.append(point(points[index].x,points[index].y-1,points[index].cost + 1,temp))
        maze[points[index].x][points[index].y - 1] = -1
    if maze[points[index].x+1][points[index].y] == 0:
        temp = points[index].path.copy()
        temp.append((points[index].x + 1,points[index].y))
        points.append(point(points[index].x+1,points[index].y,points[index].cost + 1,temp))
        maze[points[index].x+1][points[index].y] = -1
    if maze[points[index].x-1][points[index].y] == 0:
        temp = points[index].path.copy()
        temp.append((points[index].x - 1,points[index].y))
        points.append(point(points[index].x-1,points[index].y,points[index].cost + 1,temp))
        maze[points[index].x-1][points[index].y] = -1

    points.pop(index)
    if maze[points[index].x][points[index].y + 1] == 2:
        print(points[index].path)
        print(maze)
        break
    if maze[points[index].x][points[index].y - 1] == 2:
        print(points[index].path)
        print(maze)
        break
    if maze[points[index].x+1][points[index].y] == 2:
        print(points[index].path)
        print(maze)
        break
    if maze[points[index].x-1][points[index].y] == 2:
        print(points[index].path)
        print(maze)
        break
