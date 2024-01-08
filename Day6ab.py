hold = 0
final_time = """
Time:        56     97     77     93
Distance:   499   2210   1097   1440
"""

def calc_win(time, dist):
    counter = 0
    for i in range(time):
        hold = i
        result = (time - hold)*hold
        if result > dist:
            counter += 1
    return counter

def main():
    time = [56, 97, 77, 93]
    dist = [499, 2210, 1097, 1440]
    answer = calc_win(56977793,499221010971440)
    print(answer)
    print (33*24*40*54)

main()

