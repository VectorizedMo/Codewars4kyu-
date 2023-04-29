def checkcollision(index, direction, spiral, collisiondata, directions):
    try:
        directionindex = directions.index(direction)
        collisionindex = (collisiondata[directionindex])
        if collisionindex[0] == 'y':
            if index[0] > 1 and index[0] < len(spiral[0])-2 and index[1] > 1 and index[1] < len(spiral[0]) - 2:
                if spiral[index[0]+1][index[1]+collisionindex[1]] == 1 or spiral[index[0]-1][index[1]+collisionindex[1]] == 1:
                    return True
            if spiral[index[0]][index[1]+collisionindex[1]] == 0 and spiral[index[0]][index[1]+collisionindex[2]] == 1 and index[1] > 1 and index[1] < (len(spiral[0])-2):
                return True
            else:
                if spiral[index[0]][index[1]+collisionindex[1]] == 1 and spiral[index[0]][index[1]+collisionindex[2]] == 1:
                    return True   
                return False
        else:
            if spiral[index[0]+collisionindex[1]][index[1]] == 0 and spiral[index[0]+collisionindex[2]][index[1]] == 1 and index[0] > 1 and index[0] < len(spiral[0])-2:
                return True
            else:
                if spiral[index[0]+collisionindex[1]][index[1]] == 1 and spiral[index[0]+collisionindex[2]][index[1]] == 1:
                    return True     
                return False
    except IndexError:
        return False
    
def spiralize(size):
    collisiondata = [("y",1,2), ("x",1,2),("y",-1,-2), ("x",-1,-2)]
    spiral = [[0 for x in range(size)] for i in range(size)]
    directions = ["right", "down", "left", "up"]
    spiraldone = False
    x = 0
    y = 0
    rangenum = len(spiral[0])-1
    j = 0
    while not spiraldone:
        direction = directions[0]
        for i in range(size):
            if checkcollision((x,y), direction, spiral, collisiondata, directions) != True:
                spiral[x][y] = 1
                if i != size-1:
                    y += 1
            else:
                spiral[x][y] = 1
                break
        
        direction = directions[1]
        for i in range(size):
            if checkcollision((x,y), direction, spiral, collisiondata, directions) != True:
                spiral[x][y] = 1
                if i != size-1:
                    x += 1
            else:
                spiral[x][y] = 1
                break
        direction = directions[2]
        for i in range(size):
            if checkcollision((x,y), direction, spiral, collisiondata, directions) != True:
                spiral[x][y] = 1
                if i != size-1:
                    y -= 1
            else:
                spiral[x][y] = 1
                break
                
        direction = directions[3]
        for i in range(size):
            if checkcollision((x,y), direction, spiral, collisiondata, directions) != True:
                spiral[x][y] = 1
                if i != size-1:
                    x -= 1
            else:
                spiral[x][y] = 1
                break

        if j > size:
            return spiral
        j += 1  
    return spiral
    
def showspiral(args):
    for i,v in enumerate(args):
        for j,k in enumerate(v):
            if k == 1:
                args[i][j] = chr(0x0001F7E5)
            else:
                args[i][j] = chr(0x0001F7E6)
    for i in range(len(args)):
        print(*args[i])
        
spiralrange = 10
showspiral(spiralize(spiralrange))
