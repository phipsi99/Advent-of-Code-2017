from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('09/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('09/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    stream = lines[0]
    #stream = "<{o\"i!a,<{i<a>"
    
    score = 0
    group_open = 0
    garbage_open = False
    garbage = 0
    skip = False
    for c in stream:
        if skip:
            skip = False
        elif c == "!":
            skip = True
        elif c == "<":
            if garbage_open:
                garbage += 1
            garbage_open = True
        elif garbage_open and c != ">":
            garbage += 1
            continue
        elif garbage_open and c == ">":
            garbage_open = False
        elif c == "{":
            group_open += 1
        elif c == "}" and group_open > 0:
            score += group_open
            group_open -= 1
        
    print(score)
    print(garbage)
            

if __name__ == '__main__':
    do_main(False)