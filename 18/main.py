from pathlib import Path
import winsound

def run_instruction(registers, instructions, last_freq, pointer):
    op, register, val = instructions[pointer]
    if val:
        try:
            val = int(val)
        except ValueError:
            val = registers[val]
    if op == "snd":
        last_freq = registers[register]
        winsound.Beep(registers[register], 100)
    elif op == "set":
        registers[register] = val
    elif op == "add":
        registers[register] += val
    elif op == "mul":
        registers[register] *= val
    elif op == "mod":
        registers[register] %= val
    elif op == "rcv":
        if registers[register] != 0:
            return pointer, last_freq, last_freq
    elif op == "jgz":
        if registers[register] > 0:
            pointer += val - 1
    pointer += 1
    return pointer, last_freq, None

def run_instruction2(registers, instructions, pointer, recieved: list):
    op, register, val = instructions[pointer]
    snd_val = None
    blocked = False
    if val:
        try:
            val = int(val)
        except ValueError:
            val = registers[val]
    if op == "snd":
        try:
            val = int(register)
        except ValueError:
            val = registers[register]
        snd_val = val
    elif op == "set":
        registers[register] = val
    elif op == "add":
        registers[register] += val
    elif op == "mul":
        registers[register] *= val
    elif op == "mod":
        registers[register] %= val
    elif op == "rcv":
        if len(recieved) > 0:
            registers[register] = recieved.pop(0)
        else:
            blocked = True
            return pointer, snd_val, blocked
    elif op == "jgz":
        try:
            cmp_val = int(register)
        except ValueError:
            cmp_val = registers[register]
        if cmp_val > 0:
            pointer += val - 1
    pointer += 1
    return pointer, snd_val, blocked


def do_main(debug_mode=False):
    with open(Path('18/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('18/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    registers = {}
    instructions = []

    for line_index, line in enumerate(lines):
        instruction = line.split(" ")
        op = instruction[0]
        register = instruction[1]
        val = instruction[2] if len(instruction) > 2 else None
        instructions.append((op, register, val))
        registers[register] = 0


    last_freq = 0
    pointer = 0
    while pointer < len(instructions):
        pointer, last_freq, rcv = run_instruction(registers, instructions, last_freq, pointer)
        if rcv:
            print(rcv)
            break

    pointer_0 = 0
    pointer_1 = 0
    recieve_queue_0 = []
    recieve_queue_1 = []
    registers_0 = registers.copy()
    registers_1 = registers.copy()
    registers_0["p"] = 0
    registers_1["p"] = 1
    snd_count = 0

    blocked0 = blocked1 = False
    while True:
        pointer_0_old, pointer_1_old = pointer_0, pointer_1
        if pointer_0 < len(instructions):
            pointer_0, snd_val, blocked0 = run_instruction2(registers_0, instructions, pointer_0, recieve_queue_0)
            if snd_val != None:
                recieve_queue_1.append(snd_val)
        if pointer_1 < len(instructions):
            pointer_1, snd_val, blocked1 = run_instruction2(registers_1, instructions, pointer_1, recieve_queue_1)
            if snd_val != None:
                snd_count += 1
                recieve_queue_0.append(snd_val)
        if blocked0 and blocked1 and not recieve_queue_0 and not recieve_queue_1:
            break


    print(snd_count)


if __name__ == '__main__':
    do_main(False)