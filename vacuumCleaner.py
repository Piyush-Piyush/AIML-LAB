import random

room = [ 
    [1, 1, 1, 1], 
    [1, 1, 1, 1], 
    [1, 1, 1, 1], 
    [1, 1, 1, 1], 
    ] 

print(room) 
x =0 
y= 0 
 

while x < 4: 
    while y < 4: 
        room[x][y] = random.choice([0,1]) 
        y= y+1 
    x= X + 1 
    y=0 
 

print(room) 
x =0 
y= 0 
 

# Before cleaning the room I detect all of these random dirts [[0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0]] 
while x < 4: 
    while y < 4: 
        if room[x][y] == 1:  
            room[x][y] = 0 
            print(x, y,"cleaned") 
        y+=1 
    x+=1 
print(room)