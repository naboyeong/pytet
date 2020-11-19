from matrix import *
import random

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

def transpose(a):
	arra = a.get_array()
	n = len(arra)
	b = [[0 for i in range(n)] for e in range (n)]
	if n == 2:
		return a
	elif n==3:
		b[0][0] = arra[2][0]
		b[0][1]=arra[1][0]
		b[0][2]=arra[0][0]
		b[1][0]=arra[2][1]
		b[1][1]=arra[1][1]
		b[1][2]=arra[0][1]
		b[2][0]=arra[2][2]
		b[2][1]=arra[1][2]
		b[2][2]=arra[0][2]
		return b
	elif n == 4:
		b[0][0]=arra[3][0] 
		b[0][1]=arra[2][0]
		b[0][2]=arra[1][0]
		b[0][3]=arra[0][0]
		b[1][0]=arra[3][1]
		b[1][1]=arra[2][1]
		b[1][2]=arra[1][1]
		b[1][3]=arra[0][1]
		b[2][0]=arra[3][2]
		b[2][1]=arra[2][2]
		b[2][2]=arra[1][2]
		b[2][3]=arra[0][2]
		b[3][0]=arra[3][3]
		b[3][1]=arra[2][3]
		b[3][2]=arra[1][3]
		b[3][3]=arra[0][3]
		return b


def transpose1(a):
	arra = a.get_array()
	n = len(arra)
	b = [[0 for i in range(n)] for e in range (n)]
	if n == 2:
		return a
	elif n==3:
		b[0][0] = arra[0][2]
		b[0][1]=arra[1][2]
		b[0][2]=arra[2][2]
		b[1][0]=arra[0][1]
		b[1][1]=arra[1][1]
		b[1][2]=arra[2][1]
		b[2][0]=arra[0][0]
		b[2][1]=arra[1][0]
		b[2][2]=arra[2][0]
		return b
	elif n == 4:
		b[0][0]=arra[0][3] 
		b[0][1]=arra[1][3]
		b[0][2]=arra[2][3]
		b[0][3]=arra[3][3]
		b[1][0]=arra[0][2]
		b[1][1]=arra[1][2]
		b[1][2]=arra[2][2]
		b[1][3]=arra[3][2]
		b[2][0]=arra[0][1]
		b[2][1]=arra[1][1]
		b[2][2]=arra[2][1]
		b[2][3]=arra[3][1]
		b[3][0]=arra[0][0]
		b[3][1]=arra[1][0]
		b[3][2]=arra[2][0]
		b[3][3]=arra[3][0]
		return b
###
### initialize variables
###     
array1 = [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]
array2 = [[1,1],[1,1]]
array3 = [[1,0,0],[1,1,1],[0,0,1]]
array4 = [[1,0,0],[1,1,1],[0,0,0]]
array5 = [[0,0,1],[1,1,1],[0,0,0]]
array6 = [[0,0,1],[1,1,1],[1,0,0]]
array7 = [[0,1,0],[1,1,1],[0,0,0]]
array = [array1, array2, array3, array4, array5, array6, array7]
sub= array[random.randrange(0,7)]
### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(sub)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        currBlk = transpose(currBlk)
        currBlk = Matrix(currBlk)
  
    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top += 1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
        top -= 1
     
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            currBlk = transpose1(currBlk)
            currBlk = Matrix(currBlk)
            
           
            
        elif key == ' ': # undo: move up
            newBlockNeeded =True
            
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        sub = array[random.randrange(0,7)]
        currBlk = Matrix(sub)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
