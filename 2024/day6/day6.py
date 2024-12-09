import pprint
import re
battle_map = {}
steps = 1
walked_positions = []

"""
Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.

guard is the V
obstacle is the #

goal: make it to the bottom of the map.
count how many steps it takes to get there
"""
def setup():
    with open("input.txt") as f:
        lines = f.readlines()
        for index,line in enumerate(lines):
            battle_map[index] = list(line.strip())

    # pprint.pprint(battle_map)


def evaluate():
    directions = {
        1: '^', #up 
        2: '>', #right, 90 degrees of up
        3: 'v', #down, 90 degrees of right
        4: '<' #left, 90 degrees of down
    }
    current_direction = directions[1]
    position = (0,0)
    # print("length of battle_map: ", len(battle_map))
    """find starting position"""
    for row, col in battle_map.items():
        # print("row: ", row, " col: ", col)
        if directions[1] in col:
            # print("found guard at row: ", row, " col: ", col.index(directions[1]))
            position = (row, col.index(directions[1]))
            walked_positions.append(position)
            break
    
    """start moving guard"""
    while position[0] < len(battle_map) and position[0] >= 0 and position[1] < len(battle_map) and position[1] >= 0:
        position, moved = move(position, current_direction)
        if not moved:
            current_d_key = [key for key, val in directions.items() if val == current_direction][0]
            # print(f"current direction key: {current_d_key}")
            if current_d_key != 4:
                current_direction = directions[current_d_key + 1]
            else:
                current_direction = directions[1]
    #         print("new direction: ", current_direction)
    #         print(f"continuing to move. current steps: {steps}")

    # print("total steps taken: ", steps)
    # print("total distinct positions walked: ", len(walked_positions))

    # print("walked positions: ", walked_positions)


def check_position(row, col, direction=None):
    if direction == '^':
        return battle_map[row-1][col], (row-1, col)
    elif direction == '>':
        return battle_map[row][col+1], (row, col+1)
    elif direction == 'v':
        return battle_map[row+1][col], (row+1, col)
    elif direction == '<':
        return battle_map[row][col-1], (row, col-1)

def move(position: tuple, current_direction: str): #new tuple if move is successful, same tuple that was passed if blocked
    """move the guard"""
    global steps
    global walked_positions
    obstacle = "#"
    next_, pos = check_position(position[0], position[1], current_direction)
    if next_ == obstacle:
        return position, False #blocked
    else:
        if pos[0] < len(battle_map) and pos[0] >= 0 and pos[1] < len(battle_map) and pos[1] >= 0:
            steps += 1
            if pos not in walked_positions:
                walked_positions.append(pos)
        return pos, True #moved
        


setup()
evaluate()