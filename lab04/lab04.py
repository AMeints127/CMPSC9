from Stack import Stack

def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='',end='')
        print("|")
    return



def solveMaze(maze, startX, startY):
    count = 1
    s = Stack()
    x = startX
    y = startY
    pos = [x, y]
    s.push(pos)

    while s.isEmpty() == False:
        pos = s.peek()
        x = pos[0]
        y = pos[1]
        
        if maze[x][y] in [' ','G']:
            maze[x][y] = count
         

        if maze[x-1][y] in [' ', 'G']:
            s.push([x-1,y])
            if maze[x-1][y] == 'G':
                return True
            count += 1
            maze[x-1][y] = count
            continue
        
        if (maze[x][y-1] in [' ', 'G']):
            if maze[x][y-1] == 'G':
                return True
            count += 1
            maze[x][y-1] = count
            s.push([x,y-1])
            continue
        
        if (maze[x+1][y] in [' ', 'G']):
            s.push([x+1,y])
            if maze[x+1][y] == 'G':
                return True
            count += 1
            maze[x+1][y] = count
            continue
        
        if (maze[x][y+1] in [' ', 'G']):
            s.push([x,y+1])
            if maze[x][y+1] == 'G':
                return True
            count += 1
            maze[x][y+1] = count
            continue
        s.pop()
        
    return False
        



        
    
