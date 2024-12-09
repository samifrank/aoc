import re

word_search = {} # {row# : [letters]}
xmas_count = 0

def setup():
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            word_search[i] = (list(lines[i].strip()))
    #example part 1. 18 XMAS instances:   
    # global word_search 
    # word_search = {
    #      0: list('MMMSXXMASM'),
    #     1: list('MSAMXMSMSA'),
    #     2: list('AMXSXMAAMM'),
    #     3: list('MSAMASMSMX'),
    #     4: list('XMASAMXAMM'),
    #     5: list('XXAMMXXAMA'),
    #     6: list('SMSMSASXSS'),
    #     7: list('SAXAMASAAA'),
    #     8: list('MAMMMXMMMM'),
    #     9: list('MXMXAXMASX')
    # }
    # print(word_search)

    #example part 2.  MAS (in the shape of X)  9 instances:
    # global word_search 
    # word_search = {
    #     0: list('.M.S......'),
    #     1: list('..A..MSMS.'),
    #     2: list('.M.S.MAA..'),
    #     3: list('..A.ASMSM.'),
    #     4: list('.M.S.M....'),
    #     5: list('..........'),
    #     6: list('S.S.S.S.S.'),
    #     7: list('.A.A.A.A..'),
    #     8: list('M.M.M.M.M.'),
    #     9: list('..........')
    # }   
    # print(word_search)

def find_horizontal(text: str) -> int:
    return len(re.findall(r'XMAS', text))

def find_vertical() -> list:

    made_horizontal = []
    row_length = len(word_search[0])
    for i in range(row_length):
        vertical_text = ''
        for letters in word_search.values():
            vertical_text += letters[i]
        made_horizontal.append(vertical_text)
    
    return made_horizontal


def find_diagonal(word_search = word_search) -> list:
    # print(word_search)

    size = len(word_search)
    top_diagonals = []
    bottom_diagonals = []

    #top left to bottom right
    for start in range(size):
        top_diagonal = ''
        bottom_diagonal = ''
        for i in range(size - start):
            top_diagonal += word_search[start+i][i]
            if start != 0:
                bottom_diagonal += word_search[i][start+i]
        top_diagonals.append(top_diagonal)
        if start != 0:
            bottom_diagonals.append(bottom_diagonal)

    #top right to bottom left
    for start in range(size):
        top_diagonal = ''
        bottom_diagonal = ''
        for i in range(size - start):
            top_diagonal += word_search[start+i][size - i - 1]
            if start != 0:
                bottom_diagonal += word_search[i][size - 1 - (start + i )]
        top_diagonals.append(top_diagonal)
        if start != 0:
            bottom_diagonals.append(bottom_diagonal)
    # print(all_diagonals)
    return top_diagonals + bottom_diagonals

def find_backwards(texts):
    backwards = []
    for text in texts:
        backwards.append(text[::-1])
    return backwards


def find_mas_x() -> int:
    count = 0
    size = len(word_search) #example -> 10

    for i in range(size - 2):
        for j in range(len(word_search[i]) - 2):
            # Extract the 3x3 subgrid
            subgrid = [
                word_search[i][j:j+3],
                word_search[i+1][j:j+3],
                word_search[i+2][j:j+3]
            ]
            # {0: ['M', '.', 'S'],
    #          1: ['.', 'A', '.'],
    #         2: ['M', '.', 'S']
    #         }
            # Check for the "MAS" & MAS pattern in the shape of an "X"
            if (subgrid[0][0] == 'M' and
                subgrid[1][1] == 'A' and
                subgrid[2][2] == 'S' and

                subgrid[2][0] == 'M' and
                subgrid[0][2] == 'S' 
                ):
                count += 1
            # Check for the "SAM" & "SAM" pattern in the shape of an "X" (vertical flip)
            if (subgrid[0][0] == 'S' and
                subgrid[1][1] == 'A' and
                subgrid[2][2] == 'M' and

                subgrid[2][0] == 'S' and
                subgrid[0][2] == 'M' 
                ):
                count += 1
            # Check for the "MAS" & "SAM" pattern in the shape of an "X" (horizontal flip)
            if (subgrid[0][0] == 'M' and
                subgrid[1][1] == 'A' and
                subgrid[2][2] == 'S' and

                subgrid[2][0] == 'S' and
                subgrid[0][2] == 'M' 
                ):
                count += 1
            # Check for the "SAM" & "MAS" pattern in the shape of an "X" (180-degree rotation)
            if (subgrid[0][0] == 'S' and
                subgrid[1][1] == 'A' and
                subgrid[2][2] == 'M' and

                subgrid[2][0] == 'M' and
                subgrid[0][2] == 'S' 
                ):
                count += 1
    return count
    
setup()

# ['MAS', '..', 'M', 'SAM', '..', 'S', '..', 'S', '..', 'M']
#PART 1
#horizonal
for text in word_search.values():
    xmas_count += find_horizontal(''.join(text))
print(f"XMAS count total with horizontal: {xmas_count}")

# vertical
vert_made_horizontal = find_vertical()
for text in vert_made_horizontal:
    xmas_count += find_horizontal(text)

print(f"XMAS count total including vertical: {xmas_count}")

# diagonal
diag_made_horizontal = find_diagonal()
for text in diag_made_horizontal:
    xmas_count += find_horizontal(text)
print(f"XMAS count total including diagonal: {xmas_count}")

# backwards horizontal
for text in word_search.values():
    xmas_count += find_horizontal(''.join(text[::-1]))
print(f"XMAS count total backwards horizontal: {xmas_count}")

#backwards vertical
backwards_vert_made_horizontal = find_backwards(vert_made_horizontal)
for text in backwards_vert_made_horizontal:
    xmas_count += find_horizontal(text)
print(f"XMAS count total including backwards vertical: {xmas_count}")

#backwards diagonal
backwards_diag_made_horizontal = find_backwards(diag_made_horizontal)
for text in backwards_diag_made_horizontal:
    xmas_count += find_horizontal(text)
print(f"XMAS count total including backwards diagonal: {xmas_count}")

print(f"XMAS count total including all: {xmas_count}")

#PART 2
print(f"mas_x count: {find_mas_x()}")