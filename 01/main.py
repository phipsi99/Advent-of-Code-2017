from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('01/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('01/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    input = [int(i) for i in list(lines[0])]
    sum = 0

    for index, i in enumerate(input):
        if index == len(input)-1:
            if i == input[0]:
                sum+=i
        elif i == input[index+1]:
            sum+=i    
    print(sum)
    
    sum = 0
    length = int(len(input) / 2)
    for index, i in enumerate(input):
        if index + length >= len(input):
            if i == input[(length + index) % len(input)]:
                sum+=i
        elif i == input[index+length]:
            sum+=i    
    print(sum)
    
if __name__ == '__main__':
    do_main(False)