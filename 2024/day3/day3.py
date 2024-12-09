import re
pattern = r"mul\(\d{1,3},\d{1,3}\)" # matches mul(#,#)
pattern_do = r"do\(\)(.*?)don't\(\)"

to_multiply = []

matches_do = []
to_multiply_p2 = []

def setup():
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            matches = re.findall(pattern, line)
            regex_do = re.findall(pattern_do, line)
            if regex_do:
                matches_do.extend(regex_do)
            if matches:
                to_multiply.extend(matches)

def evaluate():
    """ part 1"""
    total = 0
    for item in to_multiply:
        values = item.strip('mul(').strip(')').split(',')
        total += int(values[0]) * int(values[1])
    print(f"part 1 total {total}")

def evaluate_p2():
    """ part 2"""
    total = 0

    for text in matches_do:
        to_multiply_p2.extend(re.findall(pattern, text))
    for item in to_multiply_p2:
        values = item.strip('mul(').strip(')').split(',')
        total += int(values[0]) * int(values[1])
    print(f"part 2 total {total}")


setup()
evaluate()
evaluate_p2()

