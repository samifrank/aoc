input_list = [] #[[int,..],]
safe_reports = 0

def setup():
    with open("input.txt") as f:
        readlines = f.readlines()
        for line in readlines:
            input_list.append(list(map(int, line.split(" "))))

def evaluate():
    """ part 1 """
    global safe_reports

    for report in input_list:
        safe = True 
        check_problem_dampener = False # part 2
        if isAscOrDesc(report): # either ascending or descending
            for i in range(len(report)-1):
                if not isSafeAdjacent(report[i], report[i+1]):
                    safe = False
                    check_problem_dampener = True
                    break
        else:
            safe = False
            check_problem_dampener = True
        
        if safe:
            safe_reports += 1
        if check_problem_dampener:
            problemDampener(report)
    print(f"fully safe_reports: {safe_reports}")

def isSafeAdjacent(left: int, right: int) -> bool:
    """ part 1 """
    if abs(left - right) >= 1 and abs(left - right) < 4:
        return True
    return False      

def isAscOrDesc(report: list) -> bool:
    """ part 1 """
    if report[0] > report[1]: #check descending
        for i in range(1, len(report)-1):
            if report[i] < report[i+1]:
                return False
        return True
    else: # report[0] < report[1] -- check ascending
        for i in range(1, len(report)-1):
            if report[i] > report[i+1]:
                return False
        return True

def problemDampener(report: list):
    """ part 2 
        determine if report is safe if a level is removed
    """
    print("in problem dampener")
    global safe_reports

    print("original unsafe report: ", report)
    for i in range(len(report)):
        instance_safe = False
        temp = report.copy()
        temp.pop(i)
        print("temp: ", temp)
        if isAscOrDesc(temp):
            instance_safe = True
            for i in range(len(temp)-1):
                if not isSafeAdjacent(temp[i], temp[i+1]):
                    instance_safe = False
        else:
            instance_safe = False
        
        if instance_safe:
            safe_reports += 1
            print(f"problem dampener fixed with: {temp}") 
            break

setup()
evaluate()
print(f"safe reports including problem dampener: {safe_reports}")