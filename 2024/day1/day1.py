right_list = []
left_list = []

def createList():
    with open('input.txt', 'r') as file:
        read_data = file.readlines()
        for line in read_data:
            locations = line.split("  ")
            right_list.append(int(locations[1]))
            left_list.append(int(locations[0]))

def evaluate():
    """ part 1 """
    total_distance = 0
    right_list.sort()
    left_list.sort()
    
    for i in range(len(right_list)):
        total_distance += abs(right_list[i] - left_list[i])

    print(total_distance)

def simiarityScore():
    """ part 2 """
    similatity_score = 0
    for loc_id in left_list:
        occurances = 0
        for loc_id2 in right_list:
            if loc_id == loc_id2:
                occurances += 1
        similatity_score += occurances * loc_id
    print(similatity_score)

createList()
evaluate()
simiarityScore()