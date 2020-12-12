import numpy as np
pos = np.zeros([2], dtype=int)
directions = {
    'N': np.array([0,1]),
    'S': np.array([0,-1]),
    'E': np.array([1,0]),
    'W': np.array([-1,0]),
    'F': np.array([1,0])
}

def rotate(command, directions):
    
    angle = np.radians(command[1])
    if command[0] == 'R':
        angle = -angle
    r = np.round(np.array(( (np.cos(angle), -np.sin(angle)),
                    (np.sin(angle), np.cos(angle)))))

    return r.dot(directions)

def move(command, directions):
    return directions[command[0]]*command[1]

#for part 2:
wp = np.array([10,1])
pos2 = np.copy(pos) 

with open('day12.txt') as f:
    for command in f:
        command = command.replace('\n', '')
        command = command[0], int(command[1:])
        # Part1
        if command[0] in ('R', 'L'):
            directions['F'] = rotate(command, directions['F'])
        else:
            pos =  pos + move(command, directions)
        # Part 2
        if command[0] =='F':
            pos2 = pos2 + wp*command[1]
        elif command[0] in ('R', 'L'):
            wp = rotate(command, wp)
        else:
            wp =  wp + move(command, directions) 
        
print(f"Part 1: {sum(abs(pos))=}")
print(f"Part 2: {sum(abs(pos2))=}")
