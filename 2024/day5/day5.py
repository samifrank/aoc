rules = {} #Key: must come before, value: must come after key
updates = [] #List of lists updates
bad_updates = [] #List of bad updates to be processed in p2
def setup():

    # example = [[75,47,61,53,29],
    #             [97,61,53,29,13],
    #             [75,29,13],
    #             [75,97,47,61,53],
    #             [61,13,29],
    #             [97,13,75,29,47]]
    # ex_rules = {
    #         47: [53, 13, 61, 29],
    #         97: [13, 61, 47, 29, 53, 75],
    #         75: [29, 53, 47, 61, 13],
    #         61: [13, 53, 29],
    #         29: [13],
    #         53: [29, 13]
    #     }
    with open("rules.txt") as f:
        text = f.readlines()

        for rule in text:
            split = rule.strip().split("|")
          
            before = int(split[0])
            after = int(split[1])
            if before in rules:
                rules[before].append(after)
            else:
                rules[before] = [after]
        
    with open("updates.txt") as f:
        text = f.readlines()
        for update in text:
            update = [int(x) for x in update.strip().split(",")]
            updates.append(update)
    
    # print(rules)
    # print(updates)


def find_middle(update_report: list = [1,2,3,4,5]) -> int:
    """ part 1 """
    index_length = len(update_report) - 1
    return update_report[index_length//2]

def evaluate_p1(updates: list = updates):
    print("evaluating p1")
    print(updates)
    valid_update_added = 0
    for update in updates: 
        bad_update = False
        revers = list(reversed(update))
        # print(f"reversed: {revers}")
        for index, val in enumerate(revers):
            # print(f"index: {index}, val: {val}")
            if val in rules:
                # print(f"val: {val} has rules: {rules[val]}")
                # print(f"updates to inspect for rule violation {revers[index:]}")
                for x in revers[index:]:
                    if x in rules[val]:
                        print(f"update failed validation: {update}")
                        print(f"oh no bad update. rule violated for {x}")
                        bad_update = True
                        
                        bad_updates.append(update) #non reversed
                        break
        
        if not bad_update:
            valid_update_added += find_middle(update)

    # print(valid_update_added)    

def evaluate_p2():
    
    def __swapped(update: list, index1: int, index2: int) -> list:
        update[index1], update[index2] = update[index2], update[index1]
        return update

    updated = []
    now_valid_added = 0

    for update in bad_updates:
        sorted_flag = False
        update_copy = update[:]
        while not sorted_flag:
            sorted_flag = True
            for index, val in enumerate(update_copy):
                """check if val is in later elements rules list. If so, swap"""
                for index2, val2 in enumerate(update_copy[index+1:], start=index+1):
                    if val2 in rules:
                        rules_for_val2 = rules[val2]
                        if val in rules_for_val2:
                            update_copy = __swapped(update_copy, index, index2)
                            sorted_flag = False
       
        if update_copy not in updated:
            print(f"update_copy: {update_copy} type: {type(update_copy)}")
            
            updated.append(update_copy)
            evaluate_p1([update_copy]) #make list of lists
            now_valid_added += find_middle(update_copy)

    

    print(f"added middle values of now_valid_added: {now_valid_added}")
    

setup()
evaluate_p1()
evaluate_p2()