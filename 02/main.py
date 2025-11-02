from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('02/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('02/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    point_sum2 = 0

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]
        point_sum += max(r)-min(r)
        for number in r:
            other_list = r.copy()
            other_list.remove(number)
            for other_number in other_list:
                if number % other_number == 0:
                    point_sum2 += number / other_number
    print(point_sum)
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)