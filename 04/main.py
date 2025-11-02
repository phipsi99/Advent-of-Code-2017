from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('04/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('04/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        r = [str(i) for i in line.split(" ")]
        if len(r) == len(set(r)):
            point_sum += 1
        valid = True
        for word in r:
            other_words = r.copy()
            other_words.remove(word)
            for other_word in other_words:
                if other_word == word or sorted(list(other_word)) == sorted(list(word)):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            point_sum2 += 1
            
            
    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)