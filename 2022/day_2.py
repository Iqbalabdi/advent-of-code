file = open("input.txt", "r")
score, round, sum = 0, 0, 0
for line in file:
    sline = line.rstrip().split()
    ### PART 1
    # if sline[0] == 'A':
    #     if sline[1] == 'X':
    #         score = 1
    #         round = 3
    #     elif sline[1] == 'Y':
    #         score = 2
    #         round = 6
    #     elif sline[1] == 'Z':
    #         score = 3
    #         round = 0
    # elif sline[0] == 'B':
    #     if sline[1] == 'X':
    #         score = 1
    #         round = 0
    #     elif sline[1] == 'Y':
    #         score = 2
    #         round = 3
    #     elif sline[1] == 'Z':
    #         score = 3
    #         round = 6
    # elif sline[0] == 'C':
    #     if sline[1] == 'X':
    #         score = 1
    #         round = 6
    #     elif sline[1] == 'Y':
    #         score = 2
    #         round = 0
    #     elif sline[1] == 'Z':
    #         score = 3
    #         round = 3
    ### PART 2
    if sline[0] == 'A':
        if sline[1] == 'X':
            round = 0
            score = 3
        elif sline[1] == 'Y':
            round = 3
            score = 1
        elif sline[1] == 'Z':
            score = 2
            round = 6
    elif sline[0] == 'B':
        if sline[1] == 'X':
            score = 1
            round = 0
        elif sline[1] == 'Y':
            score = 2
            round = 3
        elif sline[1] == 'Z':
            score = 3
            round = 6
    elif sline[0] == 'C':
        if sline[1] == 'X':
            score = 2
            round = 0
        elif sline[1] == 'Y':
            score = 3
            round = 3
        elif sline[1] == 'Z':
            score = 1
            round = 6
    sum += score + round
print(sum)
