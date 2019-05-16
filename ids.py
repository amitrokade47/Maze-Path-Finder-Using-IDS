'''Name: Amit Rokade
   Problem 1:Solving Maze using IDS Algorithm
'''

import turtle ,sys,math,random,time

grid=[]

with open('smallest.txt') as file:
    for line in file:
        grid.append(line.split())

t=turtle.Turtle()
cellHeight=10
cellWidth=10
rows=len(grid)
print("Rows",rows)
cols=len(grid[0])
print("Columns",cols)
goal=(rows-1,cols-1)
start=(0,0)
neighbors={}
visited=[]
t.speed(0)
path=[]

#UNCOMMENT THIS LINE TO MAKE PROGRAM RUN FASTER
# t._tracer(False)



def main(visited):
    colorgrid()
    for l in range(100):
        start_time=time.time()
        # print("Depth---------------------------------------------------------------------",l)
        val=DLS(start,goal,l,visited)
        if val is not False:
            # print(val)
            print(l+1," Steps")
            break
        else:
            visited=[]
    print("Time:", time.time() - start_time)

    # print(parent)
    turtle.mainloop()
    print("END---------------------------------------------")


def colorgrid():
    '''Used to draw the matrix in turtle and add neighbors for every cell, adjacent cells with walls are not added'''
    for x in range(rows):
        for y in range(cols):
            # print(x,y)
            add_neighbors(x,y)

            if x is goal[0] and y is goal[1]:
                print("here is goal")
                draw_filled_rect(x,y,"green")
            elif(grid[x][y]=='0'):
                draw_filled_rect(x,y,"white")
            elif(grid[x][y]=='1'):
                draw_filled_rect(x,y,"black")
            else:
                draw_filled_rect(x,y,"green")


def add_neighbors(x,y):
    '''Adding neighbors for the given cell'''
    curr_key=(x,y)
    list_of_neighbors=[]

    if (y<cols-1):
        if grid[x][y+1]!='1':
            list_of_neighbors.append((x,y+1))
    if (x<rows-1):
        if grid[x+1][y]!='1':
            list_of_neighbors.append((x+1, y))
    if(y>0):
        if grid[x][y-1]!='1':
            list_of_neighbors.append((x,y-1))
    if (x>0) :
        if grid[x-1][y]!='1':
            list_of_neighbors.append((x-1,y))

    copy=[]
    for neighbor in list_of_neighbors:

        if curr_key in neighbors:
            # print(copy.extend([neighbor]))
            # dates_dict.setdefault(key, []).append(date)
            neighbors.setdefault(curr_key,[]).append(neighbor)
            # neighbors[curr_key]=copy.extend([neighbor])
        else:
            neighbors[curr_key]=[neighbor]
            copy.extend(neighbors[curr_key])
        # print(type(neighbors[curr_key]))
        # print(neighbors[curr_key])


def draw_filled_rect(x,y,color):
    '''Drawing cell using turtle'''
    # pass
    t.up()

    t.goto(y*cellWidth,-x*cellHeight)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.forward(cellWidth)
        t.left(90)
    t.end_fill()
    t.up()

    # pass

def DLS(start_state,goal,depth,visited):
    '''Iterative Deeping Search algorithm '''
    visited.append(start_state)
    # print("Current parent",start_state)
    draw_filled_rect(start_state[0],start_state[1],"blue")

    if start_state==goal:
        print(depth)
        draw_filled_rect(goal[0],goal[1],"green")
        print("End can be reached")
        # draw_filled_rect(goal[0],goal[1],"red")
        return str(start_state[0])+":"+str(start_state[1])
    elif depth==0:
        # print("Val not found")
        return False

    else:
        val=False
        for neighbor in neighbors[start_state]:
            if neighbor not in visited and val is False:
                val=DLS(neighbor,goal,depth-1,visited)
        if val is not False:
            draw_filled_rect(start_state[0],start_state[1],"green")
            return val+","+str(start_state[0])+":"+str(start_state[1])
        return False



if __name__=="__main__":
    main(visited)