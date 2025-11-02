from pathlib import Path
import operator

ops = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    ">=": operator.ge
}

def do_main(debug_mode=False):
    with open(Path('08/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('08/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    highest = 0
    registers = {}

    for line_index, line in enumerate(lines):
        parts = line.split(" ")
        register_to_modify = parts[0]
        operation = parts[1]
        value = int(parts[2])
        register_to_check = parts[4]
        comparison = parts[5]
        value_to_compare_to = int(parts[6])
        
        value_to_add = 0
        if operation == "inc":
            value_to_add = value
        else:
            value_to_add = -value
            
        if register_to_check not in registers:
            registers[register_to_check] = 0
        if register_to_modify not in registers:
            registers[register_to_modify] = 0
            
        if ops[comparison](registers[register_to_check], value_to_compare_to):
            registers[register_to_modify] += value_to_add
        
        highest = max(highest, max(registers.values()))
            
    print(max(registers.values()))
    print(highest)

if __name__ == '__main__':
    do_main(False)